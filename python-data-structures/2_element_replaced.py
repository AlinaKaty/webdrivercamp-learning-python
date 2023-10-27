#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def replace_element(lst, idx, element):
    if idx >= 0 and idx < len(lst):
        lst[idx] = element
        print(lst)
    else:
        print(lst)

replace_element(list_, index, element_to_replace)
