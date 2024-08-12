class Касса:
  def __init__(self):
      self.сумма = 0

  def top_up(self, X):
      self.сумма += X

  def count_1000(self):
      return self.сумма // 1000

  def take_away(self, X):
      if X > self.сумма:
          raise ValueError("Недостаточно денег в кассе")
      self.сумма -= X


class Черепашка:
  def __init__(self, x=0, y=0, s=1):
      self.x = x
      self.y = y
      self.s = s

  def go_up(self):
      self.y += self.s

  def go_down(self):
      self.y -= self.s

  def go_left(self):
      self.x -= self.s

  def go_right(self):
      self.x += self.s

  def evolve(self):
      self.s += 1

  def degrade(self):
      if self.s <= 1:
          raise ValueError("Количество клеточек не может стать ≤ 0")
      self.s -= 1

  def count_moves(self, x2, y2):
      dx = abs(x2 - self.x)
      dy = abs(y2 - self.y)
      return (dx + self.s - 1) // self.s + (dy + self.s - 1) // self.s
