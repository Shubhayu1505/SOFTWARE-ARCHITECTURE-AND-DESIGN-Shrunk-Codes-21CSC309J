import threading
from typing import Any, Dict, Optional
class SMC(type):
 _i:Dict[type,Any]={}
 _l:threading.Lock=threading.Lock()
 def __call__(cls,*a,**k):
  with cls._l:
   if cls not in cls._i:
    cls._i[cls]=super().__call__(*a,**k)
  return cls._i[cls]
class S(metaclass=SMC):
 _d=False
 def __init__(self):
  if not self._d:
   self.d="Singleton Data"
   self.__class__._d=True
 def __repr__(self)->str:return f"<{self.__class__.__name__} at {hex(id(self))}>"
 def s(self)->None:print(f"Data: {self.d}")
 def a(self,nd:str)->None:self.d+=f", {nd}"
def sng(cls):
 i={}
 l=threading.Lock()
 def gi(*a,**k):
  with l:
   if cls not in i:i[cls]=cls(*a,**k)
  return i[cls]
 return gi
@sng
class C:
 def __init__(self):
  self.c={"theme":"dark","language":"en","version":"1.0.0"}
 def __repr__(self)->str:return f"<C at {hex(id(self))}>"
 def g(self,k:str)->Optional[Any]:return self.c.get(k)
 def s(self,k:str,v:Any)->None:self.c[k]=v
 def r(self,k:str)->bool:
  if k in self.c:del self.c[k];return True
  return False
 def a(self)->None:
  for k,v in self.c.items():print(f"  {k}: {v}")
class D(metaclass=SMC):
 _x=False
 def __init__(self,cs:str="default://localhost:5432"):
  if not self._x:
   self.cs=cs
   self.c=[]
   self.m=10
   self._x=True
 def g(self):return f"C from {self.cs}"
 def ca(self):self.c.clear()
if __name__=="__main__":
 s1=S()
 s1.s()
 s1.a("Additional Info")
 s2=S()
 s2.s()
 s2.a("More Data")
 print(f"\nSame? {s1 is s2}")
 s1.s()
 c1=C()
 c1.s("language","fr")
 c1.s("timeout",30)
 c1.a()
 c2=C()
 print(f"\nlang: {c2.g('language')}")
 print(f"Same? {c1 is c2}")
 c1.r("timeout")
 c1.a()
 isl=[S() for _ in range(3)]
 print(f"\nAll same? {all(isl[0] is i for i in isl)}")
 db1=D("postgresql://localhost:5432/mydb")
 db2=D()
 print(f"Same? {db1 is db2}")
 def ct(n:str):
  s=S()
  print(f"[{n}] id: {id(s)}")
 ts=[]
 for i in range(5):
  t=threading.Thread(target=ct,args=(f"T-{i}",))
  ts.append(t);t.start()
 for t in ts:t.join()