#!/usr/bin/python3
def print_element_to_replace_all(lic, ind, elm):
    if ind < 0 or ind >= len(lic):
        print(lic)
    else:
        lic[ind] = elm
        print(lic)


list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
