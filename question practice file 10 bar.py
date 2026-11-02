# for i in range(8,81,8):
#  print(i)

# n = int(input("tell your number:-"))
# for i in range(n,n*10+1,n):
#     print(i)

# n = int(input("enter your number"))
# for i in range(n,n*10+1,n):
#        print(i)

# n = int(input("tell your number"))
# for i in range(n,n*10+1,n):
#        print(i)

# n = int(input("your choice"))
# for i in range(n,n*10+1,n):
#        print(i)



# amount = int(input("Enter the membership"))
# membership = int(input("enter the membership atatus (1 for member,0 for non-member)"))
# if membership == 1:
#        if amount > 1000:
#               print("Discount available")
#        else:("no discount")
# else:
#        print("no discount")       
# n = int(input("Enter the number"))
# for i in range(n,n*10+1,n):
#        print(i)



# For Loop Question
#Q1. Print number from 1 to 10
# for i in range(1,11,1):
#     print(i)

# Q2.Print all even numbers from 1 to 20.
# for i in range(1,21):
#     if i %2 == 0:
#         print(i)


#Q3.Print all odd numbers from 1 to 20.
# for i in range(1,21):
#     if i %2 != 0:
#         print(i)

# Q4. Find the sum of numbers from 1 to 10.
# sum = 0
# for i in range(1,11):
#    sum = sum + i
# print(sum)


#Q5. Take a number as input and print its multiplication table.
# num = int(input("Enter the number"))
# for i in range(1,11):
#    print(num * i)


#Q.Print numbers from 10 to 1 in reverse order.
# for i in range(10,0,-1):
#    print(i)

#Q7.Print all numbers from 1to 100 that are divisible by 5.
# for i in range(1,101,1):
#    if i %5 == 0:
#       print(i)

#Q8.Find the sum of even numbers from 1 to 50.
sum = 0
# for i in range(1,51):
#    if i %2== 0:
#       sum = sum + i
#       print(sum)

#Q9.Take a number as input and find its factorial.
# num = int(input("Enter the number"))
# fact = 1
# for i in range(1,num + 1):
#    fact = fact * i
#    print(fact)


#Q10. print number from 1 to 100 that are divisible by both 3 and 5.
# for i in range(1,101):
#    if i%3 ==0 and i % 5== 0:
#     print(i)

# n = int(input("enter the number"))
# for i in range(1, n + 1):
#     print(i)

# present = 0 
# Absent = 0
# for i in range(7):
#     status = input("enter the p or a ")
#     if status == "p":
#         present += 1
#     elif status =="A":
#         Absent += 1
#         print("present days:", present)
#         print("absent days:",Absent)


# present = 0 
# Absent = 0 
# for i in range(7):
#  status = input("enter the p or a")
# if status == "p":
#  present += 1
# elif status == "A":
#  Absent += 1
# print("present days:", present)
# print("absent days:", Absent)




# while loop
# Q1.
# n = int(input("enter a number:"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
#     print(reverse)

# # Q2.check Palindrome Number
# n = int(input("enter a number:"))
# original = 0
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
#     if original == reverse:
#      print("palindrome")
# else:
#   print("not palindrome")

# # Q3.count digits greater than 5
# n = int(input("enter a number:"))
# count = 0
# while n > 0:
#    digit = n % 10
#    if digit > 5:
#       count = count + 1
#    n= n // 10
#    print(count)
# # Q4. Product digit
# n = int(input("enter a number:"))
# product = 1
# while n > 0:
#    digit = n % 10
#    product = product * digit
#    n = n // 10
#    print(product)

# # Q5. check whether a number contains digit 7
# n = int(input("enter a number:"))
# found = False
# while n > 0:
#    digit = n % 10
#    if digit ==7:
#       found = True
#       break
#    if found:
#       print("present")
#    else:
#       print("no present")

# # Q6.count digits divisible by 3
# n = int(input("enter a number:"))
# count = 0
# while n > 0:
#    digit = n % 10
#    if digit % 3==0:
#       count =+1
#    n = n // n
# print("count",count)

# #Q7. replace every digit with 9
# n = int(input("enter a number:"))
# result = ""
# for digit in str(n):
#    result = result + "9"
# print(result)

