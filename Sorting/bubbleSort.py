"""
Bubble Sort:
The goal is to sort our dataset from lowest to highest number (ascending order)

For each iteration we will compare the first value with the second. 
Is the first value higher or lower than the second value? If the first is higher, switch places.
Then compare the new second value with the third value. Is it higher or lower? If higher switch places, if not, do nothing move on and compare the third and forth.
We will do that until we reach the end.
Now we will do it again and again and again until the list is fully sorted. This is called recursion - We are repeating the same step, until it's done.

"""

def bubbleSort(unsorted_list : list[int]):
  # Iterate through range in the unsorted list
  for _ in range(len(unsorted_list)):
    # We are going through the length of the list minus 1, because we can't go further, after the last element.
    # Otherwise we will get "IndexError: list index out of range"
    for j in range(0, len(unsorted_list) - 1):            
      # If current element is greater than next. Swap
      if unsorted_list[j] > unsorted_list[j + 1]:
        # Swap the two elements
        unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
      
    # Prints the sorting, so we can see the process
    print(unsorted_list)