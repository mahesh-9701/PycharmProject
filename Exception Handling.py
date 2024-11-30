# Exception handling definition : Exception is an event which will cause program termination
# we can handle the exception by using try() and except() statements
# Example 1:
# print("Mahesh")
# print("Ravi")
# print("Ramakrishna")
# try:
#     print(10/0)
# except:
#     print("Exception occured and handled.....")
#
# print("Ramesh")
# print("Suresh")
# # Example 3:Multiple except blocks try: ,except: ,else: ,finally:
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("Result is:",result)
# except ZeroDivisionError:
#     print("thrown ZeroDivisionError exception....")
# except SyntaxError:
#     print("Thrown syntexError exception....")
# else:
#     print("No Exception occured....")
# finally:
#     print("Always executes.....")
# # except :Executes only when exception occured
# # Else: Executes only when no exception occured
# # Finally: Always executes
# Exapmle 4:Raising our own exception
# def enterage(num):
#     if num<0:
#         raise ValueError("only integers are allowed")
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# print("cheking number is even or odd by calling function")
# num=111
# try:
#     enterage(num)
# except ValueError:
#     print("Value error occured and handled.....")
