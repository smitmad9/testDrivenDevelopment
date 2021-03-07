import unittest
import leapYear

class testLeapYear (unittest.TestCase):

    # Test that all years divisible by 4 are leap years
    def testLeapYear(self):
        self.assertEqual(leapYear.leapYear(2000), True)
        self.assertEqual(leapYear.leapYear(2020), True)
        self.assertEqual(leapYear.leapYear(2001), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
