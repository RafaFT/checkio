"""
For the input of your function will be given one sentence. 
You have to return its fixed copy in a way so it’s always 
starts with a capital letter and ends with a dot.

Pay attention to the fact that not all of the fixes is necessary. 
If a sentence already ends with a dot then adding another one will be a mistake.

Input: A string.

Output: A string.
"""

def correct_sentence(text):
    """ (str) -> str

    Return text with the first word capitalized and a '.' at the end, if necessary.

    >>> correct_sentence('greetings, friends')
    'Greetings, friends.'
    >>> correct_sentence('Greetings, friends')
    'Greetings, friends.'
    >>> correct_sentence('hi')
    'Hi.'
    >>> correct_sentence('')
    ''
    """

    return text[0].upper() + text[1:] + '.' * (not text[-1].endswith('.')) if text else ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()