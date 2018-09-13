"""
You are given a string and two markers (the initial and final). You have 
to find a substring enclosed between these two markers. But there are a 
few important conditions:

The initial and final markers are always different.
If there is no initial marker then the beginning should be considered as the beginning of a string.
If there is no final marker then the ending should be considered as the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker is standing in front of the initial one then return an empty string.

Input: Three arguments. All of them are strings. The second and third arguments 
are the initial and final markers.

Output: A string.
"""

def between_markers(text, begin, end):
    """ (str, str, str) -> str

    Returns the substring of text between two given markers (begin and end).
    If begin isn't found, and end is, returns text[:end],
    if begin is found and end isn't, return [begin:],
    if begin and end are not found, return the whole text and finally,
    if begin index > end index, return empty string.

    >>> between_markers('What is >apple<', '>', '<')
    'apple'
    >>> between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    'My new site'
    >>> between_markers('No[/b] hi', '[b]', '[/b]')
    'No'
    >>> between_markers('No [b]hi', '[b]', '[/b]')
    'hi'
    >>> between_markers('No hi', '[b]', '[/b]')
    'No hi'
    >>> between_markers('No <hi>', '>', '<')
    ''
    """

    index_begin = text.find(begin) + len(begin) if begin in text else None
    index_end = text.find(end) if end in text else None
    
    return text[index_begin: index_end]


if __name__ == '__main__':
    import doctest
    doctest.testmod()