"""
In this mission you should write a function that introduce a 
person with a given parameters in attributes.

Input: Two arguments. String and positive integer.

Output: String.
"""

def say_hi(name, age):
    """ (str, int) -> str
    
    Return a pre-defined greeting (capitalized) using name and age.

    >>> say_hi("Alex", 32)
    'Hi. My name is Alex and I'm 32 years old'
    >>> say_hi("frank", 68)
    'Hi. My name is Frank and I'm 68 years old'
    """
    
    return "Hi. My name is {} and I'm {} years old".format(name.capitalize(), age)


if __name__ == '__main__':
    import doctest
    doctest.testmod()