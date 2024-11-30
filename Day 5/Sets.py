# # Example 1: Creating set
# myset1={"apple","banana","Cherry"}
# myset2={1,2,3,4,5}
# myset3={10.5,"Apple",10,"banana"}
# myset4={-1,-2,-3,-4,-5,0,1,2,3}
# myset5={} #empty set()
# print(myset1)
# print(myset2)
# print(myset3)
# print(myset4)
# print(myset5)
# Example 2: Accessing items from set
# myset={"apple","banana","Cherry"}
# for i in myset:
#     print(i)
# Example 3: Value exists in a set or not
# myset={"apple","banana","Cherry"}
# print("apple" in myset)
# print("apple2" in myset)  #it only gives true or false
# Example 4: adding items to set   #we have two methods
# they are add() and update() functions
# for adding single item we use add function
# for adding multiple items we use update function
# myset={"apple","banana","Cherry"}
# myset.add("orange")
# print(myset)
# myset.update(["guava","grapes"])
# print(myset)
# Example 5: Find no.of items in a set
# myset={"apple","banana","Cherry"}
# print(len(myset))
# Example 6: Remove items from set
# we have two function remove() and discard()
# myset={"apple","banana","Cherry"}
# #myset.remove("apple")
# # print(myset)
# myset.discard("xyz")
# print(myset)
# Example 7: clear all items form set
# myset={"apple","banana","Cherry"}
# myset.clear()
# #print(myset)
# del myset
# print(myset)
# Example 8: Joining two sets
# myset1={"apple","banana","Cherry"}
# myset2={1,2,3,4,5,6,7,8,9}
# myset3=myset1.union(myset2)
# print(myset3)
#set : A set is a collection which is unordered and unindexed
# in python sets are written with curly{} brackets
# Example 1:Creating a set
# myset1={"apple","banana","orange","mango","cherry"}
# myset2={1,2,3,4,5}
# myset3={1,"apple",10.5}
# myset4={}
# print(myset1)
# print(myset2)
# print(myset3)
# print(myset4)
#Example 2:Accessing items from
# myset={"apple","banana","orange","mango","cherry"}
# for i in myset:
#     print(i)
#Example 3:Value exists in a set or not
# myset={"apple","banana","orange","mango","cherry"}
# if "guava" in myset:
#     print("Exists")
# else:
#     print("Not Exists")
#Example 4:Adding items to set
# #We have 2 methods one is add() and update()
# # we use add() function for adding one item more than on ewe use update()
# myset={"apple","banana","orange","mango","cherry"}
# myset.update(["grapes","banana2","guava"])
# print(len(myset))
#Example 6:Remove items from set
# we have two functions available in python to remove items from set i.e remove() and discard()
# myset={"apple","banana","orange","mango","cherry"}
# # myset.remove('xyz')
#
# myset.discard('xyz')
# print(myset)
#Example 7:Clear all the items from the set
# myset1={"apple","banana","orange","mango","cherry"}
# myset1.clear()
# print(myset1)
# myset2={"apple","banana","orange","mango","cherry"}
# del myset2
# print(myset2)
#Example 8:Joining two sets
# myset1={"apple","banana","orange","mango","cherry"}
# myset2={1,2,3,4,5}
# myset3=myset1.union(myset2)
# print(myset3)
# myset1.update(myset2)
# print(myset1)













