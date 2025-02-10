import unittest
from converter import convert_currency

class TestCurrencyConverter(unittest.TestCase):

    def test_conversion_usd_to_eur(self):
        """Test de conversion de 10 USD en EUR (attendu : 9.20 EUR)"""
        self.assertEqual(convert_currency(10, "USD", "EUR"), 9.20)

if __name__ == "__main__":
    unittest.main()
