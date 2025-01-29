# Comprehensive Temperature Converter

A simple package that converts temperature between Celsius, Fahrenheit and Kelvin.

## Installation

Clone the repository and navigate into the directory

```bash
$ git clone <url>
$ cd comprehensive_temperature_converter
$ pip install -e .
```

## Usage

Import the conversion functions

```python
from comprehensive_temperature_converter.converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit

print(celsius_to_fahrenheit(25))
print(fahrenheit_to_celsius(77))
print(celsius_to_kelvin(25))
print(kelvin_to_celsius(298.15))
print(fahrenheit_to_kelvin(77))
print(kelvin_to_fahrenheit(298.15))

```

## Run Unit Test

To run tests, navigate to the tests directory and run:

```bash
$ python -m unittest test_converter.py
```
