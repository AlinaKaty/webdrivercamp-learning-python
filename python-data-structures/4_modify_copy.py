#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

copied_list = list(list_)

def replace_element(lst, idx, element):
    if idx >= 0 and idx < len(lst):
        lst[idx] = element

replace_element(copied_list, index, element_to_replace)

print("Modified copy:", copied_list)
print("Original list:", list_)
