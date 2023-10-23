#!/usr/bin/python3
def print_replaced_element(lic, ind, el):
    lic_original = lic.copy()

    if ind < 0 or ind >= len(lic):
        print(lic_original)
    else:
        lic[ind] = el
        print(f'Copy:     {lic}')
        print(f'Original: {lic_original}')
