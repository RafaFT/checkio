"""
Let's work with numbers.

You are given an array of numbers (floats). You should find the difference 
between the maximum and minimum element. Your function should be able to 
handle an undefined amount of arguments. For an empty argument list, 
the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary)
fractions. So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).
"""

def checkio(*args):
    """ (list of numbers) -> number

    Precondition: 0 ≤ len(args)
    all(-100 < x < 100 for x in args)
    all(isinstance(x, (int, float)) for x in args)

    Return the 

    >>> checkio(1, 2, 3)
    2
    >>> checkio(5, -5)
    10
    >>> checkio(10.2, -2.2, 0, 1.1, 0.5)
    12.399999999999999
    >>> checkio()
    0
    """

    return max(args, default=0) - min(args, default=0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()