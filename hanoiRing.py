import numpy as np
import random
class MyClass:
    def __init__(self):
        z = self.checkIt(3)
        if z:
            print("\n")

        rows = 10
        cols = 6
        two_d_array = np.zeros((rows, cols))
        
        towerWithRing = [ 4, 5, 3, 2, 0, 0, 0, 0]
        
        tower = random.choice(towerWithRing)
        
        #print(len(two_d_array))
        
        items = [1, 2, 3, 4, 5]

        # Remove and return the last item
        #removed_item = items.pop()

       # print("Removed item:", removed_item)
       
        if( items.pop() < 4):
       
         print("Updated list:", items)

        
        #print(two_d_array[5])
        

    def checkIt(self, x):
        if x == 1:
            return 1
        elif x == 2:
            return -1
        elif x == 3:
            return 0.1

# Create an instance of MyClass
my_instance = MyClass()
