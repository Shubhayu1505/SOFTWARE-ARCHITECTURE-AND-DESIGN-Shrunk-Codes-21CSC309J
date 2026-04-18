from abc import ABC,abstractmethod
class FSC(ABC):
 @abstractmethod
 def s(self,i:int=0)->None:pass
 @abstractmethod
 def g(self)->int:pass
class F(FSC):
 def __init__(self,n:str,sz:int):self.n=n;self._sz=sz
 def s(self,i:int=0)->None:print("  "*i+f"File: {self.n} ({self._sz} KB)")
 def g(self)->int:return self._sz
class D(FSC):
 def __init__(self,n:str):self.n=n;self.c=[]
 def a(self,comp):self.c.append(comp)
 def r(self,comp):self.c.remove(comp)
 def s(self,i:int=0)->None:print("  "*i+f"Directory: {self.n} ({self.g()} KB)");[x.s(i+1) for x in self.c]
 def g(self)->int:return sum(x.g() for x in self.c)
if __name__=="__main__":
 f1=F("resume.pdf",200);f2=F("photo.png",1500);f3=F("notes.txt",50);f4=F("report.doc",300);f5=F("movie.mp4",5000)
 r=D("MyComputer");d=D("Documents");p=D("Pictures");v=D("Videos")
 d.a(f1);d.a(f3);d.a(f4);p.a(f2);v.a(f5);r.a(d);r.a(p);r.a(v)
 print("File System Structure:\n----------------------")
 r.s()
 print(f"\nSize Information:\nFile 'resume.pdf': {f1.g()} KB\nDirectory 'Documents': {d.g()} KB\nTotal size: {r.g()} KB")
