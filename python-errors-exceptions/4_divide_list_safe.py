#!/usr/bin/python3
#working with exceptions and try/exept/finally

def is_num(value):
    return True if type(value) is int or type(value) is float else False

def divide_list_safe(list_1, list_2, list_len):
    res = []
    for i in range(0, list_len):
        resDiv = 0
        try:
            delimoe= list_1[i]
            delitele= list_2[i]

            if is_num(delimoe) and is_num(delitele):
                resDiv = delimoe / delitele

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        finally:
            res.append(resDiv)
    return res

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)

#--output--

#[3.0, 1.0, 3.0]
#__________

#wrong type
#division by 0
#out of range
#[0, 0, 6.0, 5.0, 0]
