from hypothesis import given
import hypothesis.strategies as st
from src.bubble_sort import bubble_sort

def test_bubble_sort_usual_occasions():
    assert bubble_sort([29, 32, 54, 11, 9]) == [9, 11, 29, 32, 54]
    assert bubble_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_one_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_reverse_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_sorted_input():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_double_pairs():
    assert bubble_sort([5, 3, 4, 4, 3, 5]) == [3, 3, 4, 4, 5, 5]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_bubble_sort_negative_with_positive():
    assert bubble_sort([-1, 2, -3, 4, -5]) == [-5, -3, -1, 2, 4]

def test_bubble_sort_one_number_list():
    assert bubble_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_bubble_sort_very_big_reversed_array():
    assert bubble_sort(list(range(1000, 0, -1))) == list(range(1, 1001))

@given(st.lists(st.integers()))
def test_bubble_any_array_whether_it_is_sorted(arr):
    result = bubble_sort(arr)
    assert result == sorted(arr)

@given(st.lists(st.integers()))
def test_bubble_if_all_elements_are_there(arr):
    sorted_arr = bubble_sort(arr)
    assert all(x in sorted_arr for x in arr)

@given(st.lists(st.integers()))
def test_bubble_len(arr):
    assert len(arr) == len(bubble_sort(arr))

@given(st.lists(st.integers()))
def test_bubble_ascending_order(arr):
    result = bubble_sort(arr)
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))
