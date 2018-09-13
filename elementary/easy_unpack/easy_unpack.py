"""
Your mission here is to create a function that gets an tuple and returns
a tuple with 3 elements - first, third and second to the last for the given array.

Input: A tuple, at least 3 elements long.

Output: A tuple.
"""

def easy_unpack(elements):
    """ (tuple of int) -> tuple of int
    
    Pre-condition: len(elements) >= 3

    Returns a tuple with 3 elements - first, third and second
    to the last of elements.
    
    >>> easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
    (1, 3, 7)
    >>> easy_unpack((1, 1, 1, 1))
    (1, 1, 1)
    >>> easy_unpack((6, 3, 7))
    (6, 7, 3)
    """
    
    return (elements[0],) + (elements[2],) + (elements[-2],)


if __name__ == '__main__':
    import doctest
    doctest.testmod()