# #Q8. Find the Second Largest digit
# n =int(input("enter a number:"))
# largest = -1
# second_largest = -1
# while n > 0:
#    digit = n % 10
#    if digit > largest:
#       second_largest = largest
#       largest = digit
#    elif digit > second_largest and digit != largest:
#       second_largest = digit
#    n = n // 10
# print("second largest digit:",second_largest)

# # Q9.Check whether all digits are Even
# n = int(input("enter a number:"))
# all_even = True
# while n > 0:
#    digit = n % 10
#    if digit % 2 !=0:
#       all_even = False
#       break
#    n = n // 10
#    if all_even:
#        print("All digit are even")
#    else:
#          print("All digit are not even")

# #Q.10 Remove the Last Digit
# n = int(input("enter a number:"))
# n = n // 10
# print(n)


# n = int(input("enter the number:"))
# a = 0
# b = 1
# for i in range(n):
#  c = a+b
#  a = b
#  b = c


#  text = input("enter the number")
#  count = 0
#  for ch in text:
#   if ch == "aeiouAEIOU":
#    count +=1
#    print(f"total vowels : {count}")

#    text = input("enter the number")
#    targer =input("enter a cha")
#    count = 0
#    for ch in text:
#       if ch == target:
#          count+=1
# print(count)



# a = "hello i am data scientist"
# print(a[0:5:1])
# print(a[11:15:1])
# print(a[16:25:1])


# n = input("enter the number:")
# for i in range(1,n+1):
#     if i%10 ==7:
#         print(i,end=" ")

# def number_ending_with_7(n):
#     result = []
#     for i in range(1,n+1):
#     if i%10==7:
#         result.append(i)
#         return result

#     n = int(input("ebter the number"))
# ans = number_ending_with_7(n))
# m = int(input("enter the number"))
# ans=(number_ending_with_7(m))
# print(f"fistans : {ans1}, second ans {ans2}")

# n = int(input("enter the number"))
# temp = n
# sum =0
# while n >0:
#     digit = n %10
#     sum +=digit
#     n//=10
# for i in sum > 0 and temp % sum ==0:
#      print("harshad number")
# else:
#     print("not a harshad number")



# n = int(input("inter the number:"))
# fact = 1
# for i in range(1,n +1):
#    fact = fact*i
#    print("factrial=",fact)

# n = int(input("enter the numbee:"))
# fact = 1
# for i in range(1, n+1):
#    fact = fact*i
#    print("factrial=",fact)

# n = int(input("enter the number:"))
# fact = 1
# for i in range(1, n +1):
#    fact = fact*i
#    print("factrial=",fact)

# n = int(input("enter the number:"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
#     print("factrisl=",fact)

# n = int(input("enter the number"))
# count= 0
# for i in range(1, n +1):
#     if i%3==0 and i%5==0:
#      count+=1   
# print(f"count :{count}")

# n = int(input("enter the number:"))
# count = 0
# for i in range(1, n+1):
#     if i%3==0 and i%5==0:
#      count+=1
# print(f"count{count}")

# n = int(input("enter the number:"))
# count = 0
# for i in range(1, n+1):
#     if i%3==0 and i%5==0:
#         count+=1
# print(f"count{count}")

# n = int(input("enter the number:"))
# temp = 0
# sum = 0
# while n>0:
#     digit = n%10
#     fact = 1
    
#     for i in range(1,digit+1):
#      fact*=i
#      sum +=fact
#      n = n//10
        
# if temp == sum:
#     print("strong number")
# else:
#     print("Not a strong number")


# n = int(input("enter the number:"))

# for digit  in range(0,10):
#     temp = n
#     count_digit = 0
# while temp > 0:
#       last_digit = temp%10
#       if last_digit == digit:
#         count_digit +=1
      
#       temp //=10
# if count_digit > 0:
#    print(f"{digit} {count_digit}")

# n = int(input("enter the numnber:"))
# temp = 0
# smallest = 9
# while temp >0:
#     digit = temp%10
#     if digit < smallest:
#         smallest = digit
#         temp //10
# print(f"chota digit in{n} is {smallest}")



