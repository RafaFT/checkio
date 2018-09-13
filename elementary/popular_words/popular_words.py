"""
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words 
the popularity of which you need to determine.

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word 
"one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 
(zero) value.
Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number 
of times when those words are occurring in a given text.
"""

def popular_words(text, words):
    """ (str, list of str) -> dict of str: int

    Precondition:
    The text will consist of English letters in uppercase and lowercase and whitespaces.

    Return a dict of str: int, where each key is a word from words and each value is
    the number of occurrences of word in text (case is ignored.)

    >>> s = ('When I was One I had just begun When I was Two I was nearly new')
    >>> popular_words(s, ['i', 'was', 'three', 'near'])
    {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    """
    
    return {word: text.lower().split().count(word) for word in words}


if __name__ == '__main__':
    import doctest
    doctest.testmod()