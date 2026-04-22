list_1 = [11,21,14,45,52,68,52,85,99,17]
list_2 = [2,14,68,21,85,52,14,85,46,3]
print(f"{list_1 + list_2}")
print(f"{list(dict.fromkeys(list_1 + list_2))}")
print(f"{list(filter(lambda x: x in list_2, list_1))}")
print(f"{list((set(list_1) - set(list_2)) | (set(list_2) - set(list_1)))}")
print(f"{min(list_1), max(list_1), min(list_2), max(list_2)}")