from abc import ABC,abstractmethod
class C(ABC):
 @abstractmethod
 def c(self)->float:pass
 @abstractmethod
 def d(self)->str:pass
class B(C):
 def c(self)->float:return 5.0
 def d(self)->str:return "Basic Coffee"
class D(C):
 def __init__(self,c):self._c=c
 def c(self)->float:return self._c.c()
 def d(self)->str:return self._c.d()
class M(D):
 def c(self)->float:return self._c.c()+1.5
 def d(self)->str:return self._c.d()+", Milk"
class S(D):
 def c(self)->float:return self._c.c()+0.5
 def d(self)->str:return self._c.d()+", Sugar"
class Ch(D):
 def c(self)->float:return self._c.c()+2.0
 def d(self)->str:return self._c.d()+", Chocolate"
class Cr(D):
 def c(self)->float:return self._c.c()+1.0
 def d(self)->str:return self._c.d()+", Cream"
if __name__=="__main__":
 c1=B();print("Order 1: "+c1.d());print("Cost: ₹"+str(c1.c()))
 c2=M(S(B()));print("\nOrder 2: "+c2.d());print("Cost: ₹"+str(c2.c()))
 c3=Ch(M(S(B())));print("\nOrder 3: "+c3.d());print("Cost: ₹"+str(c3.c()))
 c4=Cr(Ch(M(B())));print("\nOrder 4: "+c4.d());print("Cost: ₹"+str(c4.c()))
 c5=S(S(M(B())));print("\nOrder 5: "+c5.d());print("Cost: ₹"+str(c5.c()))