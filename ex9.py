from abc import ABC,abstractmethod
class M(ABC):
 @abstractmethod
 def s(self,m:str,se:'U'):pass
class U(ABC):
 def __init__(self,n:str,m:M):self.n=n;self.m=m
 @abstractmethod
 def s(self,m:str):pass
 @abstractmethod
 def r(self,m:str):pass
class AM(M):
 def __init__(self):self.b=[];self.h=0;self.hb=None
 def a(self,b):self.b.append(b)
 def s(self,m,se):
  try:
   ba=int(m)
   if ba>self.h:
    self.h=ba;self.hb=se
    for b in self.b:
     if b!=se:b.r(f"${ba} by {se.n}")
   else:se.r(f"Bid ${ba} too low (current ${self.h})")
  except:pass
class B(U):
 def s(self,m):self.m.s(m,self)
 def r(self,m):print(f"{self.n}: {m}")
if __name__=="__main__":
 am=AM()
 b1=B("John",am);b2=B("Sarah",am);b3=B("Mike",am)
 for b in[b1,b2,b3]:am.a(b)
 b1.s("100");b2.s("200");b3.s("150");b2.s("300")