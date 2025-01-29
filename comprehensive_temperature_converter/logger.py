import logging

logging.basicConfig(
    filename="temperature_conversion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_conversion(initial_scale: float, initial_unit: str, converted_scale: float, converted_unit: str):
    """
    This is a logger function that logs the temperature conversion details for each conversion.
    """
    message = f"Converted {initial_scale}°{initial_unit} to {converted_scale:.2f}°{converted_unit}"
    logging.info(message)
