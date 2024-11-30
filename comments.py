#this is my first python program

"""this is my first python program
this is my first python program
this is my first python program"""

'''this is my first python program
this is my first python program
this is my first python program
this is my first python program
this is my first python program'''
# import keyword
# print(keyword.kwlist)
# x=100
# x="welcome"
# print(type(x))
# x=100
# y=200
# print(x)
# print(y)
# del x
# print(x)
# print(y)
# operators : A symbol which will perform an operation b/w 2 or more variables
# Arithmetic operators:
# '+','-','*','/','//','**'
#Exmaple 1:
# a=5
# b=2
# print(a+b)   #7
# print(a-b)   #3
# print(a*b)   #10
# print(a/b)    #2.5
# print(a//b)   #2  (quotient)
# print(a%b)    #1 (Remainder)
# print(a**b)    #25
#Relational operators:
# '<','>','<=','>=','==','!='
# Relational operators always returns boolean value  true/false
# Relational operators also knows comparisional operators
# a=5
# b=2
# print(a<b) #false
# print(a>b) #true
# print(a<=b) #flase
# print(a>=b) #true
# print(a==b)  #false
# print(a!=b)   #true
# Logical operators: Logical operators also returns  boolean results
# a           b            a and b        a or b      not a
# true        true         true           true        false
# true        false        flase          true
# false       true         false          true
# false        false       false          false       true
#concatenation : concatenation menas it's basically adding two strings
# Example :
# print('Welcome'+" to Python")
# print(True+1)
# print(False+1)
# print(True+True)
# print(False+False)
# print(True+"welcome")   #Not valid bcz two values are different type
# Formatting output:
# name='john'
# age=30
# sal=50000
# print(name,age,sal)
# Approach 2:
# name='john'
# age=30
# sal=50000
# print("name is :",name)
# print("age is :",age)
# print("sal is :",sal)
# Approach 3:   %s %d %g
# name='john'
# age=30
# sal=5000.5
# print("name is:%s age is:%d sal is:%g"%(name,age,sal))  #when you want to print decimal number use %g
# Approach 4:    {}
# name='john'
# age=30
# sal=5000.5
# print("name is:{} age is:{} sal is:{}".format(name,age,sal))
# How to take input from the user and type conversion
# #Approach 1:
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# print(a+b)
# Approach 2:
#
# a=input("Enter the first number")
# b=input("Enter the second number")
# print(int(a)+int(b))
#Exmaple 2:
# a=float(input("Enter the first decimal number"))
# b=float(input("Enter the second decimal number"))
# print(float(a)+float(b))
# Control statements : if ,else,elif
#Example 1: A person is eligible for vote or not
# age=
# if age>=18:      if statement always returns a boolean value eaither true/false 1/0
#     print("Eligible")
# else:
#     print("Not eligible")
# Example 2:
# if True:
#     print("true condition")
# else:
#     print("False condition")
#Example 3:
# if 0:
#     print("one")
# else:
#     print("Not one")
#Example 4: find a number given number is even or odd
# num=100
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")
#Example 5:
# num=10
# print("Even") if num%2==0 else print("Odd")
#Example 6:
# a=11
# {print("hello"),print("Python")} if a<=10 else {print("hello"),print("Java")}
# Example 6:Multiple condition using elif
# weekno=8
# if weekno==1:
#     print("Sunday")
# elif weekno==2:
#     print("Monday")
# elif weekno==3:
#     print("Tuesday")
# elif weekno==4:
#     print("Wednesday")
# elif weekno==5:
#     print("Thursday")
# elif weekno==6:
#     print("Friday")
# elif weekno==7:
#     print("Saturday")
# else:
#     print("Invalid weekno")
# weekname="Sunday"
# if weekname=="Sunday":
#     print(1)
# elif weekname=="Monday":
#     print(2)
# elif weekname == "Tuesday":
#     print(3)
# elif weekname == "Wednesday":
#     print(4)
# elif weekname == "Thursday":
#     print(5)
# elif weekname == "Friday":
#     print(6)
# elif weekname == "Saturday":
#     print(7)
# else:
#     print("Invalid weekname")
#Range function in python
# we use range along with list() function because range function alone can not return any value
# Range function mostly used in for loop
# Looping statements if() while()
# 3 important points we need remember before writing loop statements
# they are
# initialisation  i mean starting point
# condition
# increment or decrement
# Mutable - can not change values of variable
# immutable - Can change values of variables
# string is immutable
# if the value is changed after updation we can say immutable
# Example 3:+ and * with string
# str="Welcome"
# print(str*100)
# Example 4:Slicing operator []
# str ='welcome'    #[0 1 2 3 4 5 6]
# print(str[0:-2])
# Example 5: ord() chr()
# print(ord('A'))  #Returns the Ascii code of the charcter
# print(chr(30))   #Returns charcter represented by ascii number
# Example 6: max() min() len()
# print(max('abc'))
# print(min('welcome'))
# print(len('mahesh'))
#Example 7: in and not in operators returns true or false
# str="welcome"
# print('em' in str)
#Example 8: string comparision  always returns true/false
# print('kavya'<'kavz')    #False
# # print('welcome'>'wels')  #True
# # print('ramesh'<='rams')   #True
# # print('mahesh'>='mahi')  #True
# # print('sruthi'=='sru')   #Flase
# # print('tarunya'!='tars')    #True
# Testing strings -- returns true or false
# str='welcome to python'
# print(str.isalnum())
# print("welcome".isalpha())
# print('2012'.isdigit())
# print('first'.isidentifier())
# print('welcome'.islower())
# print('WELCOME TO'.isupper())
# print(' '.isspace())
#Example 10: searching for sub-strings -->returns true/false
# str='welcome to python'
# print(str.startswith ('wel'))
# print(str.endswith ('thor'))
# print(str.find('become'))
# print(str.count('z'))
# Example 11:Converting strings
# str="WelcOme To PyThon"    #Only capitalize first letter
# a=str.replace('To','on')
# print(a)    #eolw
# # Example 12: Reverse a string
# s='welcome'
# rev_str=''
# for i in s:
#     rev_str=i+rev_str
# print(rev_str)








