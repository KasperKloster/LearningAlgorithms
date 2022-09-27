from Sorting.bubbleSort import bubbleSort

class Main:
  def __init__(self):
    dataset : list[int] = [3, 7, 6, 1, 9, 8, 5, 0, 2, 4, 28, -1]    
    
    # User input
    userInput = input('Which algoritm do you want to see?: \n 1: Bubble Sort \n')
    if(userInput == '1'):    
      self.startBubbleSort(dataset)

  def startBubbleSort(self, dataset:list):    
    print('Unsorted list:\n' + str(dataset) + '\n')
    bubbleSort(unsorted_list = dataset)
    print('\nSorted list:\n' + str(dataset))
    
    

if __name__ == "__main__":
  Main()
