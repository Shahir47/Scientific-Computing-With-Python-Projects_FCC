class Category:
  name = ""
  total = 0
  ledger = []

  def __init__(self, n):
    self.name = n
    self.ledger = []

  def __str__(self):
    x = 30 - len(self.name)
    st = ""
    for i in range(int(x/2)): st = st + "*"
    st = st + self.name
    for i in range(int(x/2)): st = st + "*"
    if x%2 != 0: st = st + "*"
    st = st + "\n"
    
    for item in self.ledger:
      am = format(item["amount"], ".2f")
      de = item["description"]

      if len(de) > 23 : de = de[:23]
      space = 30 - len(de) - len(am)
      st = st + de
      for i in range(space): st = st + " "
      st = st + am
      st = st + "\n"

    st = st + f"Total: {self.total:.2f}"
    return st
      

  def deposit(self, a, d=""):
    x = {
      "amount" : a,
      "description" : d
    }
    self.ledger.append(x)
    self.total = self.total + a

  def withdraw(self, a, d=""):
    if self.check_funds(a) == True:
      x = {
        "amount" : a * -1,
        "description" : d
      }
      self.ledger.append(x)
      self.total = self.total - a
      return True
    return False

  def get_balance(self):
    return self.total

  def transfer(self, a, d):
    if self.check_funds(a) == True:
      self.withdraw(a, f"Transfer to {d.name}")
      d.deposit(a, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, a):
    if a > self.total: return False
    else: return True


def create_spend_chart(categories):
  st = "Percentage spent by category\n"

  total_w = 0
  cat_w = []
  cat_name = []
  bars = []
  
  for ct in categories:
    x = 0
    cat_name.append(ct.name[0].upper()+ct.name[1:])
    for item in ct.ledger:
      if item["amount"] < 0:
        x = x + (item["amount"] * -1)
    cat_w.append(x)
    total_w = total_w + x
  
  #percent calculation
  for i in range(len(cat_w)):
    cat_w[i] = int((cat_w[i] / total_w) * 100)
  #bar calculation
  for i in range(len(cat_w)):
    bars.append(int(cat_w[i] / 10))

  #printing upper portion
  for i in range(100, -1, -10):
    if(i/10!=0 and i/10<10): st = st + " "
    if(i/10 == 0): st = st + "  "
    st = st + str(i) + "| "
    for j in range(len(bars)):
      if bars[j] == i/10:
        st = st + "o  "
        bars[j] = bars[j] - 1
      else: st = st + "   "

    st = st + "\n"

  st = st + "    "
  for i in range(3*len(bars)+1):
    st = st + "-"

  st = st + "\n"
  
  #printing lower portion
  max = 0
  for name in cat_name:
    if len(name) > max: max = len(name)

  for i in range(max):
    st = st + "     "
    for j in range(len(cat_name)):
      if cat_name[j] != "":
        st = st + cat_name[j][0] + "  "
        cat_name[j] = cat_name[j][1:]
      else: st = st + "   "
    if i != max-1: st = st + "\n"

  return st



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))