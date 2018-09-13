"""
Do you remember the radix and Numeral systems from math class? 
Let's practice with it.

You are given a positive number as a string along with the radix 
for it. Your function should convert it into decimal form. The 
radix is less than 37 and greater than 1. The task uses digits 
and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted. 
For example: "1A" cannot be converted with radix 9. For 
these cases your function should return -1.
"""

def checkio(str_number, radix):
    """ (str, int) -> int

    Precondition: 
    re.match(r"\A[A-Z0-9]\Z", str_number)
    0 < len(str_number) ≤ 10
    2 ≤ radix ≤ 36

    Return the decimal equivalent o str_number of radix numerical system.
    If str_number is invalid for it's radix, return -1 instead.

    >>> checkio('AF', 16)
    175
    >>> checkio('101', 2)
    5
    >>> checkio('101', 5)
    26
    >>> checkio('Z', 36)
    35
    >>> checkio('AB', 10)
    -1
    """

    try:
        return int(str_number, radix)
    except ValueError:
        return -1

    # this was my original answer =P
    """import string

    symbols = '0123456789' + string.ascii_uppercase
    symbols_map  = {symbols[index]: index for index in range(len(symbols))}

    decimal = 0
    position = 0
    for symbol in str_number[::-1]:
        if symbol not in symbols[:radix]:
            return -1
        decimal += symbols_map[symbol] * (radix ** position)   
        position += 1
    
    return decimal"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
