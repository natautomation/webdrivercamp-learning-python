#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_var = sys.argv
    length = len(arg_var)-1
    if length == 1:
        msg = f'{length} argument:'
    elif length == 0:
        msg = f'{length} arguments.'
    else:
        msg = f'{length} arguments:'
    print(msg)
    i = 1
    while i <= length:
        print(f'{i}: {arg_var[i]}')
        i += 1
