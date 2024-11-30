# #creating a list in python
# # mylist1=["apple","Banana","orange"]
# # mylist2=[10,20,30,40,50]
# # mylist3=["apple",100,"Banana",200]
# # mylist4=[10.5,"apple",100,"banana"]
# mylist5=() #empty list
# # print(mylist1)
# # print(mylist2)
# # print(mylist3)
# # print(mylist4)
# print(mylist5)
# #Example 2: Accessing items from the list
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # print(mylist[2])
# # print(mylist[3:5]) #n-1
# # print(mylist[-2:-1])  #['cherry','mango']  #n-1
# #Example 4: change item value
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # mylist[5]='orange'
# # print(mylist)
# #Example 5: Read the list items using loop:
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # for i in mylist:
# #     print(i)
# # Example 6: check if the item is present in the list or not
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # if "battayi" in mylist:
# #     print("Yes, apple is present")
# # else:
# #     print("No, apple is not present")
# # example 7: list length (Counting no of are presented in a list)
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # print(len(mylist))
# # Example 8: Add items -->we have two functions available in python to add the items in a list that is append() and insert()
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # #mylist.append("Guava")  #this valuve will assin last to the list
# # mylist.insert(-4,"guava")
# # print(mylist)
# # Example 9: Remove items from the list -->We have three methods available in python
# # to remove the items in a list they are pop() function del keyword and clear() function
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # mylist.pop(0)
# # print(mylist)
# #method 2: by using del keyword
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # del mylist[-3]
# # print(mylist)
# # Method:3: By using clear function()
# # mylist=["apple","Banana","orange","kiwi","mango","cherry"]
# # mylist.clear()
# # print(mylist)
# # Example 10: copy list in python
# mylist1=["apple","Banana","orange","kiwi","mango","cherry"]
# mylist2=["1,2,3,4,5"]
# #print(mylist3)
# #mylist2=list(mylist)
#
# # mylist=list(mylist2)
# # print(mylist)
# # print(mylist2)
# # mylist1=mylist2.copy()
# # print(mylist1)
# # print(mylist2)
# # example 11: Combine or join lists
# mylist1=[1,2,3,4,5]
# mylist2=[6,7,8,9,10]
# # # mylist3=mylist1+mylist2
# # # print(mylist3)
# # for i in mylist2:
# #     mylist1.append(i)
# # print(mylist1)
# #using extend() function
# mylist1.extend(mylist2)
# print(mylist1)
# there are 4 types of collections are in python they are
#1.list[]
#2.tuple()
#3.set{}
#4.dictionary{}
#collections are used to store multiple values in a single variable
#List: A list is a collection which is ordered and changeble
#in python lists are written with [] lists are mutable
# Example 1:How to create a list
# list1=[1,2,3,4,5]
# list2=['a','b','c','d','e']
# list3=['apple','banana','cherry','grape','orange']
# list4=['apple',10.5,5,0.2,'a']
# list5=[]
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
#Example 2:Accessing items from the list
#Example 3:Range of indexes
# mylist=['apple','banana','cherry','grape','orange']
# print(mylist[::-1])
# #Example 4:Change item value
# mylist=['apple','banana','cherry','grape','orange']
# mylist[0]='kiwi'
# mylist[1]='Guava'
#
# print(mylist)
#Example 5:Read the list items using loop
# mylist=['apple','banana','cherry','grape','orange']
# for i in mylist:
#     print(i)
#Example 6:Check if the item exist in list or not
# mylist=['apple','banana','cherry','grape','orange']
# if 'orange' in mylist:
#     print("Exist")
# else:
#     print("Not Exist")
# #Example 7:list length(count no of items present in a list)
# mylist=['apple','banana','cherry','grape','orange']
# print(len(mylist))
# Example 8: Add items in a list append() insert()
# mylist=['apple','banana','cherry','grape','orange']
# # mylist.append('guava')
# # print(mylist)
# mylist.insert(1,'guava')
# print(mylist)
#Example 9:Remove item from the list pop()  del keyword  clear()
# mylist=['apple','banana','cherry','grape','orange']
# mylist.pop(0)
# print(mylist)
# mylist=['apple','banana','cherry','grape','orange']
# # del mylist[-1]
# # print(mylist)
# mylist.clear()
# print(mylist)
#Example 10:copy list
# mylist1=['apple','banana','cherry','grape','orange']
# mylist2=[1,2,3,4,5,6]
# # mylist2=list(mylist1)
# # print(mylist1)
# # print(mylist2)
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)
#Example 11: Combine or join lists
# mylist1=['apple','banana','cherry','grape','orange']
# mylist2=[1,2,3,4,5,6]
# # for i in mylist2:
# #     mylist1.append(i)
# # print(mylist1)
# # using extend() function
# mylist1.extend(mylist2)
# print(mylist1)





















