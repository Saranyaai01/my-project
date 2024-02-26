# class family():
#     def __init__(self) :
#         print("welcome to my family")
#     def family_members(self):
#         print("we are three members are there")
# class parent(family):
#     def __init__(self,mother,father):
#         super(). __init__()
#         self.m=mother
#         self.f=father
#         print("welcome")
#     def welcome(self):
#         print("my parents are Mr.",self.f,"and Mrs.",self.m)
       
# class child(parent):
#     def __init__(self,mother,father,son):
#         super(). __init__(mother,father)
#         self.s=son
#         print("Thank you")
#     def display(self):
#         print("I am",self.s,"son of",self.f,"and",self.m)



# x=child("saranya","narayanan","ruthraprasath")
# x.family_members()
# x.welcome()
# x.display()




class A:
    def __init__(self,txt):
        print(txt,"I am in A class")
class B(A):
    def  __init__(self, txt):
        print(txt,"I am in B class")
        super().__init__(txt)
class C(B):
    def __init__(self, txt):
        print(txt,"I am in C class")
        super().__init__(txt)
class D(C):
    def __init__(self, txt):
        print(txt,"I am in D class")
        super().__init__(txt)
class E(D,C):
    def __init__(self, txt):
        print(txt,"I am in E class")

        super().__init__(txt)
object=E("Hai")
print(" ")
obj=C("hello")






