#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
if random_num < 0:
    status = "is negative"
elif random_num > 0:
    status = "is positive"
else:
    status = "is zero"
print(f"{random_num} {status}")
