# data types:
# 1.number(int,float,complex)
# string ("abc")
# boolean (True, false(0,1))
# # data structures.

# 1 list square brakets list[]
# 2 heterogenous data structure (a list can different data types together)
# 3 list allows storing duplicate values.
# 4 List are ordered - because they have indeing and indexing start from 0.
# marks = [] empty list
# 5 List are mutable we can change any value anytime and anywhere.
# marks= [29,34,34,445,67,77,"Abhishek",3.14]
# True, 2+1j
# print(marks[1:6])
# marks[3] "mk"

# # Traversing    #(data ke elements ko one by one access karna)
# a = [10,20,40,48]
# for i in a:
#     print(i)

# # Method in list  #object ke andar available function , jo us object par operation on karta hai
# # 1. append() add the value at the last of list 
# marks = [10,20,3,]
# marks.append(90) 
# print(marks)

# #2 Extend.  #extend() ek list method hai jo ek list ke andar dusri list ke saare elements add karta hai.
# marks2b= [70,60,35]
# marks.extend(marks2)
# parnt (marks)

# # 3 insert(index, value) #ek List method hai. Ye list me kisi specific index (position) par element add karta hai
# marks.insert(6,90)
# print(marks)


# # Remove = remove any value from the list.
# a = [10,20,30,40]
# a.remove(10)
# print(a)

# # pop() = remove any value basis on the index.
# a = [10,20,30,49]
# a.pop(3)
# print(a)

# # Clear()= remove every element and givens empty list.
# a = [10,20,30,40]
# a.clea()
# print(a)

# del -> remove list from the memory.
# a = [10,20,30,40]
# del a
# print(marks) 
# print(a)


# #  shallo copy 
# a = [10,20,30,40]
# b= a.copy()#deep copy
# b[3] = 100
# print(a)
# print(b)

# l = [10,20,30,40,50,60]
# for i in l:
#  print(i)



# l = [10,20,30,40,50,60]
# for i in range(len(l)):
#   print(1, l[i])

# l = [10,20,30,40,50,60]
# for i in range(len(l)-1, -1, -1):
#  print(l[i])
# l2 = [][80,70,60,50,40,30,20,10]

# l = [10,20,30,40,50,60,70,80]
# for i in range(len(l)-1, -1, -1):
#  l2.append(l[i]) 
#  l2. insert(len(l2), l[i])
# print(l2)


# arr = [1,2,4,5]
# n = len(arr)
# og_n = n+1
# og_sum =((og_n)*(og_n+1) )//2
# real_sum = 0
# for elem in arr:
#  real_sum +=elem
#  missing=og_sum - real_sum
#  print(missing)


# arr = [10,30,20,40,50]
# is_sorted = True
# n = len(arr)
# for i in range (0,n-1):
#  if arr[i] > arr[i+1]:
#   is_sorted = False
#   if is_sorted:
#    print("list is sorted")
#  else:
#   print("list is un sorted")



# DICTIONARY

#1.Dictionary Annoted by {curly brackets}
#2.dictionary are combination of multiply keys:Value
#3.Dictionary are mutable. 
#4.dictionary are hetrogenous.
#5.in dictionary keys will be unique but valus can be duplicate.
#.dictionary are irdered


# d ={ 1:10, 2:20, 3:30}
# d [3]= 100 #Creating a new key :value pair which never exists.
# print(d)

# d = {1:10,2:20,3:30}
# for i in d:#i-> 1
#     print(i,d[i])#,d[1]


# DICTIN DICT 
# 1. .keys()
# d = {"ravi"80 "rohan": 23,"devraj": 88}print(d.keys())


# 2.value()
# print(d.values()):

# 3. .items() -> both keys and valus
# print(d.items)

# # 4. .pop()-> keys and remove both key and Value
# d.pop("Rohan")
# print(d)

# # .get() -> agar key present hai in dictionary so we will get value for that key either wise none or any message
# print(d.get(4, "not found"))

# # update()-> merge two dictionaries
# a = {1:10, 2:20, 3:30}
# b = {4:40, 5:50, 6:60}
# a.update(b)
# print(a)

