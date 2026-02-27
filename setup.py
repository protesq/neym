from setuptools import setup, find_packages

setup(
    name="neym",
    version="0.1.4",
    description="A simple name generator library",
    author="Developed by Arif",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(),
    package_data={"neym.core": ["*.txt"]},
    include_package_data=True,
)
