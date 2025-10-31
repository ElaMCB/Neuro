"""
Neuro Programming Language
Making AI development accessible through intent-driven programming
"""

__version__ = "0.1.0"
__author__ = "Neuro Community"

from .parser import NeuroIntentParser, parse_intent, Intent
from .compiler import NeuroCompiler, compile_intent

__all__ = [
    "NeuroIntentParser", "parse_intent", "Intent",
    "NeuroCompiler", "compile_intent"
]
