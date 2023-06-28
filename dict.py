''''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
#syntax
dict_1 = {"name":"aravind","rollno":"14"}

#Accessing value 
# print(dict_1["name"],dict_1["rollno"])
#values
#syntax
x = dict_1.values()
# print("values",x)
#getting value
y = dict_1.get("name")
# print(y)

#deleting a key
z= dict_1.pop("rollno")
print(dict_1)
