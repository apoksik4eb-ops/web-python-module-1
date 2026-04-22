def flat(nested_arr):
    new_list = []
    for item in nested_arr:
        for j in item:
            new_list.append(j)
    return new_list

print(flat([[1,2,3], [4,5], [6]]))