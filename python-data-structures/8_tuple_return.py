#!/usr/bin/python3
def tuple_return(li):
    res_list = []
    list_length = len(li)
    res_list.append(list_length)

    if list_length > 0:
        first_item = li[0]
    else:
        first_item = None
        res_list.append(first_item)
        res_tuple = tuple(res_list)
    return res_tuple
