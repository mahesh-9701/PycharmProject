# # example 1: creating a tuple:
# mytuple1=("apple","banana","cherry")
# mytuple2=(1,2,3,4,5)
# mytuple3=("apple",100,"Banana",10.5)
# mytuple4=tuple()  #creating empty tuple
# print(mytuple1)
# print(mytuple2)
# print(mytuple3)
# print(mytuple4)
# Example 2: Accessing the tuple items:
# mytuple=("apple","Banana","cherry","Orange")
# print(mytuple[0:3])
# Example 3: Range of indexes
# mytuple=("apple","Banana","cherry","Orange","Mango")
# print(mytuple[-4:-2]) #"Banana","cherry"
# Example 4: Changing tuple
# changeing tuple is not possible because tuples are immutable changeing valuve is not possible
# mytuple=("apple","Banana","cherry","Orange","Mango")
# mylist=list(mytuple)
# mylist[1]="orange"
# mytuple=tuple(mylist)
# print(mytuple);
# Example 5: Reading tuple items using loop
# mytuple=("apple","Banana","cherry","Orange","Mango")
# for i in mytuple:
#      print(i)
# Example 6: Check if item exists(Searching item in a tuple)
# mytuple=("apple","Banana","cherry","Orange","Mango")
# if 'Guava' in mytuple:
#     print("present")
# else:
#     print("Not present")
# Example 7: tuple lengeth (Counting items in a tuple)
# mytuple=("apple","Banana","cherry","Orange","Mango")
# print(len(mytuple))
# Example 8: add tuple item is not possible because tuples are immutable
# mytuple=("apple","Banana","cherry","Orange","Mango")
# mylist=list(mytuple)
# print(mylist)
# mylist.append("guava")
# print(mylist)
# mytuple=tuple(mylist)
# print(mytuple)
# Example 9: Copy tuple
# tuple1=("apple","banana","orange")
# tuple2=(1,2,3,4,5)
# list1=list(tuple1)
# list2=list(tuple2)
# # print(list1)
# # print(list2)
# list2=list1.copy()
# print(list2)
# mytuple=tuple(list2)
# print(mytuple)
# Example 10: Remove items from tuple is not possible because tuples are immutable
# mytuple=("apple","Banana","cherry","Orange","Mango")
# #mytuple.remove("apple")
# del mytuple
# print(mytuple)
# #Example 11: Join or combine tuple:
# tuple1=("apple","orange","cherry")
# tuple2=(1,2,3,4,5)
# tuple3=tuple1+tuple2
# print(tuple3)
# example 12: Compare two tuples
# tuple1=("apple","banana","orange")
# tuple2=("1","banana","orange")
# if tuple1==tuple2:
#     print("tuples are equal")
# else:
#     print("not equal")
#Tuple:A tuple is a colection which is ordered and unchangeble
#In python tuples are written with round braces()
#Immutable
#Example 1:creating a tuple
# tuple1=('apple','banana','cherry','grape','orange')
# tuple2=(1,2,3,4,5)
# tuple3=(10.5,10,"apple")
# tuple4=()
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)
#Example 2:access the tuple items
#Example 3:Range of indexes
# tuple=('apple','banana','cherry','grape','orange')
# print(tuple[-4:2])
#Example 4:Changing tuple
# if it is immutable changing is not possible
# Mytuple=('apple','banana','cherry','grape','orange')
# Mylist=list(Mytuple)
# Mylist.append('guava')
# Mytuple=tuple(Mylist)
# print(Mytuple)
#Example 5:Reading tuple items using loop
# Mytuple=('apple','banana','cherry','grape','orange')
# for i in Mytuple:
#     print(i)
#Example 6:Check if item exists (searching item in tuple)
# mytuple=('apple','banana','cherry','grape','orange')
# if 'berry' in mytuple:
#     print("Exist")
# else:
#     print("Not Exist")
#Example 7:tuple length counting items in a tuple
# mytuple=('apple','banana','cherry','grape','orange')
# print(len(mytuple))
#Example 9:Copy tuple
# mytuple1=('apple','banana','cherry','grape','orange')
# mytuple2=(1,2,3,4,5)
# mytuple2=mytuple1
# print(mytuple2)
# Example 10:Removing tuple items is not possible
# mytuple=('apple','banana','cherry','grape','orange')
# del mytuple
#Example 11:Joining tuples or adding tuples
# mytuple1=('apple','banana','cherry','grape','orange')
# mytuple2=(1,2,3,4,5)
# mytuple3=mytuple1+mytuple2
# print(mytuple3)
# #Example 12:Compare two  tuples
# mytuple1=('apple','banana','cherry','grape','orange')
# mytuple2=(1,2,3,4,5)
# if mytuple1==mytuple2:
#     print("The tuples are equal")
# else:
#     print("The tuples are not equal")



















