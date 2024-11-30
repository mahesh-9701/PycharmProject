# # Eample 1: creating dictionary in python
# mydic1={"brand":"hyudai","model":"i10","year":2021}
# mydic2={"x":10,"y":20,"z":30}
# mydic3={}  #Empty dectionary
# print(mydic1)
# print(mydic2)
# print(mydic3)
# Example 2: Accessign items from dictionary
# mydic={"brand":"hyudai","model":"i10","year":2021}
# # print(mydic["brand"])
# # print(mydic["model"])
# # print(mydic["year"])
# # using get() function
# #x=mydic.get("brand")
# print(mydic.get("brand"))
# example 3: changing values in dictionary
# mydic={"brand":"hyudai","model":"i10","year":2021}
# mydic["year"]=2023
# print(mydic)
# Example 4: Reading items from dictionary using loop
# mydic={"brand":"hyudai","model":"i10","year":2021}
# for i in mydic:
#     print(i)  #it prints only keys
# for i in mydic:
#     print(mydic[i]) #it prints only values
# for i in mydic.values():
#     print(i) #it prints only values
# for i,j in mydic.items():
#     print(i,j)  #it prints all the keys and values
# Example 5: check key is exists in dictionary or not
# mydic={"brand":"hyudai","model":"i10","year":2021}
# if "brand" in mydic:
#     print("Exists")
# else:
#     print("Not Exists")
# # Example 6: find no.of items in dictionary
# mydic={"x":10,"y":20,"z":30,"k":45}
# print(len(mydic))
# Example 7: Adding items to dictionary
# mydic={"brand":"hyudai","model":"i10","year":2021}
# mydic["color"]="red"
# print(mydic)
# Example 8: Removing item from dictionary
# mydic={"brand":"hyudai","model":"i10","year":2021}
# mydic.clear()
# print(mydic)
# # Example 9: copying dictionary
# mydic1={"brand":"hyudai","model":"i10","year":2021}
# mydic2={"x":10,"y":20,"z":30}
# mydic2=mydic1
# print(mydic2)
# Dictionary: A dictionary is a collection which is unordered,changeble and indexed
# In python dictionaries are written with curly brackets{} and they are key and value pairs
#Example 1:Creating a dictionary
# mydic1={"employeeid":"1822070","employeename":"Mahesh","Salary":30000}
# mydic2={"studentid":"12345",'studentname':'mahesh','grade':'A'}
# mydic3={1:2,2:3,3:4}
# mydic4={1.5:2.5,3.5:4.5,5.5:6.5}
# mydic5={}
# print(mydic1)
# print(mydic2)
# print(mydic3)
# print(mydic4)
# print(mydic5)
#Example 2:Access items from dictionary
# mydic={"employeeid":"1822070","employeename":"Mahesh","salary":30000}
# print(mydic['employeename'])
# print(mydic.get('employeeid'))
# print(mydic['salary'])
# #Example 3:Changing values in dictionary
# mydic={"employeeid":"1822070","employeename":"Mahesh","salary":30000}
# mydic['employeeid']='1822080'
# print(mydic)
#Example 4:Reading items from dictionary using loop
# mydic={"employeeid":"1822070","employeename":"Mahesh","salary":30000}
# for i in mydic.values():
#     print(i)
# # Example 5:Check key is exists in dictionary or not
# mydic={"employeeid":"1822070","employeename":"Mahesh","salary":30000}
# if 'employeeid' in mydic:
#     print("Exists")
# else:
#     print("Not exists")
#Example 6:Find no.of items in a dictionary
# mydic1={"employeeid":"1822070","employeename":"Mahesh","Salary":30000}
# mydic2={"studentid":"12345",'studentname':'mahesh','grade':'A'}
# mydic3={1:2,2:3,3:4}
# mydic4={1.5:2.5,3.5:4.5,5.5:6.5}
# print(len(mydic1))
#
# print(len(mydic2))
#
# print(len(mydic3))
#
# print(len(mydic4))
#Example 6:Adding items to dictionary
# mydic={"employeeid":"1822070","employeename":"Mahesh","Salary":30000}
# mydic['color']='red'
# print(mydic)
#Example 8:Removing items from the dictionary
# mydic={"employeeid":"1822070","employeename":"Mahesh","Salary":30000}
# mydic.clear()
#Example 9:Copying dictionary
# mydic1={"employeeid":"1822070","employeename":"Mahesh","Salary":30000}
# mydic2={"studentid":"12345",'studentname':'mahesh','grade':'A'}
# mydic2=mydic1.copy()
# print(mydic2)