# attempts = 3
# has_access_mainmenu = False
# while attempts > 0:
#     entered_pin = int(input("enter the pin"))
#     if entered_pin == 1234:
#         has_access_mainmenu = True
#         break
#     else:
#         attempts -=1
#         if attempts>0:
#             print(f"incorrect pin! you have {attempts} attempts remaining")
#         else:
#             print("card blocked")
#     balance = 60000
#     if has_access_mainmenu == True:
#         while True:
#             print("ATM Menu")
#             print("1 -> check balance")
#             print("2 -> deposit cash")
#             print("3 -> withdraw cash")
#             print("4 -> exit")
#             choice = int(input("enter the choice"))
#             if choice == 1:
#                 print(f"Balance is {balance} choice")
#             elif choice ==2:
#                 depoist_amount = int(input("enter the amount to deposit"))
#                 if depoist_amount >0:
#                  balance += depoist_amount
#                 print("f updated balance is {balance}")
#             else:
#                 print("invalid deposit amount")
#         else choice ==3:
#             withdraw_ammount = 
#         int(input("enter the amount to withdraw"))
#     elif withdraw_ammount 
#                balance-=withdraw_ammount
#     print(f"withdraw done and updated balance is {balance}")
# else:
#     print("insufficient balance")
#     if choice ==4:
#                  print("thank you for using our atm")
#     break
#     else:
#     print("invalid choice ! please enter number from 1 - 4")


# a= int(input("enter the value:"))
# b= int(input("enter the exponent:"))
# power = a
# for i in range(b-1):
#     power = power * a
# print(f"after power you answer is {power}")


# n = int(input("enter the number(prime check)"))
# for i in range(2,n):
#     if n % i ==0:
#        print("sorry you number is composite")
#     break
# else:
#     print("your number is prime")


# a = int(input("please tell your number"))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a%10
#     a = a //10
#     if rev == copy:
#            print("yes your number is pallindrome")
#     else:
#            print("sorry your number is not pallindrome")


# a = 8
# dup = a
# count = 0
# square = a ** 2
# while a > 0:
#     count = count + 1
#     a = a//10
#     extract = square % (10**count)
#     if extract == dup:
#         print("you number is automorphim")
#     else:
#       print("sorry not an automorphim number")




# arr = [10,20,30,40,50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i], arr[n-1-1] = arr[n-i-1],arr[i]




# arr = [10,-5,20,-3,0,8]
# print("positive")
# for elem in arr:
#     if elem>0:
#         print(elem)

#         print("negative")
#         for elem in arr:
#             if elem<0:
#               print(elem)

# cal = [10,20,30,40]
# sum = 0
# for i in cal:
#     sum = sum+i
# ave = sum / len(cal)
# print(ave)


# arr = [2,96,69,77,20]
# max = arr[0]
# index = 0
# for i in range(1,len(arr)):
#     elem = arr[i]
# if elem > max:
#     max = elem
# index = i
# print(f"max is {max} at index{index}")


# for i in range (5):
#     for i in range(5):
#         print("*",end="")
#         print()


# n= 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



# n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+i+1):
#         print("*",end="")
#     print()



# l = [15,5,20,8,12]
# smallest = float('inf')
# second_smallest = float('inf')
# for i in l:
#    if i <smallest:
#       second_smallest = smallest
#       smallest = i
#    elif i > smallest and i < second_smallest:
#     second_smallest = i 
#     print("second smallest:",second_smallest)


# arr = [2,4,3,5,7,8]
# target = 2
# n = len(arr)
# for i in range(n):
#    for j in range(i+1,n):
#       if (arr[i]+ arr [j]) == target:
#           print(arr[i],arr[j])


# arr = [10,20,30,40,50]
# n = len(arr)
# sub = [20,30,40]
# m = len(sub)
# for i in range(0,n-m+1):
#    if arr[i:i+m] == sub:
#       print("sublist found")
#       break
#    else:
#     print("not sublist found")


# Q1.Find the largest value 
# given a dictionary containing numbers find the
# largest value without using max ()

# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     if value> largest:
#         largest = value
# print("largest value",value)

# a = {'a':10,'b':25,'c':15,'d':40}
# largest = 0
# for value in a.values():
#     if value > largest:
#         largest = value
# print("largest value",largest)

# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     if value> largest:
#      print("largest value largesr")

#      a = {'a':10,'b':25,'c':15,"d":40}
#      largest = 0
#      for value in a.values():
#          if value in a.values:
#            largest = value
#            print("largest value",largest)

# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a. values():
#    largest = 0
#    if value > largest:
#       print("largest value",largest)

# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#    largest = 0
#    if value > largest:
#       print("largest value",largest)


# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     largest = 0
#     if value > largest:
#         print("largest value",largest)




# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.valies():
#     largest = 0
#     if value > largest:
#         print("largest value",largest) 



# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     largest = 0
#     if value > largest:
#         print("largest value",largest)


# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     largest = 0
#     if value > largest:
#         print("largest value",largest)

# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a. values():
#     largest = 0
#     if value > largest:
#         print("largest value",largest)


# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     largest = 0
#     if value > largest:
#      print("largest value",largest)


# a = {'a':10,'b':25,'c':15,"d":40}
# largest = 0
# for value in a.values():
#     larhest = 0
#     if value > largest:
#         print("largest value",largest)



# arr1 = [1,4,7,10]
# arr2 = [2,3,8,9]
# n1 = len(arr1)
# n2 = len(arr2)
# i= 0
# j =0
# ans =[]
# while i<n1 and j<n2:
#   if arr1[i]<arr2[j]:
#     ans .append(arr1[i])
#     i+=1
#   else:
#       ans.append(arr2[j])
#       j+=1
# while i < n1:
#      ans.append(arr1[i])
#      i+=1
# while j <n2:
#       ans.append(arr2[j])
#       j+=1

# print(ans)


# a = [23,67,123,1,54,7,98,45,23,13,6,68]
# search  = 67
# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element found at index{i}")
#         break
# else:
#     print("sorry no such element exist")


# a = [23,67,123,1,54,7,98,45,23,13,6,68]
# search = 45
# start = 0
# last = len(a)-1
# mid = (start +last )//2

# while start <= last:
#     if a[mid]== search:
#         print("element found at index{mid}")
#         break
#     elif a[mid] < search:
#         start = mid +1
#         mid =(start + last)//2

#     elif a[mid]> search:
#         last = mid -1
#         mid = (start + last)//2
# else:
#     print("sorry no such element exist")



# a = [12,12,12,34,34,34,6,6,6,7,7,8,8,3,4,5,6] duplicare value 
# s = set(a)
# print(s)

# s1={12,13,24,56}
# s2 ={13,45,67,4,5}
# s1.discard(12)
# print(s1)


# s1={12,13,45,56}  #intersection 
# s2 ={13,45,56,4,5}
# print(s1 & s2)


# s1={10,20,30,40,5} #pop
# s2 ={30,40}
# s1.pop()
# print(s1)

# s1={10,20,30,40} #symmetric
# s2 ={30,40,50,60}
# print(s1 ^ s2)


# s1={10,20,30,40} # union
# s2 ={30,40,50,}
# print(s1 | s2)


# # traversing on set
# s = {12,13,32,34,5,54}
# for i in s:
#     print(i)


# d = {"hello":100,"bro":200,"sunday":300}
# l=[10,20,30,40]
# print(d['bro'])


# d = {"hello":100,"bro":200,"sunday":300}
# (d['bro']) = 2000
# print(d)

# a ={10:100,20:200,30:300,40:400}
# a.setdefault(12,default = 1200)
# print(a)

# a ={10:100,20:200,30:300,40:400}
# a.setdefault(12)
# print(a)
# popped = a.popitem()
# print(popped)

# a = {20:100,20:200,30:300}  #update
# b= {20:300,40:500,50:500}
# a.update(b)
# print(a)


# a= [1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#       d[i] = 1
# # print(d) 
# print(d.keys())    


# a = [1,1,2,2,3,3,4,4,5,5,5,5,6,6,7,7,8,8,9,9,0]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# # print(d)
# for i in d:
#     if d[i] > 1:
#         print(i)



# Q10. count positive and negative values given a dictionary
# containing numbers ,count how many values are positive
# and how many are negative.

# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive = 0
# negative = 0
# for value in a. values():
#     if value > 0:
#         positive +=1
#     elif value <0:
#         negative +=1
        
# print("positive number",positive)
# print("negative number",negative)
    
    

# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive =0
# negative = 0
# for value in a. values():
#     if value > 0:
#         positive +=1
#     elif value <0:
#         negative +=1
#         print("positive number",positive)
#         print("number numer",negative)

# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive = 0
# negative = 0
# for value in a.values():
#     if value > 0:
#         positive +=1
#     elif value < 0:
#         negative +=1
#         print("positive number",positive)
#         print("negative number",negative)

# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive = 0
# negative =0
# for value in a.values():
#     if value > 0:
#         positive+=1
#     elif value <0:
#         negative +=1
#         print("positivre number",positive)
#         print("negative number",negative)

# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive = 0
# negative = 0
# for value in a. values():
#     if value > 0:
#         positive+=1
#     elif value <0:
#         negative+=1
# print("positive number",positive)
# print("negative number",negative)


# a ={'a':10,'b':-5,'c':20,'d':-8,'e':7}
# positive= 0
# negative = 0
# for value in a. values():
#     if value > 0:
#         positive+=1
#     elif value <0:
#         negative+=1
# print("positive number",positive)
# print("negative number",negative)



# #  Q9. count values equal to a given number given
# # a dictionary and a number count how many times
# # that number appears as a value in the dictionary

# # a = {'a':10,'b':20,'c':10,'d':30}
# # num = 10
# # count = 0
# # for value in a. values():
# #     if value == num:
# #         count +=1
# # print(count)

# a = {'a':10,'b':20,'c':16,'d':30}
# num = 10
# count= 0
# for value in a.values():
#     if value == num:
#         count +=1
#         print(count)

# a = {'a':20,'b':27,'c':23}
# num = 10
# count = 0
# for value in a.values():
#     if value == num:
#         count +=1
#         print(count)

# a = {'a':19,'b':30,'c':23}
# num = 0
# count= 0
# for value in a.values():
#     if value == num:
#         count +=1
        # print(count)

# a = {'a':10,'b':20,'c':50}
# num = 10
# count = 0
# for value in a. values():
#     if value== num:
#         count+=1
#         print(count)

# a = {'a':12,'b':23,'c':22}
# num =10
# count =0
# for value in a. values():
#     if value==num:
#         count+=1
#         print(count)



#  Upadate all value 
# increase every value in a dictionary by 5

# a= {'a':10,'b':25,'c':15,}
# for key in a:
#    a[key]= a[key] +5
# print(a)


# a = {'a':22,'b':23,'c':33}
# for key in a:
#     a[key]= a[key]+5
#     print(a)

# a = {'a':22,'b':23,'c':33}
# for key in a:
#     a[key]= a[key]+5
#     print(a)


# a = {'a':22,'b':23,'c':33}
# for key in a:
#     a[key]= a[key]+ 5
#     print(a)

# a = {'a':22,'b':23,'c':33}
# for key in a:
#     a[key]= a[key]+5
    # print(a)


# Q5.Find a key with a given value 
# given a dictionary and a value find the key 
# associated with that value.

# v = int(input("enter the value:"))
# a ={'a':10,'b':20,'c':30}
# for key ,values in a.items():
#     if values == a:
#      print(key)

# n = int(input("enter the number:"))
# a ={'a':22,'b':23,'c':22}
# for key ,values in a.items():
#     if values==a:
#         print(key)


# n = int(input("enter the number:"))
# a ={'a':22,'b':33,'c':44}
# for key ,values in a. items():
#     if values == a:
#         print(key)

# n = input("enter the number:")
# a={'a':22,'b':33,'c':42}
# for key ,values in a.items():
#     if values == a:
#         print(key)



# # Q4. sum of even values 
# # Find the sum of all even values present in a dictionary

# # a = {'a':10,'b':25,'c':15,"d":40}
# # total = 0
# # for value in a.values():
# #     if value %2 ==0:
# #         total += value
# # print("sum 0f sum value:",total)

# a ={'a':22,'b':32,'c':23,'d':45}
# total = 0
# for value in a.values():
#     if value%2 ==0:
#         total += value
#         print("sum of sum value:",total)


# a = {'a':22,'b':33,'c':51}
# total = 0
# for value in a.values():
#     if value %2 ==0:
#         total += value
#         print("sum of sum value:",total)


# a = {'a':22,'b':33,'c':51}
# total = 0
# for value in a.values():
#     if value %2 ==0:
#         total += value
#         print("sum of sum value:",total)

# a = {'a':22,'b':33,'c':51}
# total = 0
# for value in a. values():
#     if value %2==0:
#         total += value
#         print("sum of sum value:",total)


# a = {'a':22,'b':33,'c':51}
# total = 0
# for value in a.values():
#     if value%2==0:
#         total += value
#         print("sum of sum value:",total)


# a = {'a':22,'b':33,'c':51}
# total = 0
# for value in a. values():
#     if value %2 ==0:
#         total+=value
#         print("sum of sum value:",total)




# #  Q3. count even and odd values 
# # count how many value in a dictionary 
# # are even and how many are odd

