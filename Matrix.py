class Matrix:
  def __init__(self, width, height, contents):
    if width < 0 or height < 0:
      raise ValueError # only type of error i know lol
      
    self.width = width
    self.height = height
    
    self.contents = contents if contents != None else [[0] * width] * height
    
  def add(self, factor):
    if Matrix.is_matrix(factor):
      if factor.width != self.width or factor.height != self.height
        raise ValueError
      
      result = [[0] * width] * height
      
      for y in range(len(height))
        for x in range(len(width))
          result[y][x] = self.contents[y][x] + factor[y][x]
          
      self.contents = result
    else:
      result = [[0] * width] * height
      
      for y in range(len(height))
        for x in range(len(width))
          result[y][x] = self.contents[y][x] + factor
          
      self.contents = result
    
    return self
    
  def subtract(self, factor):
    if Matrix.is_matrix(factor):
      if factor.width != self.width or factor.height != self.height
        raise ValueError
      
      result = [[0] * width] * height
      
      for y in range(len(height))
        for x in range(len(width))
          result[y][x] = self.contents[y][x] - factor[y][x]
          
      self.contents = result
    else:
      result = [[0] * width] * height
      
      for y in range(len(height))
        for x in range(len(width))
          result[y][x] = self.contents[y][x] - factor
          
      self.contents = result
    
    return self
  
  def negate(self):
    self.multiply(-1)
    
    return self
  
  def determinant(self):
    if self.width != self.height:
      return float("nan")
    
    if self.width == 1:
      return self.contents[0][0]
    
    if self.height == 1:
      return self.contents[0][0] * self.contents[1][1] - self.contents[0][1] * self.contents[1][0]
    
    result = 0
    
    for x in range(len(width)):
      sub =  [row[:x] + row[x + 1:] for row in (m[:0] + m[1:])]
      
      result += (-1) ** (x + 2) * self.contents[0][x] * Matrix.from_array(sub).determinant()
    
    return result
  
  # cont'd
    
  @staticmethod
  def is_matrix(v):
    return isinstance(v, Matrix)
   
