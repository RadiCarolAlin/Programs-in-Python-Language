"""
    Creating two sets of numbers (lists).
    Function for sorting items in the list.
    Function for the intersection of two sets.
    Function for the reunion of two sets.
"""
class Nod:
    def __init__(self,nr):
        self.nr=nr
        self.link=None
    def setarelink(self,element):
        self.link=element
    def __repr__(self):
        return "("+str(self.nr)+")"
    def clona(self):
        return Nod(self.nr)
    def __gt__(self,element):
        if element==None:
            return False
        if self.nr>element.nr:
            return True
        else:
            return False
    def __eq__(self,t):
     if t!=None:
       if self.nr==t.nr:
        return True
       else:
        return False
     else:
        return False

class Lista:
    def __init__(self):
        self.root=None
    def adaugare(self,element):
        if element!=None:
            if self.root==None:
                self.root=element
            else:
                element.link=self.root
                self.root=element
    def __repr__(self):
        s=" "
        i=self.root
        while i!=None:
            s=s+str(i)+" "
            i=i.link
        return s
    def Listasortare(self):
        esteSortat=False
        while esteSortat==False:
            esteSortat=True
            x=self.root
            while x.link!=None:
                if(x>x.link):
                    x.nr,x.link.nr=x.link.nr,x.nr
                    esteSortat=False
                x=x.link
    def reuniune(self,lista):
        self.Listasortare()
        lista.Listasortare()
        l=Lista()
        x=self.root
        y=lista.root
        while x!=None and y!=None:
            if x<y:
                l.adaugare(x.clona())
                x=x.link
            elif y<x:
                l.adaugare(y.clona())
                y=y.link
            else:
                l.adaugare(x.clona())
                x = x.link
                y = y.link
        while x!=None:
            l.adaugare(x.clona())
            x = x.link
        while y != None:
            l.adaugare(y.clona())
            y = y.link
        return l
    def intersectie(self,lista):
        self.Listasortare()
        lista.Listasortare()
        l=Lista()
        x = self.root
        y = lista.root
        while x!=None and y!=None:
            if x<y:
                x=x.link
            elif y<x:
                y=y.link
            else:
                l.adaugare(x.clona())
                x=x.link
                y=y.link
        return l

e1=Nod(1)
e2=Nod(2)
e3=Nod(5)
e4=Nod(9)
e5=Nod(4)
e6=Nod(10)
a1=Nod(2)
a2=Nod(4)
a3=Nod(6)
a4=Nod(8)
a5=Nod(10)
l1=Lista()
l2=Lista()
l1.adaugare(e1)
l1.adaugare(e2)
l1.adaugare(e3)
l1.adaugare(e4)
l1.adaugare(e5)
l1.adaugare(e6)
l2.adaugare(a1)
l2.adaugare(a2)
l2.adaugare(a3)
l2.adaugare(a4)
l2.adaugare(a5)
print(l1)
print(l2)
l1.Listasortare()
#print(l1)
print(l1.reuniune(l2))
print(l1.intersectie(l2))

