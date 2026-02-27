import random

from ..core.randomizer import names, last_names

isimler = list(names())
soyisimler = list(last_names())


def generate_turkish_name():
    return random.choice(isimler)

def generate_turkish_last_name():
    return random.choice(soyisimler)
