#!/usr/bin/python3
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    elif num % 5 == 0:
        return ("Buzz")
    elif num % 3 == 0:
        return ("Fizz")
    else:
        return num


for i in range(1, 101):
    print(fizzbuzz(i), "", end="")
