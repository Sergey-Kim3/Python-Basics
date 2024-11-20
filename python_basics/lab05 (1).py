def sine(x):
    """
    Calculates the sine of x using the Taylor series expansion.

    Args:
      x: The angle in radians.

    Returns:
      The sine of x.
    """
    i = 0
    n = 1
    exp = 1
    res = 0
    while i < 10:
        temp = res
        y = (2 * i + 1)
        for k in range(1, int(y) + 1):
            exp = exp * x
            n *= k
        if (i % 2 == 0):
            min = 1
        else:
            min = -1
        res = min * (exp / n)
        res += temp
        i += 1
        exp = 1
        n = 1
    print(res)

def collatz():
    """
    Generates the Collatz sequence for a given integer.
    """
    while(1):
        print("Please type a number greater than one\nor 'quit' to quit")

        try:
            x = input()
            if x == "quit" or x == "q":
                print("goodbye")
                break

            n = int(x)
            if n <= 1:
                print("Please enter an integer greater than 1.\n")
                continue

            i = 1
            print("Giving Collatz sequence for {}\n".format(x))
            print("iteration {} results in {}".format(i, x))
            i += 1

            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = n * 3 + 1
                print("iteration {} results in {}".format(i, n))
                i += 1

        except ValueError:
            print("it turns out that {} was not an integer.".format(x))

sine(30 * 3.1415926536 / 180)
collatz()