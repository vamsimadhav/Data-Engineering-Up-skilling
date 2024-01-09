def flatten_list(nested_list):
    flat_list = []

    for list_obj in nested_list:
        if isinstance(list_obj, list):
            for num in list_obj:
                flat_list.append(num)
        else:
            flat_list.append(list_obj)

    return flat_list


value = [[1, 2], [3, 4], [5, 6], 7, 9, [8, 10]]

print(flatten_list(value))
