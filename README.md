# neym

<p align="center">
  <img src="assets/logo.png" width="200" alt="neym logo">
</p>

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
import neym

name = neym.generate_turkish_name()
print(name)  # Generates a random Turkish name
```

### Generate a Random Last Name

```python
import neym

lastname = neym.generate_turkish_last_name()
print(lastname)  # Generates a random Turkish last name
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

## Author

Developed by Arif
