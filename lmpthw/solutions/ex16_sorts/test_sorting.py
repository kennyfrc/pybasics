import sorting_kenn
from dllist import DoubleLinkedList
from random import randint

max_numbers = 5

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(0, max_numbers):
        numbers.shift(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value: 
            return False
        else:
            node = node.next

    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)

    sorting_kenn.bubble_sort(numbers)

    assert is_sorted(numbers)


def test_merge_sort():
    numbers = random_list(max_numbers * 31) 

    sorting_kenn.merge_sort(numbers)

    assert is_sorted(numbers)

def xtest_quick_sort():
    numbers = random_list(max_numbers)

    sorting_kenn.quick_sort(numbers, 0, numbers.count() - 1)

    assert is_sorted(numbers)
