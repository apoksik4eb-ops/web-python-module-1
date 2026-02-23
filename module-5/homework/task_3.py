def bubble_sort(arr):
    n = len(arr)
    print(f"Начальный список чисел: {arr}")

    for i in range(n - 1):
        swapped = 0
        print(f"\nПроход {i + 1}:")

        for j in range(n - 1 - i):
            print(f"  Сравниваем элемент {arr[j]} и {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped += 1
                print(f"Перестановка {arr}")

        if swapped == 0:
            print(f"Сортировка завершена на проходе {i + 1}: перестановок не было.")
            break
        else:
            print(f"Проход {i + 1}: выполнено {swapped} перестановок")

    return arr
result = bubble_sort([1,2,-3,4,5])
print(f"Резудьтат: {result}")