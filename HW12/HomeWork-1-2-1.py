#!/usr/bin/python3.8

# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
temp_list = []

for num_list1 in my_list_1:
    if num_list1 not in my_list_2:
        temp_list.append(num_list1)
    
print(temp_list)