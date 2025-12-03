def heapify(array, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if (left < size) and (array[left] > array[largest]):
        largest = left
    if (right < size) and (array[right] > array[largest]):
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, size, largest)


def heap_sort(numbers):
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, -1, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)
    return numbers