"""
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces 
(one space). The words contains only letters. You should check if the string 
contains three words in succession. For example, the string "start 5 one two three 7 end" 
contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.
"""

import re

def checkio(words):
    """ (str) -> bool

    Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
    0 < len(words)

    Return True if words contains at least three words in a row, or False otherwise.

    >>> checkio("Hello World hello")
    True
    >>> checkio("He is 123 man")
    False
    >>> checkio("1 2 3 4")
    False
    >>> checkio("bla bla bla bla")
    True
    """

    # solution without re
    """
    consecutive_word = 0
    for word in words.split():
        consecutive_word = consecutive_word + 1 if word.isalpha() else 0
        if consecutive_word >= 3: 
            return True
    return False
    """
    
    # this seems better
    return bool(re.search(r'[a-z]+\s[a-z]+\s[a-z]+', words, flags=re.I))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
