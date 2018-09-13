"""
You are given a positive integer. Your function should calculate the 
product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 
(don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.
"""

def checkio(number):
    """ (int) -> int

    Precondition: 0 < number

    Return the product of all digits in number, ignoring 0's digits.

    >>> checkio(123405)
    120
    >>> checkio(999)
    729
    >>> checkio(1000)
    1
    """

    return eval('*'.join(list(str(number).replace('0', ''))))


if __name__ == '__main__':
    import doctest
    doctest.testmod()