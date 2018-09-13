"""
You are given an array of integers. You should find the sum of the elements 
with even indexes (0th, 2nd, 4th...) then multiply this summed number and 
the final element of the array together. Don't forget that the first 
element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.
"""

def checkio(array):
    """ (list of int) -> int

    Precondition: 
    all(isinstance(x, int) for x in array)
    all(-100 < x < 100 for x in array)

    Return the sum of even-indexed elements in array multiplyied by the last item.

    >>> checkio([0, 1, 2, 3, 4, 5])
    30
    >>> checkio([1, 3, 5])
    30
    >>> checkio([6])
    36
    >>> checkio([])
    0
    """

    #my original solution was this one
    #return sum([array[i] for i in range(len(array)) if i % 2 == 0]) * sum(array[-1:])

    # but this one is simply awesome!
    return sum(array[0::2]) * array[-1] if array else 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()