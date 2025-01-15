def find_all_list_indices(lst, item):
    indices = []

    def recursive_search(sub_lst, parent_indices):
        for i, x in enumerate(sub_lst):
            current_indices = parent_indices + [i]
            if x == item:
                indices.append(current_indices)
            elif isinstance(x, list):
                recursive_search(x, current_indices)

    recursive_search(lst, [])
    return indices

# Example usage:
nested_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# print(find_all_list_indices(nested_list, 2))
# print(find_all_list_indices(nested_list, 3))
# print(find_all_list_indices(nested_list, 8))
# print(find_all_list_indices(nested_list, 10))
print(find_all_list_indices(nested_list, [1, 2, 3]))