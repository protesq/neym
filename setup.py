from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="neym",
    version="0.1.5",
    description="A simple Turkish name generator library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Developed by Arif",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(),
    package_data={"neym.core": ["*.txt"]},
    include_package_data=True,
)
