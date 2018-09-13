"""
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: A string and the market identifier code.
"""

def best_stock(data):
    """ (dict of str: float) -> str

    Preconditions: All the key values are unique.

    Return the key in data with the highest value.

    >>> stocks = {'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}
    >>> best_stock(stocks)
    'ATX'
    >>> stocks = {'CAC': 91.1, 'ATX': 1.01, 'TASI': 120.9}
    >>> best_stock(stocks)
    'TASI'
    """
    
    reversed_dict = [(value, key) for key, value in data.items()]
    reversed_dict.sort(reverse=True)
    
    return reversed_dict[0][1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()