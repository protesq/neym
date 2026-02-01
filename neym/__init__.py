"""Neym - Turkish name generator library."""
try:
    from .generators.name_generator import generate_turkish_name,generate_turkish_last_name
except ImportError:
    from generators.name_generator import generate_turkish_name,generate_turkish_last_name

__all__ = ["generate_turkish_name","generate_turkish_last_name"]