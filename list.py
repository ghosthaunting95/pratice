#List a array where the index starts from 0
#a list contain string boolean float int or mixtures of all the values
#there some important methods in a list 

a = [1,2,3,4,5]
print(a[4])
# some important methods
#length
#syntax len([list_Name])
# print(len(a))
print("Before append")
print(a)
#append
#syntax(list_Name.Append(3))
# add the element at the end
a.append(6)
print("After append")
print(a)
#remove 
#syntax(list_Name.pop())
#remove the last element
a.pop()
print("After pop")
print(a)
#extend
#syntax list1.extend(list2)
a= [5,4,8,9,10,2]
b=[5,7,8,11,12]
print(a,b)
a.extend(b)
print("before appending")
print(a)
a.append(89)
print("after appending")
print(a)
# #sort
print("before sorting")
print(a)
a.sort()
print("ascending order")
print(a)
print("Descending order")
a.reverse()
print(a)