# # a= {'a':10,'b':15,'c':20,"d":7}
# # even = 0
# # odd = 0
# # for value in a.values():
# #     if value %2 ==0:
# #         even+=1
# #     else:
# #         odd+=1
# # print("even count",even)
# # print("odd count",odd)


# a= {'a':10,'b':15,'c':20,"d":7}
# even =0 
# odd = 0
# for value in a. values():
#     if value %2==0:
#         even+=1
#     else:
#         odd+=1
#         print("even count",even)
#         print("odd count",odd)

# a= {'a':10,'b':15,'c':20,"d":7}
# even = 0
# odd = 0
# for value in a. values():
#     if value % 2==0:
#         even+=1
#     else:
#         odd+=1
#         print("even count",even)
#         print("odd count",odd)

# a= {'a':10,'b':15,'c':20,"d":7}
# even = 0
# odd = 0
# for value in a. values():
#     if value % 2== 0:
#         even +=1
#     else:
#         odd+=1
#         print("even count",even)
#         print("odd count",odd)


# a= {'a':10,'b':15,'c':20,"d":7}
# even = 0
# odd = 0
# for value in a. values():
#     if value %2 ==0:
#         even+=1
#     else:
#         print("even count",even)
#         print("odd count",odd)


# a= {'a':10,'b':15,'c':20,"d":7}
# even = 0
# odd = 0
# for value in a. values():
#     if value %2==0:
#         even+=1
#     else:
#         odd+=1
#         print("even count",even)
#         print("odd count",odd)



# #  Q2. Find the smallest value 
# # given a dictionary containing numbers,find the
# #smallest value without using min()


# # a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# # smallest = a['a']
# # for value in a.values():
# #     if value < smallest:
# #         smallest = value

# # print("smallest value", smallest)


# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# smallest = a['a']
# for value in a.values():
#     if value < smallest:
#         smallest = value
# print("smallest value",value)

# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}

# smallest = a['a']
# for value in a. values():
#     if value < smallest:
#         smallest = value
# print("smallest value",value)


# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# smallest = a['a']
# for value in a.values():
#     if value < smallest:
#         smallest = value 
# print("smallest value",value)

# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# smallest = a['a']
# for value in a.values():
#     if value < smallest:
#         smallest = value
# print("smallest value",value)


# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# smallest= a['a']
# for value in a.values():
#     if value < smallest:
#       smallest = value

# print("smallest values",value)


# a = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# largest = 0
# for value in a. values():
#     if value > largest:
#         largest = value
# print("largest value",value)

# # Q7.Print All Keys
# # Print all the keys present in a dictionary using a loop.

# # my_dict = {
# #      "name": "Rahul",
# #      "age": 20,
# #      "city": "Bhopal"
# # }
# # for key in my_dict:
# #   print(key)    


# my_dict = {
#     "name": "ravi",
#     "age": "20",
#     "city": "bhopal"
# }
# for key in my_dict:
#     print(key)

#     my_dict = {
#         "name":"rahul",
#         "age":"20",
#         "city":"Aurangabad"
#     }
# for key in my_dict:
#     print(key)

# my_dict = {
#     "name":"ravi",
#     "age":"20",
#     "city":"Aurangabad"
# }
# for key in my_dict:
#     print(key)


# my_dict ={
#     "name":"akash",
#     "age":"20",
#     "city":"Aurangabad"

# }
# for key in my_dict:
#     print(key)


#  Appiy the following rules:

# Age below 5 free
# Age 5 to 17 50% discount
# Age 18 to 59 Full0% discount
# Age 60 or above 3
# print the final tickat print

# a = int(input("enter the age of passenger:"))
# if a < 5:
#     price = 0
# elif a <=17:
#     price = 200 * 50 / 100
# elif a<= 59:
#     price = 200
# else:
#     print = 200 * 70/100
#     print("Final tickat price:,price")



# Q10. Exam Eligibility
# Take a student's attendence percentage and marks as input.
# A student is eligible to appear for the final exam only if:
# Attendance is 75% or above
# Marks are 40 or above
# if both conditions are satisfied,print
# "Eligible"
# otherwise, print "Not Eligible"

# a = float(input("Enter the attendance percentage")) 
# marks = float(input("Enter the marks"))
# if a >= 75 and marks >= 40:
#     print("Eligible")
# else:
#     print("Not Eligible")

# a = float(input("enter the attendance percentage"))
# marks = float(input ("enter the marks"))
# if a >= 75 and marks >=40:
#     print("eligible")
# else:
#     print("not eligible")


