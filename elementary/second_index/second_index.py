"""
You are given two strings and you have to find an index of the 
second occurrence of the second string in the first one.

Let's go through the first example where you need to find the 
second occurrence of "s" in a word "sims". It’s easy to find 
its first occurrence with a function index or find which will 
point out that "s" is the first symbol in a word "sims" and 
therefore the index of the first occurrence is 0. But we have to 
find the second "s" which is 4th in a row and that means that the 
index of the second occurrence (and the answer to a question) is 3.

Input: Two strings.

Output: Int or None
"""

def second_index(text, symbol):
    """ (str, int) -> int or None
    
    Returns the second index of symbol in text. If symbol doesn't occur in
    text or it doesn't have at least two occurances, None is returned.

    >>> second_index("sims", "s")
    3
    >>> second_index("find the river", "e")
    12
    >>> second_index("hi", " ")
    >>> second_index("hi mayor", " ")
    >>> second_index("hi mr Mayor", " ")
    5
    """

    second_occurance = text.find(symbol, text.find(symbol) + 1)

    return second_occurance if second_occurance != -1 else None


if __name__ == '__main__':
    import doctest
    doctest.testmod()