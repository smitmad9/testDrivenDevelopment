import unittest
import leapYear

class testLeapYear (unittest.TestCase):

    # Test that all years divisible by 4 are leap years
    #def testLeapYearByFour(self):
    #    self.assertEqual(leapYear.leapYear(2000), True)
    #    self.assertEqual(leapYear.leapYear(2020), True)
    #    self.assertEqual(leapYear.leapYear(2001), False)

    # Test that all years divisible by 4 and not by 100 are leap years
    def testLeapYearByFourAndHundred(self):
        self.assertEqual(leapYear.leapYear(2000), False)
        self.assertEqual(leapYear.leapYear(2020), True)
        self.assertEqual(leapYear.leapYear(2001), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