# a = float(input("enter the attendance percentage"))
# marks = float(input("enter the marks"))
# if a >= 75 and marks >=50:
#     print("eligible")
# else:
#     print("not eligible")

# a = float(input("enter the attendace percentage"))
# marks = float(input("enter the marks"))
# if a >= 75 and marks >=50:
#     print("eligible")
# else:
#     print("not eligible")

# a = float(input("enter the attendance percentage:"))
# marks = float(input("enter the marks"))
# if a >= 75 and marks >=50:
#     print("eligible")
# else:
#     print("not eligible")

# a = float(input("enter the attendence percentage:"))
# marks = float(input("enter the number"))
# if a >= 75 and marks >=50:
#     print("eligible")
# else:
#     print("not eligible")

# a = float(input("enter the attendence percentage:"))
# marks = float(input("enter the number"))
# if a > 75 and marks >=50:
#   print("eligible")
# else:
#   print("not eligible")


# Electricity Bill
# Take the number of unit consumed as input.
# Calculate the electricity bill according to these rules:
# Up to 100 units 5 per unit
# 101 to 200 units 7 per unit
# Above 200 units 10 per unit
# print the total bill.

# a = int(input("Enter the unit:"))
# if 100 >= a:
#     print(f"total bill {a*5}")

# elif a >101 and a < 200:
#     print(f"total bill = {a*7}")

# elif a > 200:
#     print(f"total bill = {a*10}")

# a = int(input("enter the unit:"))
# if 100 >= a:
#     print(f"total bil{a*5}")

# elif a> 101 and  a < 200:
#     print(f" total bill = {a*7}")
# elif a > 200:
#     print(f"total bill = {a*10}")


# a = int(input("enter the unit"))
# if 100 >=a:
#     print(f"total bill{a*5}")
# elif a> 101 and a <200:
#     print(f"total bill ={a*7}")
# elif a > 200:
#     print("total bill ={10*7}")


# a = int(input("enter the unit:"))
# if 100 >=a:
#     print(f"total bill{a*5}")
# elif a > 101 and a <200:
#     print(f"total bill ={a*7}")
# elif a > 200:
#     print("total bill ={10*7}")



# 7. Time of Day 
# Take the hour as input in 24-hour format.

# a = int(input("Enter the hour: "))
# if a < 0 or a > 23 :
#     print("invalid hour")
# elif a >= 5 and a <= 11:
#     print("Morning")
# elif a >= 12 and a <= 16:
#     print("Afternoon")
# elif a >= 17 and a <= 20:
#     print("Evening")
# else:("Night")



# a = int(input("enter the hour:"))
# if a < 0 or a > 23:
#     print("invalid hour")
# elif a >= 5 and a <= 11:
#     print("morning")
# elif a >= 12 and a <= 16:
#     print("afternnoon")
# elif a>= 17 and a <= 20:
#   print("evening")
#   print("night")

# a = int(input("enter the hour:"))
# if a < 0 or a>23:
#     print("invalid hour")
# elif a >= 5 and a<= 11:
#     print("morning")
# elif a >=12 and a<= 16:
#     print("afternoon")
# elif a>=17 and a <= 20:
#     print("evening")
#     print("night")

# a= int(input("enter the hour:"))
# if a < 0 or a>23:
#     print("invilid hour")
# elif a >= 5 and a<= 11:
#     print("morning")
# elif a >=12 and a<= 16:
#     print("afternoon")
# elif a>=12 and a<=16:
#     print("evening")
#     print("night")



#  Shopping Delivery Charge
# Take the shopping amount as input.
# Calculate the delevery charge:
# Amount below 500 - 50 delivery charge
# Amount from 500 to  999 -- 30 delivery charge
# Amount 1000 or above free delivery
# print the final amount including the delivery charge

# amount = float(input("Enter the shopping: "))
# if amount < 500:
#     delivery = 50
#     final_amount = amount  + delivery
# elif amount >= 500 and amount <= 1000:

#     delivery = 30
#     final_amount = amount + delivery
# else:
#    amount >= 999
#    delivery = 0
#    final_amount = amount + delivery
# print(f"Delivery charge = {delivery}")
# print(f"final amount = {final_amount}")


