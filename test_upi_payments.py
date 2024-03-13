import unittest
from unittest.mock import patch
from upi_payments import get_balance

class TestUPIPayments(unittest.TestCase):
    @patch('requests.get')
    def test_get_balance(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'balance': '1000.00',
        }
        balance = get_balance('test@upi')
        self.assertEqual(balance, '1000.00')

if __name__ == '__main__':
    unittest.main()