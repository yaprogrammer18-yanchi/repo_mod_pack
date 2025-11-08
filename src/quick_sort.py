# arr - массив для сортировки
# low - индекс начала подмассива
# high - индекс конца подмассива

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = separation(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# за опорный берем последний из массива
def separation(arr, low, high):
    base_el = arr[high]
    ind_to_put = low - 1

    for j in range(low, high):
        if arr[j] <= base_el:
            ind_to_put += 1
            arr[ind_to_put], arr[j] = arr[j], arr[ind_to_put]
    arr[ind_to_put+1], arr[high] = arr[high], arr[ind_to_put + 1]
    return ind_to_put + 1
