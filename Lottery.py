import random

class Lottery:
    def __init__(self):
        self.balls = list(range(1, 50))
        self.picked_balls = []

    def pick_balls(self):
        self.picked_balls = random.sample(self.balls, 10)
        print("Picked balls are: " + str(self.picked_balls))

    def sort_picked_balls(self):
        return sorted(self.picked_balls)

lot = Lottery()
lot.pick_balls()
print("Sorted balls are : " + str(lot.sort_picked_balls()))

### Unit tests
# Test 1 = Check if the output of the function is a list
#
# Test 2 = Check if each elements in the list are between 1 and 50
#
# Test 3 = Check if the list is correctly sorted by running a loop starting with 
#          the first element and check if the element on the right of each element is higher
###


