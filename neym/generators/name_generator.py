import random
from ..core.randomizer import names

isimler = list(names())


def generate_turkish_name():
    return random.choice(isimler)
