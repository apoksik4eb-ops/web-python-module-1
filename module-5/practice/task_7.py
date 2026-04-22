my_list = [3, 1, 4, -2, 8, 5, 7, -6, -9]

def sort_list(my_list):
    average = sum(my_list) / len(my_list)
    n = len(my_list)
    
    if average > 0:
        sort_size = (2 * n) // 3
        print(f"Среднее значение = {average} > 0 - сортируем две трети списка:")
    else:
        sort_size = n // 3
        print(f"Среднее значение = {average} < 0 - Сортируем первую треть списка:")
    
    sorted_part = sorted(my_list[:sort_size])
    reversed_part = sorted(my_list[sort_size:][::-1])

    return sorted_part + reversed_part

print(sort_list(my_list))