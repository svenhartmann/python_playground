"""
Test mocking in Python unit tests..
"""
import unittest
from unittest.mock import patch


class TestMockedSimplecalc(unittest.TestCase):
    """TestCase"""

    @patch('simplecalc.add', return_value=11)
    def test_add_int(self, add):
        """Add test mocked"""
        result = add(8, 9)
        self.assertEqual(result, 11)
        self.assertNotEqual(result, 89)


    @patch('simplecalc.sub', return_value=344)
    def test_sub_int(self, sub):
        """Sub test mocked"""
        result = sub(1, 34)
        self.assertEqual(result, 344)


if __name__ == '__main__':
    unittest.main()
