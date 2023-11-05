def dict_v_delete(a_dictionary, value):

    #initialise array key

    list_ = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            list_.append(i)
    for i in list_:
        del a_dictionary[i]
    return a_dictionary


if __name__ == "__main__":
    dict_print = __import__('6_dict_print').dict_print

    dict_ = {
            "libs": (1, 2, 3),
            "x": "Selenium",
            "lang": ["Java"],
            "frame": "Selenium"
            }
    new_dict = dict_v_delete(dict_, "Selenium")

    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)

    new_dict = dict_v_delete(dict_, 'y')
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)

#---output---
#....Updated Dict....
#lang: ['Java']
#libs: (1, 2, 3)
#....Updated Dict....
#lang: ['Java']
#libs: (1, 2, 3)
