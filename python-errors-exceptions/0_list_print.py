#!/usr/bin/python3

#function prints x-elements of a list
#try/except use

def list_print(lst=[], i=0):
    print_count = 0
    for index in range(0, i):
        try:
            print(lst[index], end="")
            print_count += 1
        except IndexError:
            break
    print()
    return print_count

if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")

#output
#1234
#Count: 4
#1234567
#Count: 7
#1234567
#Count: 7
