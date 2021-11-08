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
    
    for x in range(len(self.width)):
      sub = [row[:x] + row[x + 1:] for row in (m[:0] + m[1:])]
      
      result += (-1) ** (x + 2) * self.contents[0][x] * Matrix.from_list(sub).determinant()
    
    return result
  
  @property
  def minors(self):
    minors = Matrix(self.width, self.height)
    
    for y in range(len(self.height)):
      for x in range(len(self.width)):
        minors.set(x, y, Matrix.from_list([row[:x] + row[x + 1:] for row in (m[:y] + m[y + 1:])]).determinant())
        
    return minors
  
  @property
  def cofactors(self):
    checkerboard = [[1] * width] * height
    
    for y in range(len(self.height)):
      for x in range(len(self.width)): 
        if (x + y) % 2 != 0:
          checkerboard[y][x] = -1
          
    minors = self.minors
    
    cofactors = [[0] * width] * height
    
    for y in range(len(self.height)):
      for x in range(len(self.width)): 
        cofactors[y][x] = minors[y][x] * checkerboard[y][x]
    
    return cofactors
  
  @property
  def adjugate(self):
    return self.cofactors.transpose()
  
  @property
  def inverse(self):
    determinant = self.determinant()
    
    if determinant == 0:
      raise ValueError
      
    adjugate = this.adjugate
    
    return Matrix.from_list(list(map(lambda row: list(map(lambda x: (1 / determinant) * x, row)), self.contents)))
  
  def to_list(self):
    return self.contents
  
  def __str__(self):
    pass
  
  def clone(self):
    return Matrix(self.width, self.height, self.contents)
  
  def rotate(self, dir):
    if dir < 0:
      l = list(zip(*self.contents[::-1]))
      self.contents = [list(r) for r in l]
    elif dir > 0:
      l = list(zip(*self.contents))[::-1]
      self.contents = [list(r) for r in l]
    
    return self
  
  def transpose(self):
    self.reverse()
    
    self.rotate(1)
    
    return this
  
  @staticmethod
  def rotate(m):
    return m.clone().rotate()
  
  @staticmethod
  def zeroes(self, width, height):
    return Matrix(width, height, [[0] * width] * height)
  
  @staticmethod
  def ones(self, width, height):
    return Matrix(width, height, [[1] * width] * height)
  
  @staticmethod
  def identity(s):
    identity = Matrix.zeroes(s, s)
    
    for y in range(s):
      for x in range(s):
        if x == y:
          identity[y][x] = 1
          
    return identity
  
  @staticmethod
  def from_list(a):
    return Matrix(a.length, a[0].length, a)
   
  # 
    
  @staticmethod
  def is_matrix(v):
    return isinstance(v, Matrix)
   
