def find_all_list_indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

print(find_all_list_indices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # [4]
print(find_all_list_indices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))  # [9]
print(find_all_list_indices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))  # [0]
print(find_all_list_indices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))  # []
print(find_all_list_indices([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))  # []
