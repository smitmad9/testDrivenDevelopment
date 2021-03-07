
# Print all numbers 1-100 but replace multiples of 3 with "Fizz", multiples of
# 5 with "Buzz", and multiples of both with "Fizzbuzz"
def fb():

    result = ""
    toAdd = ""
    i = 1

    while i <= 100:

        # Replace multiples of 3 with Fizz
        if i % 3 == 0:
            toAdd = "Fizz"

        # Replace multiples of 5 with Buzz
        elif i % 5 == 0:
            toAdd = "Buzz"

        # If not a multiple of 3 or 5, just keep the number i
        else:
            toAdd = str(i)

        # Add the term to the result
        result += toAdd

        # Add a space between each term for easy readability
        if i != 100:
            result += " "

        # Go to the next term
        i += 1

    print(result)
    return result

fb()