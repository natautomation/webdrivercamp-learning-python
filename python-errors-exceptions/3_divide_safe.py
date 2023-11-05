#!/usr/bin/python3

#function devides 2 integers and prints result
#print value of devision or none.

def divide_safe(a, b):
    res = None

    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print(f"Result: {res}")
    return res

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    
    b=0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

#--output--
#Result: 3.0
#9 / 3 = 3.0
#Result: None
#9 / 0 = None
