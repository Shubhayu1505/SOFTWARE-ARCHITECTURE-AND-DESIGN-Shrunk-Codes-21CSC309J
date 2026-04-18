from abc import ABC,abstractmethod
class D(ABC):
 @abstractmethod
 def e(self,q:str)->str:pass
class R(D):
 def __init__(self,n:str):
  self.n=n
  print(f"Connecting to {self.n} database...")
  self.l()
 def l(self):print(f"Loading data from {self.n}...")
 def e(self,q:str)->str:print(f"Executing query on {self.n}: {q}");return f"Results for: {q}"
class P(D):
 def __init__(self,n:str):
  self.n=n
  self._r=None
  self.a="admin"
 def e(self,q:str)->str:
  if not self._r:self._r=R(self.n)
  if self.c():r=self._r.e(q);self.l(q);return r
  return "Access Denied: Insufficient permissions"
 def c(self)->bool:return self.a=="admin"
 def l(self,q:str):print(f"Log: Query executed - {q}")
class CP(D):
 def __init__(self,n:str):
  self.n=n
  self._r=None
  self.c={}
 def e(self,q:str)->str:
  if q in self.c:print(f"Returning cached results for: {q}");return self.c[q]
  if not self._r:self._r=R(self.n)
  r=self._r.e(q);self.c[q]=r;return r
if __name__=="__main__":
 print("=== Regular Database Access ===");r=R("ProductionDB");print(r.e("SELECT * FROM users"))
 print("\n=== Proxy with Access Control ===");p=P("SecureDB");print(p.e("SELECT * FROM employees"))
 print("\n=== Proxy with Caching ===");cp=CP("ProductDB");print(cp.e("SELECT * FROM products"));print(cp.e("SELECT * FROM products"));print(cp.e("SELECT * FROM orders"));print(cp.e("SELECT * FROM products"))
 print("\n=== Testing Access Control ===");p.a="user";print(p.e("DELETE FROM users"))
