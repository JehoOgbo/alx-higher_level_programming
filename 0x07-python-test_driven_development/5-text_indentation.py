#!/usr/bin/python3

def text_indentation(text):
    """prints na text with two new lines after each ., ? and : character
    Args:
        text: the string which is to be printed anew
    raise a typeError if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while i < length:
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{:s}\n".format(text[i]))
            i += 1
        else:
            print("{:s}".format(text[i]), end='')
        i += 1