# update()-> merge two dictionaries
# a = {1:10, 2:20, 3:30}
# b = {3:30, 5:50, 6:60}
# a.update(b)
# print(a)
 

# # print keys
# d = {"ravi": 70, "abhisek": 30 ,"mohan": 40}
# print(d.keys())



# d= {"ravi": 70, "abhisek": 30 ,"mohan": 40}
# total = 0 
# for i in d.values():
#     total = total + i
# print(total)

# # print student name who secored more than 40
# d = {"ravi": 70, "abhisek": 30 ,"mohan": 40}
# for name,marks  in d:
#     if marks >=70:
#         print(name)

# # find the student the with the highest marks
# d= {"ravi": 70, "abhisek": 88 ,"mohan": 12}
# highest = 0
# top = 0
# for name,marks in d.items():
#     if marks > highest:
#         highest = marks
#         top = name
# print(top, highest)



# # Q Add bonus 5 marks to every student.
# d= {"ravi": 70, "abhisek": 30 ,"mohan": 40}
# for i in d:
#     d[i] = d[i]+ 5
#     print(d)
"""
# SETS
# 1. stores  only unique elements and remove duplicate ones
# 2. Sets are annoted by {} or set()
# 3. sets are unorderd that means there is no indexing in sets
# 4. sets are hetrogenous.
# 5. sets are semi-mutable
"""

# # s = {}dict 
# a = {1,1,2,2,2,3,4,5,70.2 "sample"}
# print(s)

# # list to set 
# l = [1,1,2,3,4,5]
# print(set(l))

# # 1.add -> add an element

# s = {1,2,3,4}
# s.add(5)


# # 2. remove()-> remove an element if the element didn't exists we will get an KEY-ERROR
# s.remove(100)
# print(s)

# # 3. .discard ()-> will not show any error if the 
# # elements is not present in sets
# s.discard(100)
# print(s)


# s1= {1,2,3,4}
# s2={4,5,6,7,8}
# """
# 1. .Union() 
# merge both the sets
# """
# print(f"Union ->{s1.union(s2)}")

# # 2. INTERSECTION 
# # Common elements.

# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"INTERSECTION) -> {s1.intersection(s2)}")


# 3 difference element present in one set but not in other
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}

# print(f" Difference ->  {s1.difference(s2)}")
# print(f" Difference ->  {s2.difference(s2)}")


# 4. symmetric_difference()
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"symmetric_difference ->{s1 . difference(s2)}")



# symmetric_difference()
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"symmetric_difference ->{s1 ^ s2}")

# s = {}
# s = set()
# # Frozenset markes any set with of fixed elements we cannot add element and we cannot remove one.
# s = frozenset([1,2,3,4,5])
# s.add(6)
# print(s)


# """
# Tuple
# 1. ANNOTED by (paranthesis)
# 2. Tuple are ordered.
# 3. Tuple are Immutable.
# 4. Tuple can store duplicate values.
# 5. Hetrogenous -> can store mixed tupe of data
# """

# t = () # Empty Tuple
# t = (1,2,3,4,"Hello",7.32, True)
# print(t)
# print(t[2])


"""
# METHODS IN TUPLE
# #1. .INDEX()-> retur index of any value.
# #2. .Count()-> count occurence of any value
# """
# """
# operations
# + -> concatenation
# * -> Repetition
# """
# t1 = (1,2)
# t2 = (3,4)
# print(t1 + t2)
# print(t1 * 5)

# t = (1,2,[3,4,5,])
# t[2] . append(100)
# print(t)
 

# t = (1,2,[3,4,5,])
# t[2] . append(100)
# print(t)
 

# t = (1,2,[3,4,5,])
# t[3] . insert(100)
# print(t)

# t = (1,2,3,4,5)
# for i in range (len(t)):
#     print(i,t[i])

# t = (1,2,3,4,5,6,7,8)
# print(t[1:6])
 
# t = (1,2,3,4,5,6,7,8)
# t = tuple(reversed(t))
# print(t)

# t = (1,2,3,4,5,6,7,8)











   