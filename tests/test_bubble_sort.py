from sorting.bubbleSort import bubbleSort

def test_bubble_sort() -> None:
  unsorted_list = [3, 7, 1]
  sorted_list = bubbleSort(unsorted_list)
  assert sorted_list == [1, 3, 7]