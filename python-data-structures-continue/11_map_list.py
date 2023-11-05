#!/usr/bin/python3

# function returns list with all values multiplied by number
# no loops


def map_list(list_=[], num=0):
    return list(map(lambda x: x * num, list_))


if __name__ == "__main__":
    list_ = [5, 4, 3, 2, 1, 7]
    new_list = map_list(list_, 4)

    print(f"Original: {list_}")
    print(f"Modified: {new_list}")

#--output--
#Original: [5, 4, 3, 2, 1, 7]
#Modified: [20, 16, 12, 8, 4, 28]
