#!/usr/bin/python3
if __name__ == "__main__":
    try:
        import sys
        arg_var = sys.argv
        length = len(arg_var)-1
        if length == 0:
            print('No arguments. Add some.')
        i = 1
        sum = 0
        while i <= length:
            sum += int(arg_var[i])
            i += 1
        print(sum)
    except ValueError:
        print('Use digits only')
