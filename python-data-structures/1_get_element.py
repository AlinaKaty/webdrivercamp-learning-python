#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2

def get_element(lst, idx):
    if idx < 0 or idx >= len(lst):
        return None
    return lst[idx]

element = get_element(list_, index)

if element is not None:
    print(f"The element retrieved is {element}")
