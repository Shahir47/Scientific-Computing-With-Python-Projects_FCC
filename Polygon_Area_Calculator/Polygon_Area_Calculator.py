class Rectangle:
  width = 0
  height = 0
  def __init__(self, w, h):  
    self.width = w
    self.height = h

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
  
  def set_width(self, w):
    self.width = w
  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * (self.width + self.height)
  def get_diagonal(self):
    return (self.width**2 + self.height**2) **.5 

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
      
    st = ""
    for i in range(self.height):
      for j in range(self.width):
        st = st + "*"
      st = st + "\n"
    return st

  def get_amount_inside(self, obj):
    return int((self.width*self.height) / (obj.width*obj.height))

class Square(Rectangle):
  
  def __init__(self, s):
    self.width = self.height = s

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, s):
    self.width = self.height = s

  def set_width(self, s):
    self.width = self.height = s
  def set_height(self, s):
    self.width = self.height = s


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))