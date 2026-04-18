from abc import ABC,abstractmethod
class B(ABC):
 @abstractmethod
 def c(self)->None:pass
 @abstractmethod
 def r(self)->None:pass
class C(ABC):
 @abstractmethod
 def c(self)->None:pass
 @abstractmethod
 def r(self)->None:pass
class WB(B):
 def c(self)->None:print("Windows Button clicked")
 def r(self)->None:print("Rendering Windows-style button")
class WC(C):
 def c(self)->None:print("Windows Checkbox checked")
 def r(self)->None:print("Rendering Windows-style checkbox")
class MB(B):
 def c(self)->None:print("Mac Button clicked")
 def r(self)->None:print("Rendering macOS-style button")
class MC(C):
 def c(self)->None:print("Mac Checkbox checked")
 def r(self)->None:print("Rendering macOS-style checkbox")
class GF:
 def cb(self)->B:...
 def cc(self)->C:...
class WF:
 def cb(self)->B:return WB()
 def cc(self)->C:return WC()
class MF:
 def cb(self)->B:return MB()
 def cc(self)->C:return MC()
class A:
 def __init__(self,f):
  self._f=f
  self._b=f.cb()
  self._c=f.cc()
 def cu(self)->None:
  self._b.r()
  self._c.r()
 def si(self)->None:
  self._b.c()
  self._c.c()
 @property
 def b(self)->B:return self._b
 @property
 def c(self)->C:return self._c
class UF:
 @staticmethod
 def gf(t:str)->GF:
  fs={"windows":WF,"mac":MF,"win":WF,"macos":MF}
  fc=fs.get(t.lower())
  if not fc:raise ValueError(f"Unsupported: {t}")
  return fc()
if __name__=="__main__":
 print("=== Windows UI Demo ===")
 wa=WF()
 aa=A(wa)
 aa.cu()
 aa.si()
 print("\n"+"="*30+"\n")
 print("=== Mac UI Demo ===")
 ma=MF()
 aa=A(ma)
 aa.cu()
 aa.si()
 print("\n"+"="*30+"\n")
 print("=== Dynamic Factory Selection Demo ===")
 try:
  f=UF.gf("windows")
  a=A(f)
  a.cu()
  a.si()
 except ValueError as e:print(f"Error: {e}")