from math import sqrt, acos

class Vector2:
  ORDER = 2
  
  def __init__(self, x, y):
    self.__coords = (x if x != None else 0, y if y != None else 0)
    self.__iter = 0
    
  def __iter__(self):
    yield self.__coords[0]
    yield self.__coords[1]
    
  def add(self, thing, y):
    if isinstance(thing, Vector2):
      self.x += thing.x
      self.y += thing.y
    else:
      self.x += thing
      self.y += y if y != None else thing
      
    return self
  
  def subtract(self, thing, y):
    if isinstance(thing, Vector2):
      self.x -= thing.x
      self.y -= thing.y
    else:
      self.x -= thing
      self.y -= y if y != None else thing
      
    return self
  
  def multiply(self, thing, y):
    if isinstance(thing, Vector2):
      self.x *= thing.x
      self.y *= thing.y
    else:
      self.x *= thing
      self.y *= y if y != None else thing
      
    return self
  
  def divide(self, thing, y):
    if isinstance(thing, Vector2):
      self.x /= thing.x
      self.y /= thing.y
    else:
      self.x /= thing
      self.y /= y if y != None else thing
      
    return self
  
  def negate(self):
    self.multiply(-1)
    
    return self
  
  def angle_to(self, v):
    return acos((self.dot(v) / self.magnitude) * v.magnitude)
  
  def dot(self, v):
    return self.x * v.x + self.y * v.y
  
  # cross
  
  # determinant
  
  @property
  def min(self):
    return self.x if self.x < self.y else self.y
      
  @property
  def max(self):
    return self.x if self.x > self.y else self.y
  
  def normalize(self):
    self.divide(self.magnitude)
    
    return self
  
  def equals(self, v):
    return v.x == self.x and v.y == self.y

  def to_string(self):
    return f"Vector2 ({self.x}, {self.y})"
      
  def __print__(self):
    return self.to_string()
    
  def clone(self):
    return Vector2(self.x, self.y)
  
  def to_tuple(self): # screw you python with your fancy tuples
    return (self.x, self.y)
  
  def to_point(self):
    return {
      "x": self.x,
      "y": self.y,
    }
  
  # transform
  
  @property
  def magnitude(self):
    return sqrt(self.x * self.x + self.y * self.y)
  
  @property
  def length(self):
    return self.magnitude
  
  @property
  def x(self):
    return self.__coords[0]
  
  @x.setter
  def x(self, value):
    self.__coords[0] = value
    return value
  
  @property
  def y(self):
    return self.__coords[1]
  
  @y.setter
  def y(self, value):
    self.__coords[1] = value
    return value
  
  # i knew it ! python sucks i cant make a property whose name is a number :(
  
  @staticmethod # uh... how to static getters ???
  def up():
    return Vector2(0, 1)
  
  @staticmethod
  def down():
    return Vector2(0, -1)
  
  @staticmethod
  def left():
    return Vector2(-1, 0)
  
  @staticmethod
  def right():
    return Vector2(1, 0)
  
  @staticmethod
  def add(a, b):
    return a.clone().add(b.clone())
  
  @staticmethod
  def subtract(a, b):
    return a.clone().subtract(b.clone())
  
  @staticmethod
  def multiply(a, b):
    return a.clone().multiply(b.clone())
  
  @staticmethod
  def divide(a, b):
    return a.clone().divide(b.clone())
  
  @staticmethod
  def negate(v):
    return v.clone().negate()
  
  @staticmethod
  def angle_to(a, b):
    return a.clone().angle_to(b.clone())
  
  @staticmethod
  def normalize(v):
    return v.clone().normalize()
  
  @staticmethod
  def lerp(a, b, t):
    if t < 0 or t > 1:
      raise IndexError
      
    def lerp(a, b, t):
      return (1 - t) * a + t * b;
    
    return Vector2(lerp(a.x, b.x, t), lerp(a.y, b.y, t))
  
  @staticmethod
  def is_vector2(thing):
    return isinstance(thing, Vector2)
    
