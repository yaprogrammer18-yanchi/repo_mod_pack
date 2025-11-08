from hypothesis import given, strategies as st
from src.sorting_algorithms import quick_sort


def test_empty_array():
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == []


def test_single_element():
    arr = [42]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [42]


def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


def test_array_with_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_all_same_elements():
    arr = [7, 7, 7, 7]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [7, 7, 7, 7]


def test_negative_numbers():
    arr = [-3, -1, -4, -1, -5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [-5, -4, -3, -1, -1]


def test_mixed_positive_negative():
    arr = [3, -1, 4, -1, 0, -5, 9]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [-5, -1, -1, 0, 3, 4, 9]


def test_two_elements():
    arr = [2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2]


@given(st.lists(st.integers(), min_size=0, max_size=100))
def test_random_arrays(arr):
    original = arr.copy()
    quick_sort(arr, 0, len(arr) - 1)

    # Проверяем, что результат совпадает с sorted()
    assert arr == sorted(original)
    # Проверяем, что длина не изменилась
    assert len(arr) == len(original)


@given(
    st.lists(st.integers(), min_size=1, max_size=50),
    st.integers(min_value=0, max_value=100),
    st.integers(min_value=0, max_value=100)
)
def test_edge_cases_with_indices(arr, low_offset, high_offset):
    # Добавляем смещения, чтобы проверить граничные условия индексов
    n = len(arr)
    if n == 0:
        return

    low = max(0, min(low_offset, n - 1))
    high = max(low, min(high_offset, n - 1))

    original_slice = arr[low:high + 1]
    quick_sort(arr, low, high)
    sorted_slice = sorted(original_slice)

    # Сравниваем только отсортированный фрагмент
    assert arr[low:high + 1] == sorted_slice
