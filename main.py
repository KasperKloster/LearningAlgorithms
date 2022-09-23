from Sorting.bubbleSort import bubbleSort

class Main:
  def __init__(self):
    dataset : list[int] = [3, 7, 6, 1, 9, 8, 5, 0, 2, 4, -1, 28]    
    bubbleSort(unsorted_list = dataset)
    print(dataset)
    

if __name__ == "__main__":
  Main()
