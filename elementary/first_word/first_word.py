"""
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.
"""

import re

def first_word(text):
    """ (str) -> str

    Returns the first word in a given text or empty string if
    there's no word in it.

    >>> first_word("Hello world")
    'Hello'
    >>> first_word(" a word ")
    'a'
    >>> first_word("don't touch it")
    "don't"
    >>> first_word("... and so on ...")
    'and'
    >>> first_word("Hello.World")
    'Hello'
    >>> first_word(".")
    ''
    """
    
    word = re.search(r"[a-zA-Z-']+", text)
    
    return word.group(0) if word else ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()