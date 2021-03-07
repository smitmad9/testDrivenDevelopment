
# Given a year, return whether it was a leap year
def leapYear(n):

    # If the year is divisible by 4, it is a leap year
    if n % 4 == 0:

        # The year must also NOT be divisible by 100 OR divisible by 400
        # to be a leap year
        if n % 100 != 0 or n % 400 == 0:
            return True

    return False