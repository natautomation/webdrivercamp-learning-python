#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
message = ""
if random_num < 0:
    message = "is negative"
elif random_num == 0:
    message = "is zero"
elif random_num > 0:
    message = "is positive"
print(random_num, message)
