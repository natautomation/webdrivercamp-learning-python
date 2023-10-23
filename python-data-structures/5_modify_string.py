#!/usr/bin/python3
string = """AbraCadabra
A new string voila!"""


def remove_char(some_string):
    res_str = ''

    for i in some_string:
        if i != 'a' and i != 'A':
            res_str += i
    return res_str
print(remove_char(string))
