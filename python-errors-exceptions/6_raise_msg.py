#!/usr/bin/python3
#function raises a name exception with message

def raise_message(message = ''):
   raise NameError(message)


if __name__ == "__main__":
    try:
        raise_message("I love Python!")
    except NameError as ne:
        print(ne)

#---output---
#I love Python!
