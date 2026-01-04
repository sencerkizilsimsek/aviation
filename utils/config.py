"""
Configuration Manager for THY Cadet Pilot Prep App
Handles loading and accessing configuration from config.yaml
"""

import os
import yaml
from pathlib import Path


class Config:
    """Configuration manager singleton"""
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Load configuration from config.yaml"""
        config_path = Path(__file__).parent.parent / "config.yaml"
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                self._config = yaml.safe_load(f)
        else:
            # Default configuration if file doesn't exist
            self._config = {
                'gemini': {
                    'api_key': '',
                    'model': 'gemini-1.5-flash',
                    'enabled': False
                },
                'ai_enhancements': {
                    'dictionary': False,
                    'news': False,
                    'history': False,
                    'future': False,
                    'fleet': False,
                    'destinations': False,
                    'training_aircraft': False
                },
                'ai_display': {
                    'highlight_ai_content': True,
                    'indicator_color': '#9b59b6',
                    'show_disclaimer': True
                },
                'cache': {
                    'enabled': True,
                    'duration_hours': 24
                }
            }
    
    def reload(self):
        """Reload configuration from file"""
        self._load_config()
    
    @property
    def gemini_api_key(self) -> str:
        """Get Gemini API key"""
        # Priority: Streamlit secrets > Environment variable > config file
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'gemini' in st.secrets:
                secret_key = st.secrets.get('gemini', {}).get('api_key', '')
                if secret_key:
                    return secret_key
        except:
            pass
        
        # Check environment variable
        env_key = os.environ.get('GEMINI_API_KEY', '')
        if env_key:
            return env_key
        
        # Fallback to config file (for local development)
        return self._config.get('gemini', {}).get('api_key', '')
    
    @property
    def gemini_model(self) -> str:
        """Get Gemini model name"""
        return self._config.get('gemini', {}).get('model', 'gemini-1.5-flash')
    
    @property
    def gemini_enabled(self) -> bool:
        """Check if Gemini is globally enabled"""
        return self._config.get('gemini', {}).get('enabled', False) and bool(self.gemini_api_key)
    
    def is_ai_enabled_for(self, page: str) -> bool:
        """Check if AI enhancement is enabled for a specific page"""
        if not self.gemini_enabled:
            return False
        return self._config.get('ai_enhancements', {}).get(page, False)
    
    @property
    def highlight_ai_content(self) -> bool:
        """Check if AI content should be highlighted"""
        return self._config.get('ai_display', {}).get('highlight_ai_content', True)
    
    @property
    def ai_indicator_color(self) -> str:
        """Get AI content indicator color"""
        return self._config.get('ai_display', {}).get('indicator_color', '#9b59b6')
    
    @property
    def show_ai_disclaimer(self) -> bool:
        """Check if AI disclaimer should be shown"""
        return self._config.get('ai_display', {}).get('show_disclaimer', True)
    
    @property
    def cache_enabled(self) -> bool:
        """Check if caching is enabled"""
        return self._config.get('cache', {}).get('enabled', True)
    
    @property
    def cache_duration_hours(self) -> int:
        """Get cache duration in hours"""
        return self._config.get('cache', {}).get('duration_hours', 24)


# Singleton instance
config = Config()

