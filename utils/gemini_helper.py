"""
Gemini AI Helper for THY Cadet Pilot Prep App
Handles all Gemini API interactions and content generation
"""

import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Any
import streamlit as st

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

from utils.config import config


class GeminiHelper:
    """Helper class for Gemini API interactions"""
    
    def __init__(self):
        self._model = None
        self._cache_dir = Path(__file__).parent.parent / ".cache"
        self._cache_dir.mkdir(exist_ok=True)
    
    @property
    def is_available(self) -> bool:
        """Check if Gemini is available and configured"""
        return GEMINI_AVAILABLE and config.gemini_enabled
    
    def _get_available_models(self) -> List[str]:
        """Get list of available Gemini models that support content generation"""
        if not self.is_available:
            return []
        
        try:
            genai.configure(api_key=config.gemini_api_key)
            available = []
            for model in genai.list_models():
                if 'generateContent' in [m for m in model.supported_generation_methods]:
                    # Store clean name without "models/" prefix
                    clean_name = model.name.replace("models/", "")
                    if 'gemini' in clean_name.lower():
                        available.append(clean_name)
            return sorted(available)
        except Exception:
            return []
    
    def _get_model(self):
        """Get or create Gemini model instance, with user selection if preferred model unavailable"""
        if self._model is None and self.is_available:
            genai.configure(api_key=config.gemini_api_key)
            
            # Get available models
            available_models = self._get_available_models()
            
            if not available_models:
                st.error("❌ No Gemini models available for your API key. Check your API key permissions.")
                return None
            
            # Check if preferred model from config is available
            preferred_model = config.gemini_model
            
            # Initialize session state for model selection
            if 'selected_gemini_model' not in st.session_state:
                st.session_state.selected_gemini_model = None
            
            if preferred_model in available_models:
                # Preferred model is available, use it
                selected_model = preferred_model
            elif st.session_state.selected_gemini_model and st.session_state.selected_gemini_model in available_models:
                # User has already selected a model
                selected_model = st.session_state.selected_gemini_model
            else:
                # Preferred model not available, show warning and let user select
                st.warning(f"⚠️ Preferred model '{preferred_model}' is not available.")
                
                # Show available models for user to select
                st.markdown("**Select an available model:**")
                selected_model = st.selectbox(
                    "Available Gemini Models",
                    options=available_models,
                    key="gemini_model_selector",
                    help="Select a model to use for AI features"
                )
                
                if st.button("✅ Use Selected Model", key="confirm_model"):
                    st.session_state.selected_gemini_model = selected_model
                    st.rerun()
                
                # Don't proceed until user confirms
                if not st.session_state.selected_gemini_model:
                    return None
                
                selected_model = st.session_state.selected_gemini_model
            
            try:
                self._model = genai.GenerativeModel(selected_model)
                st.toast(f"✅ Connected to {selected_model}")
            except Exception as e:
                st.error(f"Failed to initialize model {selected_model}: {str(e)}")
                return None
        
        return self._model
    
    def _get_page_cache_file(self, page_name: str) -> Path:
        """Get the cache file path for a specific page"""
        return self._cache_dir / f"history_{page_name}.json"
    
    def _load_page_cache(self, page_name: str) -> List[Dict[str, Any]]:
        """Load cache history for a page"""
        cache_file = self._get_page_cache_file(page_name)
        if cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_to_page_cache(self, page_name: str, response_data: Any):
        """Save response to page cache history (keeps last 5)"""
        cache_file = self._get_page_cache_file(page_name)
        history = self._load_page_cache(page_name)
        
        # Add new entry
        entry = {
            'timestamp': datetime.now().isoformat(),
            'data': response_data
        }
        history.insert(0, entry)  # Add to front
        
        # Keep only last 5
        history = history[:5]
        
        with open(cache_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def get_cache_history(self, page_name: str) -> List[Dict[str, Any]]:
        """Get cache history for a page (public method)"""
        return self._load_page_cache(page_name)
    
    def _get_cache_key(self, prompt: str, context: str = "") -> str:
        """Generate cache key from prompt and context"""
        content = f"{prompt}:{context}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def _get_cached_response(self, cache_key: str) -> Optional[str]:
        """Get cached response if available and not expired"""
        if not config.cache_enabled:
            return None
        
        cache_file = self._cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    cached = json.load(f)
                
                cached_time = datetime.fromisoformat(cached['timestamp'])
                if datetime.now() - cached_time < timedelta(hours=config.cache_duration_hours):
                    return cached['response']
            except (json.JSONDecodeError, KeyError):
                pass
        
        return None
    
    def _save_to_cache(self, cache_key: str, response: str):
        """Save response to cache"""
        if not config.cache_enabled:
            return
        
        cache_file = self._cache_dir / f"{cache_key}.json"
        with open(cache_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'response': response
            }, f)
    
    def generate(self, prompt: str, context: str = "", use_cache: bool = True) -> Optional[str]:
        """Generate content using Gemini API"""
        if not self.is_available:
            return None
        
        cache_key = self._get_cache_key(prompt, context)
        
        # Check cache first
        if use_cache:
            cached = self._get_cached_response(cache_key)
            if cached:
                return cached
        
        try:
            model = self._get_model()
            if model is None:
                st.error("Could not initialize Gemini model. Check your API key and internet connection.")
                return None
            
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            response = model.generate_content(full_prompt)
            result = response.text
            
            # Cache the response
            self._save_to_cache(cache_key, result)
            
            return result
        except Exception as e:
            st.error(f"Gemini API error: {str(e)}")
            return None
    
    def _parse_json_response(self, response: str) -> Any:
        """Parse JSON from Gemini response, handling code blocks"""
        if not response:
            return None
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        try:
            return json.loads(response.strip())
        except json.JSONDecodeError:
            return None

    def get_dictionary_additions(self, existing_terms: List[str], use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get additional aviation terms from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('dictionary'):
            return []
        
        context = f"""You are an aviation expert helping a pilot candidate prepare for their Turkish Airlines interview.
        
The following aviation terms/abbreviations are already in the dictionary:
{', '.join(existing_terms[:50])}... (and {len(existing_terms) - 50} more)

Please suggest 15-20 ADDITIONAL important aviation terms that are NOT in the list above.
Focus on terms that would be relevant for a cadet pilot interview."""

        prompt = """Return your response as a valid JSON array with this exact format:
[
  {
    "term": "TERM_OR_ABBREVIATION",
    "full_name": "Full Name or Description",
    "category": "One of: Aerodynamics, Navigation, Meteorology, Aircraft Systems, Regulations, Communications, Instruments, Emergencies, Human Factors, Flight Operations, Airport, ATC, V-Speeds",
    "difficulty": "One of: Basic, Intermediate, Advanced",
    "definition": "Clear definition of the term (1-2 sentences)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        terms = self._parse_json_response(response)
        
        if terms and isinstance(terms, list):
            # Save to page cache
            self._save_to_page_cache('dictionary', terms)
            return terms
        return []
    
    def get_news_updates(self, use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get recent aviation news from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('news'):
            return []
        
        context = """You are an aviation industry analyst helping a Turkish Airlines cadet pilot candidate 
prepare for their interview scheduled for March/April 2026."""

        prompt = """Provide 5-7 recent and important aviation news items that would be relevant for a pilot interview.
Focus on: industry trends, safety developments, Turkish Airlines news, technology advances, and significant incidents.

Return your response as a valid JSON array with this exact format:
[
  {
    "title": "News headline",
    "date": "2025 or 2026",
    "category": ["Category1", "Category2"],
    "content": "Brief summary of the news (2-3 sentences)",
    "interview_tip": "How this might come up in an interview (1 sentence)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        news = self._parse_json_response(response)
        
        if news and isinstance(news, list):
            self._save_to_page_cache('news', news)
            return news
        return []
    
    def get_history_additions(self, existing_years: List[int], use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get additional aviation history events from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('history'):
            return []
        
        context = f"""You are an aviation historian helping a pilot candidate learn aviation history.
        
The following years already have events covered:
{', '.join(map(str, sorted(existing_years)))}"""

        prompt = """Suggest 10 additional important aviation historical events that are NOT in the years listed.
Include events from early aviation to modern times.

Return your response as a valid JSON array with this exact format:
[
  {
    "year": 1950,
    "era": "One of: Pioneers, Early Aviation, Golden Age, World War II, Jet Age, Modern Era",
    "title": "Event Title",
    "content": "Description of the event and its significance (2-3 sentences)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        events = self._parse_json_response(response)
        
        if events and isinstance(events, list):
            self._save_to_page_cache('history', events)
            return events
        return []
    
    def get_fleet_insights(self, fleet_summary: str, use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get fleet insights from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('fleet'):
            return []
        
        context = f"""You are an aviation expert helping a Turkish Airlines cadet pilot candidate.
        
Current THY Fleet Summary:
{fleet_summary}"""

        prompt = """Provide 5-7 interesting insights about Turkish Airlines' fleet that would be useful for a pilot interview.
Include facts about fleet strategy, aircraft capabilities, operational efficiency, and comparisons.

Return your response as a valid JSON array with this exact format:
[
  {
    "title": "Insight Title",
    "category": "One of: Fleet Strategy, Aircraft Specs, Operations, Efficiency, Industry Comparison",
    "content": "Detailed insight (2-3 sentences)",
    "interview_tip": "How this might be relevant in an interview (1 sentence)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        insights = self._parse_json_response(response)
        
        if insights and isinstance(insights, list):
            self._save_to_page_cache('fleet', insights)
            return insights
        return []
    
    def get_destinations_insights(self, destinations_summary: str, use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get destinations insights from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('destinations'):
            return []
        
        context = f"""You are an aviation expert helping a Turkish Airlines cadet pilot candidate.
        
Current THY Network Summary:
{destinations_summary}"""

        prompt = """Provide 5-7 interesting insights about Turkish Airlines' route network that would be useful for a pilot interview.
Include facts about hub strategy, key markets, growth areas, and competitive positioning.

Return your response as a valid JSON array with this exact format:
[
  {
    "title": "Insight Title",
    "category": "One of: Hub Strategy, Key Markets, Growth, Competition, Geography",
    "content": "Detailed insight (2-3 sentences)",
    "interview_tip": "How this might be relevant in an interview (1 sentence)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        insights = self._parse_json_response(response)
        
        if insights and isinstance(insights, list):
            self._save_to_page_cache('destinations', insights)
            return insights
        return []
    
    def get_future_insights(self, existing_topics: List[str], use_cache: bool = False) -> List[Dict[str, Any]]:
        """Get additional future aviation insights from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('future'):
            return []
        
        context = f"""You are an aviation technology analyst providing insights about the future of aviation.
        
Topics already covered include:
{', '.join(existing_topics)}"""

        prompt = """Suggest 5 additional emerging technologies or trends in aviation that are NOT already covered.
Focus on developments that would be relevant for a pilot candidate to know about.

Return your response as a valid JSON array with this exact format:
[
  {
    "title": "Technology or Trend Name",
    "timeline": "Expected timeline (e.g., 2025-2030)",
    "category": "One of: Sustainability, Technology, Aircraft, Operations",
    "content": "Description of the technology/trend and its impact (3-4 sentences)",
    "interview_tip": "Why this is relevant for an interview (1 sentence)"
  }
]

Return ONLY the JSON array, no other text."""

        response = self.generate(prompt, context, use_cache=use_cache)
        insights = self._parse_json_response(response)
        
        if insights and isinstance(insights, list):
            self._save_to_page_cache('future', insights)
            return insights
        return []
    
    def get_training_aircraft_tips(self, aircraft: str, existing_content: str) -> Optional[str]:
        """Get additional tips for training aircraft from Gemini"""
        if not self.is_available or not config.is_ai_enabled_for('training_aircraft'):
            return None
        
        context = f"""You are a flight instructor helping a student prepare for their interview about the {aircraft}.
        
The student already knows about:
{existing_content[:1000]}..."""

        prompt = f"""Provide 3-5 additional interview tips or key points about the {aircraft} that would help 
a cadet pilot candidate. Focus on things an interviewer might ask about.

Format your response as a bullet-point list that can be displayed directly. Keep it concise."""

        return self.generate(prompt, context)


def render_ai_content_indicator():
    """Render the AI content indicator/badge"""
    color = config.ai_indicator_color
    st.markdown(f"""
    <div style="display: inline-flex; align-items: center; gap: 0.5rem; 
                padding: 0.3rem 0.8rem; background: {color}22; 
                border: 1px solid {color}66; border-radius: 20px;
                font-size: 0.85rem; color: {color};">
        <span>🤖</span>
        <span>AI-Generated Content</span>
    </div>
    """, unsafe_allow_html=True)


def render_ai_disclaimer():
    """Render AI content disclaimer"""
    if config.show_ai_disclaimer:
        st.markdown("""
        <div style="padding: 0.5rem 1rem; background: rgba(155, 89, 182, 0.1); 
                    border-left: 3px solid #9b59b6; border-radius: 0 8px 8px 0;
                    font-size: 0.85rem; color: #888; margin: 1rem 0;">
            ⚠️ <strong>AI-Generated Content:</strong> The items marked with 🤖 are generated by Gemini AI 
            and may not be 100% accurate. Always verify important information from official sources.
        </div>
        """, unsafe_allow_html=True)


def render_ai_card(content: Dict[str, Any], card_type: str = "generic"):
    """Render an AI-generated content card with indicator"""
    color = config.ai_indicator_color
    
    if card_type == "dictionary":
        st.markdown(f"""
        <div style="background: linear-gradient(145deg, rgba(155, 89, 182, 0.15), rgba(155, 89, 182, 0.05));
                    border: 1px solid {color}44; border-radius: 12px; padding: 1.2rem; margin: 0.8rem 0;
                    position: relative;">
            <div style="position: absolute; top: 0.5rem; right: 0.5rem; font-size: 0.75rem; 
                        color: {color}; background: {color}22; padding: 0.2rem 0.5rem; border-radius: 10px;">
                🤖 AI
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 600; color: {color};">
                {content.get('term', '')}
            </div>
            <div style="font-size: 1.1rem; color: #fff; margin: 0.3rem 0;">
                {content.get('full_name', '')}
            </div>
            <div style="font-size: 0.95rem; color: #b0b0b0; line-height: 1.6;">
                {content.get('definition', '')}
            </div>
            <div style="margin-top: 0.5rem;">
                <span style="display: inline-block; padding: 0.2rem 0.6rem; background: {color}22; 
                            border: 1px solid {color}44; border-radius: 15px; font-size: 0.75rem; color: {color};">
                    {content.get('category', '')}
                </span>
                <span style="display: inline-block; padding: 0.2rem 0.6rem; background: rgba(46, 213, 115, 0.15); 
                            border: 1px solid rgba(46, 213, 115, 0.3); border-radius: 15px; font-size: 0.75rem; 
                            color: #2ed573; margin-left: 0.3rem;">
                    {content.get('difficulty', '')}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif card_type == "news":
        categories = content.get('category', [])
        if isinstance(categories, str):
            categories = [categories]
        cat_html = ''.join([f'<span style="display: inline-block; padding: 0.2rem 0.5rem; background: {color}22; border-radius: 10px; font-size: 0.75rem; color: {color}; margin-right: 0.3rem;">{cat}</span>' for cat in categories])
        
        st.markdown(f"""
        <div style="background: linear-gradient(145deg, rgba(155, 89, 182, 0.15), rgba(155, 89, 182, 0.05));
                    border: 1px solid {color}44; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    position: relative;">
            <div style="position: absolute; top: 0.5rem; right: 0.5rem; font-size: 0.75rem; 
                        color: {color}; background: {color}22; padding: 0.2rem 0.5rem; border-radius: 10px;">
                🤖 AI-Generated
            </div>
            <h3 style="color: #fff; margin-bottom: 0.5rem;">{content.get('title', '')}</h3>
            <p style="color: {color}; font-size: 0.9rem; margin-bottom: 0.5rem;">📅 {content.get('date', '')}</p>
            <div style="margin-bottom: 0.5rem;">{cat_html}</div>
            <p style="color: #d0d0d0; line-height: 1.8;">{content.get('content', '')}</p>
            <div style="background: rgba(255, 193, 7, 0.1); border: 1px solid rgba(255, 193, 7, 0.3); 
                        border-radius: 8px; padding: 0.8rem; margin-top: 0.8rem;">
                <strong style="color: #ffc107;">💡 Interview Tip:</strong>
                <span style="color: #d0d0d0;"> {content.get('interview_tip', '')}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif card_type == "history":
        st.markdown(f"""
        <div style="background: linear-gradient(145deg, rgba(155, 89, 182, 0.15), rgba(155, 89, 182, 0.05));
                    border-left: 4px solid {color}; border-radius: 0 12px 12px 0; padding: 1.5rem; margin: 1rem 0;
                    position: relative;">
            <div style="position: absolute; top: 0.5rem; right: 0.5rem; font-size: 0.75rem; 
                        color: {color}; background: {color}22; padding: 0.2rem 0.5rem; border-radius: 10px;">
                🤖 AI
            </div>
            <div style="font-size: 1.8rem; font-weight: 700; color: {color};">
                {content.get('year', '')}
            </div>
            <div style="font-size: 1.3rem; font-weight: 600; color: #fff; margin: 0.3rem 0;">
                {content.get('title', '')}
            </div>
            <div style="font-size: 1rem; color: #d0d0d0; line-height: 1.6;">
                {content.get('content', '')}
            </div>
            <span style="display: inline-block; padding: 0.2rem 0.6rem; background: {color}22; 
                        border: 1px solid {color}44; border-radius: 15px; font-size: 0.75rem; color: {color}; margin-top: 0.5rem;">
                {content.get('era', '')}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    elif card_type == "insight":
        # Generic insight card for fleet/destinations
        st.markdown(f"""
        <div style="background: linear-gradient(145deg, rgba(155, 89, 182, 0.15), rgba(155, 89, 182, 0.05));
                    border: 1px solid {color}44; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    position: relative;">
            <div style="position: absolute; top: 0.5rem; right: 0.5rem; font-size: 0.75rem; 
                        color: {color}; background: {color}22; padding: 0.2rem 0.5rem; border-radius: 10px;">
                🤖 AI-Generated
            </div>
            <h3 style="color: #fff; margin-bottom: 0.5rem;">{content.get('title', '')}</h3>
            <span style="display: inline-block; padding: 0.2rem 0.6rem; background: {color}22; 
                        border: 1px solid {color}44; border-radius: 15px; font-size: 0.75rem; color: {color}; margin-bottom: 0.8rem;">
                {content.get('category', '')}
            </span>
            <p style="color: #d0d0d0; line-height: 1.8;">{content.get('content', '')}</p>
            <div style="background: rgba(255, 193, 7, 0.1); border: 1px solid rgba(255, 193, 7, 0.3); 
                        border-radius: 8px; padding: 0.8rem; margin-top: 0.8rem;">
                <strong style="color: #ffc107;">💡 Interview Tip:</strong>
                <span style="color: #d0d0d0;"> {content.get('interview_tip', '')}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_cache_history(page_name: str, card_type: str = "generic"):
    """Render cache history for a page with expandable sections"""
    history = gemini.get_cache_history(page_name)
    
    if not history:
        st.info("No cached responses yet. Generate AI content first.")
        return
    
    st.markdown(f"**📜 Previous AI Responses ({len(history)} saved)**")
    
    for i, entry in enumerate(history):
        timestamp = entry.get('timestamp', 'Unknown')
        try:
            dt = datetime.fromisoformat(timestamp)
            time_str = dt.strftime("%b %d, %Y at %H:%M")
        except:
            time_str = timestamp
        
        with st.expander(f"Response {i+1} - {time_str}", expanded=(i == 0)):
            data = entry.get('data', [])
            if isinstance(data, list):
                for item in data:
                    render_ai_card(item, card_type)
            else:
                st.write(data)


def render_ai_section(page_name: str, card_type: str, generate_func, generate_args: tuple = (), 
                      section_title: str = "🤖 AI Insights"):
    """Render a complete AI section with fresh/cached buttons for a page"""
    
    if not config.is_ai_enabled_for(page_name):
        if gemini.is_available:
            st.markdown(f"""
            <div style="padding: 1rem; background: rgba(100, 100, 100, 0.1); border-radius: 8px; text-align: center;">
                <p style="color: #888;">🤖 AI enhancements available but disabled for this page.</p>
                <p style="color: #666; font-size: 0.85rem;">Enable in <code>config.yaml</code> → <code>ai_enhancements.{page_name}: true</code></p>
            </div>
            """, unsafe_allow_html=True)
        return
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"### {section_title}")
    
    render_ai_disclaimer()
    
    # Session state keys
    current_key = f'ai_{page_name}_current'
    show_history_key = f'ai_{page_name}_show_history'
    
    if current_key not in st.session_state:
        st.session_state[current_key] = None
    if show_history_key not in st.session_state:
        st.session_state[show_history_key] = False
    
    # Buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🔄 Get Fresh AI Response", key=f"fresh_{page_name}", use_container_width=True):
            with st.spinner("Generating fresh AI content..."):
                result = generate_func(*generate_args, use_cache=False)
                st.session_state[current_key] = result
                st.session_state[show_history_key] = False
    
    with col2:
        if st.button("📜 Show Previous Responses", key=f"history_{page_name}", use_container_width=True):
            st.session_state[show_history_key] = not st.session_state[show_history_key]
    
    with col3:
        history = gemini.get_cache_history(page_name)
        st.caption(f"📦 {len(history)} cached")
    
    # Display current results
    if st.session_state[current_key]:
        st.markdown("**✨ Current AI Response:**")
        for item in st.session_state[current_key]:
            render_ai_card(item, card_type)
    
    # Display history
    if st.session_state[show_history_key]:
        st.markdown("<br>", unsafe_allow_html=True)
        render_cache_history(page_name, card_type)


# Singleton instance
gemini = GeminiHelper()