# amount = float(input("enter the shopping:"))
# if amount < 500:
#     delivery = 50
#     final_amount = amount + delivery
# elif amount >= 500 and amount <=1000:
#     delivery = 30
#     final_amount = amount + delivery
# else:
#     amount >= 900
#     delivery = 0
#     final_amount = amount + delivery
#print(f"delivery charge ={delivery}")
#print(f"final amount = {final_amount}")

# amount = float(input("enter the shoping"))
# if amount < 500:
#     delivery = 50
#     final_amount = amount + delivery
# elif amount >= 500 and amount <=1000:
#     delivery = 30
#     final_amount = amount + delivery
# else:
#     amount >= 900
#     delivery = 0
#     final_amount = amount + delivery
# print("delivery charge ={delivery}")
# print("final_amount = {final_amount}")


# amount = float(input("enter the shopping"))
# if amount < 600:
#       delivery = 60
#       fial_amount = amount + delivery
# elif amount >= 600 and amount <= 899:
#        delivery = 45
#        final_amount = amount + delivery
# else:
#        amount >= 1000
#        delevery = 0
#        final_amount = amount + delivery
# print("delivery charge = {delivery}")
# print("final_amount = {final_amount}")


# sen = "python is easy and python is powerful and esay"
# sen = sen.lower()
# print(sen)
# words = []
# word =""
# for ch in sen:
#      if ch!="":
#       word+=ch
# else:
#       words.append(word)
#       word =""
# print(word)


# sen = "Eat sleep code and repet code and eat clean"
# sen = sen.lower()
# ans ={}
# word = sen 

# for i in range(10,41,1):
#     print(i)

# for i in range(-10,21,1):
#     print(i)

# for i in range(35,4,-1):
      # print(i)

# n = int(input("tell the number you want table of"))
# for i in range(n,(n*10)+1, n):
#     print(i)
 

# a = "hello i am mitunjay yadav"
# for i in a:
#     print(i)

# for i in range(0,len(a),1):
#     print(a[i])

# a = "Nature"
# for i in range(len(a)):
#      print(i)
#   print(a[i])

# Q.2
# n = int(input("please tell me how many times you wan tto print:-"))
# for i in range(n):
#   print(f"{i+1}:hello world")

# n = int (input("till where you want your numbers:-"))
# for i in range(1,n+1):
#   print(i)

# n = int (input("till where you want your numbers:-"))
# for i in range(n,0,-1):
#   print(i)

# sum of natural number(1 to 10)
# n = int(input("till where your sum"))
# a = 0
# for i in range(1,n+1):
#     a = a + i
# print(f"your sum is {a}")


# n = int(input("which number fsctorial you want :-"))
# fact = 0
# for i in range(1,n+1):
#     fact = fact * i
# print("your factorial is {fact}")
    


# n = int(input("tell your range:"))
# odd_sum = 0
# even_sum = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even_sum +=i
#     else:
#         odd_sum +=i
# print(f"hello your even sum is {even_sum} and your odd sum is{odd_sum}")

    
# print all factor number
# n = int(input("tell your factors number:"))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)


# sum of all factor
# n = int(input("what number factors sum you want:- "))
# s = 0
# for i in range(1,n+1):
#     if n%i ==0:
#       s = s + i 
# print(f"your factors sum is {s}")
    
# a = int(input("tell your value:"))
# b = int(input("tell your exponent:"))
# power = a
# for i in range(b-1):
#     power = power * a
# print(f"After power your answer is {power}")



# n = int(input("enter the number(prime check):"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 1:
#     print("enter the number is a unity number")
# elif count == 0:
#     print("enter the nymber is prime")
# else:
#     print("enter the number is coposite")


# n = int(input("enter the number(prime check):"))
# for i in range(2,n):
#     if n % i == 0:
#         print("sorry your number is composite")
#         break
# else:
#     print("your number is prime")


# nums = [3,1,2,2,2,1,3]
# k = 2
# count = 0
# for i in range(len(nums)):
#     for j in range(i + 1,len(nums)):
#         if nums[i] == nums[j] and(i * j) % k == 0:
#          count +=1
# print(count)

# for i in range(len(nums)):
#    for j  in range(1 + i,len(nums)):
#       if nums[i] == nums[j] and (i*j)% l ==0:
#          count +=1
nums = [4,1,2,3]
odd = nums[1::2]
even =nums[0::2]
odd.sort(reverse = True)
even.sort()
nums[1::2] =odd
nums[0::2] = even
print(nums)

                                                                                                                                                                                       