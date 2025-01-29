import argparse
from comprehensive_temperature_converter.converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit
)
from comprehensive_temperature_converter.logger import log_conversion

def convert_temperature(temp_value: float, input_unit: str, output_unit: str):
    """Convert temperature based on the input and output units."""
    
    conversions_obj = {
        ("C", "F"): celsius_to_fahrenheit,
        ("F", "C"): fahrenheit_to_celsius,
        ("C", "K"): celsius_to_kelvin,
        ("K", "C"): kelvin_to_celsius,
        ("F", "K"): fahrenheit_to_kelvin,
        ("K", "F"): kelvin_to_fahrenheit
    }

    if input_unit == output_unit:
        result = temp_value
    elif (input_unit, output_unit) in conversions_obj:
        result = conversions_obj[(input_unit, output_unit)](temp_value)
    else:
        print("\nInvalid temperature units provided. Use C, F, or K.")
        return

    print(f"\n => {temp_value:.2f}°{input_unit} is {result:.2f}°{output_unit}")

    log_conversion(temp_value, input_unit, result, output_unit)

def main():
    """Parse command-line arguments and call convert_temperature."""
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius, Fahrenheit, and Kelvin."
    )
    parser.add_argument(
        "temp_value", type=float, help="Temperature value to convert"
    )
    parser.add_argument(
        "input_unit", choices=["C", "F", "K"], help="Input temperature unit (C, F, K)"
    )
    parser.add_argument(
        "output_unit", choices=["C", "F", "K"], help="Output temperature unit (C, F, K)"
    )

    args = parser.parse_args()
    convert_temperature(args.temp_value, args.input_unit.upper(), args.output_unit.upper())

if __name__ == "__main__":
    main()
