# neym

A simple Turkish name generator library.

## Description

`neym` is a lightweight Python library that generates random Turkish names. It's perfect for testing, data generation, and any application that needs authentic Turkish names.

## Installation

Install from PyPI:

```bash
pip install neym
```

Or install from the local repository:

```bash
pip install .
```

## Usage

### Generate a Random Turkish Name

```python
from generators.name_generator import generate_turkish_name

name = generate_turkish_name()
print(name)  # Generates a random Turkish name
```

### Generate a Random Last Name

```python
from core.randomizer import random_lastname

lastname = random_lastname()
print(lastname)  # Generates a random Turkish last name
```

### Get All Available Names

```python
from core.randomizer import names

all_names = names()
print(len(all_names))  # Total number of names
print(all_names[:5])   # First 5 names
```

### Get All Available Last Names

```python
from core.randomizer import lastnames

all_lastnames = lastnames()
print(len(all_lastnames))  # Total number of last names
print(all_lastnames[:5])   # First 5 last names
```

## Features

- 📚 Comprehensive list of Turkish names and last names
- 🎲 Random name generation
- 👤 Random last name generation
- 🔧 Simple and easy-to-use API
- 🐍 Pure Python, no external dependencies

## Requirements

- Python >= 3.8

## Project Structure

```
neym/
├── core/
│   ├── __init__.py
│   ├── randomizer.py      # Core name and last name loading functionality
│   ├── names.txt          # Turkish names database
│   └── lastnames.txt      # Turkish last names database
├── generators/
│   ├── __init__.py
│   └── name_generator.py  # Random name and last name generation
├── pyproject.toml
└── README.md
```

## License

MIT

## Author

Developed by Arif
