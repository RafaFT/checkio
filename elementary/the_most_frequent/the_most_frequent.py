"""
You have a sequence of strings, and you’d like to determine the 
most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.
"""

def most_frequent(data):
    """ (list of str) -> str

    Return the most frequently occurring string in data.

    >>> most_frequent(['a', 'b', 'c', 'a', 'b', 'a'])
    'a'
    >>> most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
    'bi'
    """
    
    return max(data, key=data.count)


if __name__ == '__main__':
    import doctest
    doctest.testmod()