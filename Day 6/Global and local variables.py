# # # global_var=10
# # # def myfunc():
# # #     local_var=20
# # #     print(global_var)  #10
# # #     print(local_var) #20
# # # myfunc()
# # # print(global_var)  #10
# # # print(local_var)
# # # Example 2:
# # # xy=100 #global variable
# # # def func():
# # #     xy=200    #local variable
# # #     print(xy)
# # # func()
# # # Example 3:Using global variable in local variable and update value
# # # xy=100
# # # def cool():
# # #     global xy
# # #     xy=200
# # #     print(xy)
# # # cool()
# # # print(xy) #200
# # # # Example 4:
# # # x=100
# # # def cool():
# # #     global x
# # #     x=500
# # #     print(x)
# # # cool()
# # # print(x)
# # # Example 5:
# # # def cool():
# # #     global x
# # #     x=100
# # #     print(x)
# # # cool()
# # # print(x)
# # # two types arguments/parameters we can pass to the function they are
# # # 1.positional arguments
# # # 2.keyword arguments
# # # Example 1:
# # # def my_func(x,y):
# # #     print(x,y)
# #
# # #my_func(10,20)    #positional arguments
# # # #my_func(x=10,y=20)  #keyword arguments
# # # # Example 2: Default values assigned to positional argumnets
# # # def my_func(i,j=10):
# # #     print(i,j)
# # # my_func(100)
# # # Example 3: keyword arguments
# # # def my_func(i,j):
# # #     print(i,j)
# # # my_func(i=10,j=20)  #Keyword arguments
# # # def greetings(name,greetingmsg):
# # #     print(greetingmsg+"  "+name)
# # # #greetings("jhon","hello")
# # # greetings(greetingmsg="hello",name="john")
# # # greetings(name="john",greetingmsg="hello")
# # # Example 4: Combination positional and keywprd arguments/parameters
# # # def my_func(a,b,c):
# # #     print(a,b,c)
# # #
# # # # my_func(10,20,30)
# # # # my_func(a=10,b=20,c=30)
# # # #my_func(20,30,c=10)
# # # my_func(10,b=20,30)
# # # Example 5: Function can return multiple values
# # # def largest(a,b):
# # #     if a>b:
# # #         return a,b
# # #     else:
# # #         return b,a
# # # x=(largest(10,20))   #20 10
# # # print(x)
# # # print(type(x))#20 10
# # # def myfun(x):
# # #     print(x)
# # #
# # # myfun(1)
# # # Global and local variables:
# # #Global variables:The variables which are created outside of the function is called global variables
# # #Local variables:The variables which are created inside of the function are callled local variables
# # # Example 1:
# # # global_var=10
# # # def myfun():
# # #     local_var=5
# # #     # print(local_var)
# # #     # print(global_var)
# # # myfun()
# # # print(global_var)
# # # print(local_var)
# # #Example 2:
# # xy=100
# # def cool():
# #     xy=200
# #     print(xy)
# # cool()
# # print(xy)
# # print(xy)
# #Example 3:Using global variable in local variable and update the value
# # def cool():
# #     global xy
# #     xy=200
# #     print(xy)
# # cool()
# # print(xy)
# # Two types arguments/parameters we can pass to the function they are
# #1.positional arguments and
# #2.Keyword arguments
# # # Example 1:
# # def myfun(i=5,j=6):
# #     print(i,j)
# # myfun(10,20)   #positional arguments
# # myfun(i=10,j=20)    #keyword arguments
# #Default values assigned to positional arguments
# def cool(i,j=5):
#     print(i,j)
#
# cool(1,6)
# keyword arguments
# def myfun(name,greetingmsg):
#     print(greetingmsg+" "+name)
# myfun(greetingmsg='hello',name='john')
# myfun(name='hello',greetingmsg='john')
#cobination of positional and keyword arguments
# def cool(a,b,c):
#     print(a,b,c)
# # cool(10,20,30)
# cool(10,30,b=20)
# Example 5:Function can return multiple values
# def cool(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
# print(cool(20,10))











