from abc import ABC,abstractmethod
class N(ABC):
 @abstractmethod
 def n(self,m:str)->None:pass
class E(N):
 def n(self,m:str)->None:print(f"Email Notification Sent: {m}")
class S(N):
 def n(self,m:str)->None:print(f"SMS Notification Sent: {m}")
class P(N):
 def n(self,m:str)->None:print(f"Push Notification Sent: {m}")
class F:
 @staticmethod
 def g(t:str)->N:
  if t.lower()=="email":return E()
  if t.lower()=="sms":return S()
  if t.lower()=="push":return P()
  raise ValueError(f"Unknown: {t}")
if __name__=="__main__":
 try:
  F.g("email").n("Welcome to our platform!")
  F.g("sms").n("Your OTP is 1234.")
  F.g("push").n("You have a new message.")
 except ValueError as e:print(e)
