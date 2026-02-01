import random
import sys
from pathlib import Path

# Try relative import first (when imported as module), then fallback to absolute
try:
    from ..core.randomizer import names, last_names
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from core.randomizer import names, last_names

isimler = list(names())
soyisimler = list(last_names())


def generate_turkish_name():
    return random.choice(isimler)

def generate_turkish_last_name():
    return random.choice(soyisimler)
