import unittest
from comprehensive_temperature_converter.converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
class TestConverter(unittest.TestCase):
    def test_converter(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(25.5), 77.9, places=2)
        
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(77.9), 25.5, places=2)

        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(100), 373.15)
        self.assertAlmostEqual(celsius_to_kelvin(25.5), 298.65, places=2)

        self.assertEqual(kelvin_to_celsius(273.15), 0)
        self.assertEqual(kelvin_to_celsius(373.15), 100)
        self.assertAlmostEqual(kelvin_to_celsius(298.65), 25.5, places=2)

        self.assertEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertEqual(fahrenheit_to_kelvin(212), 373.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(77.9), 298.65, places=2)

        self.assertEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertEqual(kelvin_to_fahrenheit(373.15), 212)
        self.assertAlmostEqual(kelvin_to_fahrenheit(298.65), 77.9, places=2)

if __name__ == '__main__':
    unittest.main()
