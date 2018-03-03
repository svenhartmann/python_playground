"""
Unit test
"""
import unittest
import simplecalc

class TestSimplecalc(unittest.TestCase):
    """TestCase"""
    def test_add_int(self):
        """Add test"""
        result = simplecalc.add(8, 9)
        self.assertEqual(result, 17)
        self.assertNotEqual(result, 89)

    def test_sub_int(self):
        """Sub test"""
        result = simplecalc.sub(1, 1)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
