#Definition: Aquiring all the attributes/variables and behaviour/methods from
# from one class to another class to another class is called inheritance
# class A ---->a,b,c   m1() m2()
# class B(A) ---->x,y,z   m3()
# here A is parent of class B and
# B is child of class A
# some people call parent as base class or super class
# simillarly some people call child as sub-class or derived class
# objectives of inheritence
# 1.code re-usalibility
# 2.avoid duplication
# types of  inheritance
# 1.single  #one parent class and on child class
# 2.multi-level  #one parent class and multiple child classess
# 3.Heirarchy #One parent class and two child independent classess
# 4.multiple #one child class two independent parent classess
# #Example 1:
# # class A:
# #     def m1(self):
# #         print('This is m1 method from class A')
# #
# # class B(A):
# #         def m2(self):
# #             print("This is m2 method from class B")
# #
# # obj=B()
# # obj.m1()
# # obj.m2()
# # Example 2: Single inheritance
# # class A:
# #     x,y=10,20
# #     def m1(self):
# #         print(self.x+self.y)
# # class B(A):
# #     a,b=200,100
# #     def m2(self):
# #         print(self.a-self.b)
# # bobj=B()
# # bobj.m2()
# # bobj.m1()
# # Exmaple 3:Multi-level inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# bobj=B()
# bobj.m2()
# bobj.m1()
# class C(B):
#     i,j=2,3
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()   #30
# cobj.m2()   #100
# cobj.m3()   #6
# Example 4:Hierarchy inheritance
# class A:
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     i,j=200,100
#     def m2(self):
#         print(self.i-self.j)
# class C(A):
#     x,y=2,3
#     def m3(self):
#         print(self.x*self.y)
# aobj=A()
# aobj.m1()
# aobj.m2()
# Example 5: Multiple hierarchy
# class A:
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)
# class B:
#     i,j=200,100
#     def m2(self):
#         print(self.i-self.j)
# class C(A,B):
#     x,y=2,3
#     def m3(self):
#         print(self.x*self.y)
# cobj=C()
# cobj.m3()
# cobj.m2()
# cobj.m1()
# Example 6: Calling parent class method using child class by using super() function
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("This is m2 method from class B")
#         super().m1()
#
# bobj=B()
# bobj.m1()
# Example 7:
# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)    #70
#         print(self.i+self.j)   #300
#         print(self.a+self.b)   #30
# bobj=B()
# bobj.m(30,40)
# # Example 8:Over riding variables
# class parent:
#     def m1(self,name):
#         print(name)
# class child(parent):
#     name='scott'
#
# c=child()
# print(c.name)
# c.m1("David")
# Example 9: over riding methods
# class Bank:
#     def rateOfInterest(self):
#         return 0
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
# objy=YBank()
# print(objy.rateOfInterest())
# print(obj.rateOfInterest())
#Polymorphism :Def: one thing can have many forms
#Ex: shape -->circle,rectangle,square
# polymorphism we can implement using over riding concept
# Example 10: overloading (polymorphism 1)
# class human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print(name)
#         else:
#             print("hello")
# obj=human()
# obj.sayhello("Scott")
# obj.sayhello()
# # example 2:Overloading 2:(Polymorphism)
# class calculation:
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=calculation()
# obj.add(a=1,b=2,c=3)          #6
# obj.add(10,20,30)  #60
# obj.add(100,200,300)   #600




