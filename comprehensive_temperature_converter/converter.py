from comprehensive_temperature_converter.logger import log_conversion

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    This is a function that converts temperature from celsius scale to fahrenheit scale
    example: 
        >> celsius_to_fahrenheit(0)
        >> 32
    """
    fahr = (celsius * 9/5) + 32
    log_conversion(celsius, "C", fahr, "F")
    return fahr

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    This is a function that converts temperature from fahrenheit scale to celsius scale
    example: 
        >> fahrenheit_to_celsius(32)
        >> 0
    """
    cels = (fahrenheit - 32) * 5/9
    return cels

def celsius_to_kelvin(celsius: float) -> float:
    """
    This is a function that converts temperature from celsius scale to kelvin scale
    example:
        >> celsius_to_kelvin(10)
        >> 283.15
    """
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin: float) -> float:
    """
    This is a function that converts temperature from kelvin scale to celsius scale
    example:
        >> kelvin_to_celsius(300)
        >> 26.85
    """
    kelvin = kelvin - 273.15
    return kelvin

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    This is a function that converts temperature from fahrenheit scale to kelvin scale
    example:
        >> fahrenheit_to_kelvin(32)
        >> 273.15
    """
    fahr =  (fahrenheit - 32) * 5/9 + 273.15
    return fahr

def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    This is a function that converts temperature from kelvin scale to fahrenheit scale
    example:
        >> kelvin_to_fahrenheit(300)
        >> 80.33
    """
    fahr = (kelvin - 273.15) * 9/5 + 32
    return fahr


