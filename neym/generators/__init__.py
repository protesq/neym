"""Generators package for neym library."""
try:
    from .name_generator import generate_turkish_name,generate_turkish_last_name
except ImportError:
    from name_generator import generate_turkish_name,generate_turkish_last_name

__all__ = ["generate_turkish_name","generate_turkish_last_name"]
