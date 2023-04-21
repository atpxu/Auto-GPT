"""
This module contains the configuration classes for AutoGPT.
"""
from autogpt.config.ai_config import AIConfig
from autogpt.config.config import Config, check_openai_api_key
from autogpt.config.singleton import AbstractSingleton, Singleton
from autogpt.config import lang_cn, lang_en

__all__ = [
    "check_openai_api_key",
    "AbstractSingleton",
    "AIConfig",
    "Config",
    "Singleton",
]
