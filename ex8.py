from abc import ABC,abstractmethod
from typing import Any
class I(ABC):
 @abstractmethod
 def h(self)->bool:pass
 @abstractmethod
 def n(self)->Any:pass
class B:
 def __init__(self):self.b=[]
 def a(self,b):self.b.append(b)
 def f(self):return F(self)
 def r(self):return R(self)
class F(I):
 def __init__(self,c):self.c=c;self.i=0
 def h(self)->bool:return self.i<len(self.c.b)
 def n(self)->Any:
  if self.h():b=self.c.b[self.i];self.i+=1;return b
  return None
class R(I):
 def __init__(self,c):self.c=c;self.i=len(self.c.b)-1
 def h(self)->bool:return self.i>=0
 def n(self)->Any:
  if self.h():b=self.c.b[self.i];self.i-=1;return b
  return None
if __name__=="__main__":
 print("=== Book Collection Example ===")
 l=B()
 l.a("Python Programming");l.a("Data Structures");l.a("Algorithms");l.a("Machine Learning");l.a("Database Systems")
 print("\nForward Traversal:")
 i=l.f()
 while i.h():print(i.n())
 print("\nReverse Traversal:")
 i=l.r()
 while i.h():print(i.n())
 print("\n=== Multiple Simultaneous Iterators ===")
 print("\nTwo independent forward iterators:")
 i1=l.f();i2=l.f()
 print("Iterator 1 first two books:")
 print(i1.n());print(i1.n())
 print("\nIterator 2 all books:")
 while i2.h():print(i2.n())