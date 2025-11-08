from hypothesis import given
from hypothesis import strategies as st
from src.merge_sort import merge_sort

def test_merge_sort_usual_occasions():
    assert merge_sort([29, 32, 54, 11, 9]) == [9, 11, 29, 32, 54]
    assert merge_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]

def test_merge_sort_empty_list():
    assert merge_sort([]) == []

def test_merge_sort_one_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_reverse_order():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_sorted_input():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_double_pairs():
    assert merge_sort([5, 3, 4, 4, 3, 5]) == [3, 3, 4, 4, 5, 5]

def test_merge_sort_negative_numbers():
    assert merge_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

def test_merge_sort_negative_with_positive():
    assert merge_sort([-1, 2, -3, 4])

@given(st.lists(st.integers()))
def test_bubble_any_array_whether_it_is_sorted(arr):
    result = merge_sort(arr)
    assert result == sorted(arr)

@given(st.lists(st.integers()))
def test_bubble_if_all_elements_are_there(arr):
    sorted_arr = merge_sort(arr)
    assert all(x in sorted_arr for x in arr)

@given(st.lists(st.integers()))
def test_bubble_len(arr):
    assert len(arr) == len(merge_sort(arr))

@given(st.lists(st.integers()))
def test_bubble_ascending_order(arr):
    result = merge_sort(arr)
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))