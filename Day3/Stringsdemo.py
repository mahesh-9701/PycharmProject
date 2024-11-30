# #creating string variables
# s="welcome"
# s='welcome'
# s=str('welcome')
# s=str('welcome')
#
# #creating empty strings
# name=str()
# name=""
# name=''
# str1="welcome"
# print(id(str1))  #1946173133888
#
# str1=str1+" to python"
# print(id(str1))  #2984368335408

#+ and * with strings
# str1="welcome"
# print(str1*6)

#Slicing operator []
# str="welcome"
# print(str[1:3])  #el
# print(str[1:])   #elcome
# print(str[:3])  #wel
# print(str[1:-1])  #elcom
# print(str[1:-2])  #elco

#example 5: ord() and char() functions
# print(ord('A'))
# print(chr(107))

#example 6: max() min() len() operators
# print(max('cool'))
# print(min('maheshz'))
# print(len("hello"))
# example 7: in and not in operators
# s=("welcome")
# print('come' in s)
# print('lome' not in s)
# print('e'not in s)
# string comparision
# print("tim" == "tin")  #false
# print("free" != "freedom")  #true
# print("freedom" >= "free")
# print("arrow" < "aron")
# print("abc" > "r")
#example 8: testing strings this will return true/false
# s="welcome to python"
# print(s.isalnum())
# print("welcome".isalpha())
# print("2012" .isdigit())
# print("" .isidentifier())
#example 9: searching substrings
# s="welcome to python"
# print(s.endswith ("thon"))  #true
# print(s. startswith("good"))  #false
# print(s. find("come"))    #3
# print(s. find("become"))  #-1
# print(s. count("o"))  #3

#example 11: converting strings
# s="string in python"
# s1=s.capitalize()
# print(s1)
# s2=s.title()
# print(s2)
# s3=s.lower()
# print(s3)
# s4=s.upper()
# print(s4)
# s5=s.swapcase()
# print(s5)
# s6=s.replace("in", "one")
# print(s6)
# example 12: reverse a string
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str;
#
# print("reversed string is:", rev_str)
#method-2
s="welcome"
rev_str=s[::-1]
print(rev_str)
