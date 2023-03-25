import copy
import random
# Consider using the modules imported above.


class Hat:
  contents = []
  cont_copy = []

  def __init__(self, **balls):
    self.contents = []
    self.cont_copy = []

    for key, value in balls.items():
      for i in range(value):
        self.contents.append(key)
        self.cont_copy.append(key)

  def draw(self, n):
    if n > len(self.contents): return self.contents

    remove = []

    for i in range(n):
      x = random.choice(self.contents)
      remove.append(x)
      inx = self.contents.index(x)
      self.contents = self.contents[:inx] + self.contents[inx + 1:]

    return remove


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0

  for i in range(num_experiments):
    re = hat.draw(num_balls_drawn)
    flag = True
    for key, val in expected_balls.items():
      if re.count(key) < val:
        flag = False
        break

    if flag == True: count = count + 1
    hat.contents = copy.deepcopy(hat.cont_copy)

  return count / num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)