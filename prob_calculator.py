import copy
import random

class Hat:

  def __init__(self, **args):
    self.contents = []
    for key, value in args.items():
      for i in range(value):
        self.contents.append(key)   

  def draw(self, n):
    drawnAll = []
    if(n > len(self.contents)):
      return self.contents
    for i in range(n):
      drawn = self.contents.pop(random.choice(range(len(self.contents))))
      drawnAll.append(drawn)
    return drawnAll

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    expectedCopy = copy.deepcopy(expected_balls)
    hatCopy = copy.deepcopy(hat)
    drawn = hatCopy.draw(num_balls_drawn)
    for color in drawn:
      if(color in expectedCopy):
        expectedCopy[color]-=1
    if(all(x <= 0 for x in expectedCopy.values())):
      m += 1
  return m / num_experiments