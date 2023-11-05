#!/usr/bin/python3

#function returns numbers of keys in dictionary.

def keys_number(d):
    return len(d.keys())


if __name__ == "__main__":
    dict_ = {
            "lib": "requests",
            1: "Selenium",
            "lang": "Python",
            "frame": "Behave"
            }
    number_of_keys = keys_number(dict_)
    print(f"The dictionary has {number_of_keys} keys")

#--output---
#The dictionary has 4 keys
