import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, "Location('SLO', 35.3, -120.7)")

        loc = Location("Wow", 35.3, -120.7)
        self.assertEqual(loc, "Location('Wow', 35.3, -120.7)")

        loc = Location("WOW", 35.3, -120.7)
        self.assertEqual(loc, "Location('WOW', 35.3, -120.7)")

        loc = Location("Colorado", 35.5, -120.7)
        self.assertEqual(loc, "Location('Colorado', 35.5, -120.7)")
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
