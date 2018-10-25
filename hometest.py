import os

def t1():
  #1
  a = [1,2,3]
  b = a
  b[0] = 33
  try:
    print(a) #[33, 2, 3]
    print(b) #[33, 2, 3]
  except IOError:
    print("fail")

def t2():
  #2 данная конструкция интерполирует значение с 0 до 10 и вставляет в массив 
  result = [x for x in range(10)]
  print(result) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def t3():
  a = [1,2,3]
  b = a           # a [1,2,3], b стала [1,2,3]
  b.append(a)     # b [1,2,3[...]]
  print(b)
  b[3].append(4)  # b [1,2,3,[...],4]
  print(b)        # [1,2,3,[...],4]

#4
class Parent:
  def __init__(self):
    self.a = 0
  def set_a(self, value):
    self.a = value

  def get_a(self):
    return self.a

class Child1(Parent):
  pass

class Child2(Parent):
  def set_a(self, value):
    self.a = value + 10

if __name__ == '__main__':
  #t1()
  #t2()
  #t3()
  #4
  child1 = Child1()
  child1.set_a(5)
  child2 = Child2()
  child2.set_a(child1.get_a())
  print(child2.get_a()) # 15