import os

#1
def t1():
  a = [1,2,3]   # C++ int a[3] = { 1,2,3 };
  b = a         # C++ int *b = a;
  b[0] = 33     # C++ *b = 33;
  try:
    print(a) #[33, 2, 3]  
    print(b) #[33, 2, 3]
    '''
    C++
    cout << "[";
	  for (int i = 0; i < 3; i++)
	  {
	  	if (i != 2)
	  		cout <<  a[i] << ",";
	  	else
	  		cout << a[i] << "]";
	  }
	  cout << endl;
	  cout << "[";
	  for (int i = 0; i < 3; i++)
	  {
	  	if (i != 2)
	  		cout << *b++ << ",";
	  	else
	  		cout << *b << "]";
	  }
    '''
  except IOError:
    print("fail")

#2 данная конструкция интерполирует значение с 0 до 10 и вставляет в массив 
def t2():
  # range() std lib of python
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

class Child1(Parent): # C++ class C1 : public P
  pass

class Child2(Parent):     # C++ class C2 : public P
  def set_a(self, value): # self in C++ this?
    self.a = value + 10

if __name__ == '__main__':
  #t1()
  #t2()
  #t3()
  #4
  child1 = Child1()               # C++ Child1 child1 = new Child1(...);
  child1.set_a(5)                 # C++ child1->set_a(5);
  child2 = Child2()               # C++ Child2 child2 = new Child2(...);
  child2.set_a(child1.get_a())    # C++ child1->get_a(child1->get_a());
  print(child2.get_a()) # 15      # C++ std::cout << child2->get_a() << std::endl;