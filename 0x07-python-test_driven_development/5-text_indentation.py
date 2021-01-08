#!/usr/bin/python3
"""
print_square - print a square

"""


def text_indentation(text):
    """ function that print a square from size
    Args:
        text: (string): string to indent
    """
    signal = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delim = ['?', '.', ':']
    st = ""
    counter = 0
    for i in text:
        st += text[counter]
        for y in delim:
            if i == y:
                print(st.strip(), end="")
                st = ""
                print()
                print()
        counter += 1
    print(st.strip(), end="")
