

def fb():

    result = ""
    toAdd = ""
    i = 1

    while i <= 100:

        if i % 3 == 0:
            toAdd = "Fizz"

        else:
            toAdd = str(i)

        result += toAdd

        if i != 100:
            result += " "

        i += 1

    print(result)
    return result

fb()