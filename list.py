
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