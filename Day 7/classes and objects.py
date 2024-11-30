# # Example 1:how to create a class
# class Myclass:
#     def myfunc(self):
#         pass
#     def display(self,name):
#         print(name)
# mc1=Myclass()
# mc1.myfunc()
# mc1.display("Ram")
# Example 2:Two types of methods we can define within the class
# 1.Instance method(we can call only through object)
# 2.Static method(we can directly call using class)
#        annotation @static method
# whenever you created a static method method the self also considered as one
# parameter but when you create an instance method self is not considered as a
# # parameter
# class Myclass:
#     def m1(self):
#         print("This is instance method......")
#     @staticmethod
#     def m2(self,name):
#         print(self,name)
# mc=Myclass()
# mc.m1()
# mc.m2(100,200)  #100 200
# Myclass().m2(100,200) #Here callig stacic method directly using class not through object
# note: whenever you self parameter that is representing class
# # Example 3: How to access class variables inside the method
# class Myclass:
#     a,b=10,20
#     def m1(self):
#         print(self.a+self.b)  #30
#     def m2(self):
#         # print(self.a*self.b)  #200
# mc=Myclass()
# mc.m1()
# mc.m2()
# Example 4: Combination of global,class,local variables
# a,b=10,20    #Global variables
# class Myclass:
#     i,j=2,3   #Class variables
#     def m1(self,x,y):
#         print(x+y)   # local variables    #50
#         print(self.i+self.j)              #5
#         print(a+b)                        #30
# mc=Myclass()
# mc.m1(20,30)
# Example 5: All variables names are same
# a,b=5,10
# class Myclass:
#     a,b=15,20
#     def add(self,a,b):
#         print(a+b)    #Local variables #55
#         print(self.a+self.b)  #class variables #35
#         print(globals()['a']+globals()['b'])   #global variables #15
# mc=Myclass()
# mc.add(25,30)
# Example 6: One class can have multiple objects
# class Myclass:
#     def display(self,name):
#         print("This is display method.......")
#         print(name)
# object1=Myclass()
# object2=Myclass()
# object1.display("John")
# object2.display("Scott")
#Method and constructor:
#method
#1.We can give any name to method
#2.Method can return the values
#3.Method can take arguments/parameters
#4.We have to use object to invoke the method

#Constructor:
#1.constructor name is fixed i.e __init__(self):
#2.Constructor will not return any values
#3.Constructor can also take arguments/parameters
#4.Constructor will be called at the time of object creation ifself
# Example 7 : Constructor example
# class Myclass:
#     def __init__(self):
#         print("This is constructor.......")
#     def m1(self,x,y):
#         print("Hellooooo constructor")
#         return (x+y)
# mc=Myclass()    #invoke constructor automatically
# print(mc.m1(100,200))
#Here we are calling the method explicitly bu using object
# class Myclass:
#     name="john"   #class variable
#     def __init__(self,name):   #constructor expecting one parameter
#         print(self.name)
#         print(name)
# obj=Myclass("Scott")   #passing parameter to the constructor
#Example 9: my requirement create on employe class
# constructor:eid,ename,sal
#display: print eid,print ename,print sal
# class Emp():
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#             print(self.eid,self.ename,self.sal)
# obj=Emp(101,"John",50000)
# obj.display()
# obj2=Emp(102,"scott",50000)
# obj2.display()
# obj3=Emp(103,"david",75000)
# obj3.display()
# we have one more constructor in python that is __str__ constructor it will not
# print anything it will just return the str value ,string constructor always return
# str type of data only.
# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def __str__(self):
#         return (self.eid,self.ename,self.sal)
# obj=Emp(101,"John","alekya")
# print(obj)
# print(obj)
# class Emp:
#     a="kavya"
#     def __str__(sel):
#
#         return(self.a)
#         return name
# obj=Emp()
# print(obj)




