#!/usr/bin/python3

#Write a function that raises a type exception.
def raise_ex():
    raise TypeError

if __name__ == "__main__":
    try:
        raise_ex()
    except TypeError as te:
        print("Exception raised")

#--output--
#Exception raised
