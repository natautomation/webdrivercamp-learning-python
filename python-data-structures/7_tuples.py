#!/usr/bin/python3

#init
def tuple_addition(first_tuple=(0, 0), second_tuple=(0, 0)):
    
    first_list = list(first_tuple)
    second_list = list(second_tuple)
    res_list = []

    while len(first_list) < 2:
        first_list.append(0)
    while len(second_list) < 2:
        second_list.append(0)

    for i in range(0, 2):
        res_list.append(first_list[i] + second_list[i])
    result_tuple = tuple(res_list)
    return result_tuple
