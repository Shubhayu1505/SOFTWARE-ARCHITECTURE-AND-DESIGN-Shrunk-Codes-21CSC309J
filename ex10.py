from abc import ABC,abstractmethod
class V(ABC):
 @abstractmethod
 def b(self,o):pass
 @abstractmethod
 def m(self,o):pass
 @abstractmethod
 def s(self,o):pass
class I(ABC):
 @abstractmethod
 def a(self,v):pass
class B(I):
 def __init__(self,n,p):self.n=n;self.p=p
 def a(self,v):return v.b(self)
class M(I):
 def __init__(self,n,p):self.n=n;self.p=p
 def a(self,v):return v.m(self)
class S(I):
 def __init__(self,n,p):self.n=n;self.p=p
 def a(self,v):return v.s(self)
class PV(V):
 def __init__(self):self.t=0
 def b(self,o):self.t+=o.p;return o.p
 def m(self,o):self.t+=o.p;return o.p
 def s(self,o):self.t+=o.p;return o.p
class TV(V):
 def b(self,o):return o.p*0.05
 def m(self,o):return o.p*0.18
 def s(self,o):return o.p*0.12
class DV(V):
 def b(self,o):return o.p*0.10
 def m(self,o):return o.p*0.15
 def s(self,o):return o.p*0.20
if __name__=="__main__":
 i=[B("Ramayana",500),M("Smartphone",15000),S("Silk Saree",3000),B("Mahabharata",600),M("Tablet",8000)]
 print("=== Shopping Cart ===")
 for x in i:print(f"{type(x).__name__}: {x.n} - Rs.{x.p}")
 pv=PV()
 for x in i:x.a(pv)
 tv=TV()
 tt=sum(x.a(tv) for x in i)
 dv=DV()
 td=sum(x.a(dv) for x in i)
 print(f"\nTotal Price: Rs.{pv.t}\nTotal Tax: Rs.{tt:.2f}\nTotal Discount: Rs.{td:.2f}\n\nFinal Amount: Rs.{pv.t+tt-td:.2f}")
