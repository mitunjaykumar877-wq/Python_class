
    
# Prime Numbers from 1 to N (10 marks)
# Take a positive integer N as input and print all prime numbers from 1 to N (inclusive).
n = int(input("Enter a positive number: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")
         


#Q3.Strong Number (10 marks)
    
    # Given a non-negative integer, check whether it is a Strong number. 
    # The sum of the factorials of its digits must equal the original number.

# Q4 second largest number

# n = int(input("enter a number"))
# largest = -1
# second_largest = -1
# while n > 0:
#     digit = n % 10
#     if digit > largest:
#        second_largest = largest 
#        largest = digit
#     elif digit > second_largest and digit != largest:
#        second_largest = digit
#     n = n // 10
# print("second largest digit:",second_largest)



# Q3 Armstrong Number
# def arm(n):
#    sum = 0
#    copy=n
#    while n != 0:
#      last = n % 10 #3 ,5,1
#      sum = sum + last**3
#      n = n // 10 
#    if sum == copy:
#        print("it is armstrong")
#    else:
#      print("not armstrong")
#    print(sum)
# arm(153)

n = int(input("Enter a number: "))
original = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")



# n = int(input("Enter a number:"))
# original = 0
# total = 0
# digit = len(str(n))
# while n > 0:
#     digit = n % 10
#     total = total + digit ** digit
#     n = n//10
# if original == total:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")




# Q5. palindrome  

# def check_palindrome(n):
#     original = n
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     if original == reverse:
#         return True
#     else:
#         return False

# num = int(input("Enter the number: "))

# if check_palindrome(num):
#     print("Palindrome")
# else:
#     print("Not palindrome")


# class factory:
#     a = 12 #attribute
#     def hello(): #method
#         print("hpw are you")

# print(factory.a)
# factory.hello()

# print("I am getting intialized")




# class Factory:
#     a = "hello I am an attribut"
#     def hello(s):
#         print("hello I am method")

# obj = Factory() #obj become an object who can access anythin
# obj2 = Factory()

# print(obj.a)
# obj2.hello()


# Q3 Armstrong Number
# def arm(n):
#    sum = 0
#    copy=n
#    while n != 0:
#      last = n % 10 #3 ,5,1
#      sum = sum + last**3
#      n = n // 10 
#    if sum == copy:
#        print("it is armstrong")
#    else:
#      print("not armstrong")
#    print(sum)
# arm(153)

# def arm(n):
#    sum = 0
#    copy = n
#    while n != 0:
#       last = n % 10 #3,5,1
#       sum = sum + last**3
#       n = n//10
#    if sum == copy:
#          print("its is arm")
#    else:
#     print("not arm")
#    print(sum)
# arm(153)
      
# a = int(input("enter the number:"))
# def arm(n):
#    sum = 0
#    copy = n
#    while n!= 0:
#       last =n%10 # 3,5,1
#       sum = sum+last**3
#       n = n//10
#    if sum == copy:
#       print("its arm")
#    else:
#     print("not arm")
#     # print(sum)
# arm(153)      



# present = 0
# absent = 0
# for i in range(7):
#     status = input("Enter the p or a")
#     if status == "p":
#         present += 1
#     elif status == "A":
#         absent += 1
# print("present days:",present)
# print("absent")


# present = 0
# absent = 0
# for i in range(7):
#     status = input("Enter the present or absent")
#     if status == "p":
#         present +=1
#     elif status == "a":
#         absent+= 1
#     elif status == "q":
#         break
#     else:
#         print("please enter p, a, or q")
# print("present days:",present)
# print("absent days:",absent)

# present = 0
# absent = 0
# for i in range(7):
#     status = input("enter the numer:")
#     if status == "p":
#         present +=1
#     elif status == "a":
#         absent+= 1
#     elif status == "q":
#         break
#     else:
#         print("please enter p,a,or,q")
# print("present days",present)
# print("present enter",absent)


# Science = int(input("First subject is science"))
# math  = int(input("First subject is math"))
# if Science >=33:
#    print("science: Pass")
# else:
#     print("science: Fail")
# if math >= 33:
#      print("Math: Pass")
# else:
#      print("Math: Fail")


# sci = int(input("first sub is sci"))
# math = int(input("first sub is math"))
# if sci >=33:
#     print("sci: Pass")
# else:
#     print("sci: fail")
# if math >=33:
#     print("math: Pass")
# else:
#     print("math: fail")



# nums = [6,6,5,4,5,1]
# count = 0
# nums = [nums[0]] + [nums[i]
# for i in range(1,len(nums))
#     if nums[i]!= nums[i-1]]
# for i in range(1,len(nums)-1):
#     if nums[i]> nums[i-1] and nums[i]>nums[i+1]:
#         count +=1
#     elif nums[i]< nums[i-1] and nums[i]< nums[i+1]:
#         count +=1
# print(count) 
        

# nums = [6,3,4,2,4]
# count = 0
# nums = [nums[0]] + [nums[i]
# for i in range(1,len(nums))
#     if nums[i]!= nums[i-1]]
# for i in range(1,len(nums)-1):
#    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
#       count +=1
#    elif nums[i]< nums[i-1] and nums[i]< nums[i+1]:
#      count +=1
# print(count)


# def check_palindrome(n):
#     original = n
#     reverse = 0
#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10
#     if original == reverse:
#         return True
#     else:
#         return False
# num = int(input("Enter the number: "))
# if check_palindrome(num):
#     print("Palindrome")
# else:
#     print("Not palindrome")


# def check_palindrome(n):
#     original = 0
#     reverse = 0
#     while n> 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n //10
#     if original == reverse:
#         return True
#     else:
#         return False
# num = int(input("Enter the number:"))
# if check_palindrome(num):
#     print("Palindrome")
# else:
#     print("not palindromr")



# # Q4 second largest number

# # n = int(input("enter a number"))
# # largest = -1
# # second_largest = -1
# # while n > 0:
# #     digit = n % 10
# #     if digit > largest:
# #        second_largest = largest 
# #        largest = digit
# #     elif digit > second_largest and digit != largest:
# #        second_largest = digit
# #     n = n // 10
# # print("second largest digit:",second_largest)

# # n = int(input("enter a number"))
# # largest = -1
# # second_largest = -1
# # while n>0:
# #     digit = n % 10
# #     if digit > largest:
# #         second_largest = largest
# #         largest = digit
# #     elif digit > second_largest and digit != largest:
# #         second_largest = digit
# #     n = n // 10
# # print("second largest digit:",second_largest)


# for n in range(2, 101):
#     count = 0

#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
        # print(n, end=" ")


# def check_vote(n):
#      if n >18:
#           return "Eligible"
#      else:
#           return "not eligible"
# n = int(input("enter a number:"))
# print(check_vote(n))


# n = int(input("enter the age:"))
# if n > 18:
#     print("vot eligivle")
# # else:
#     print("not vote eligible")



# def check_palindrome(n):
#     original = n
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     if original == reverse:
#         return True
#     else:
#         return False

# num = int(input("Enter the number: "))

# if check_palindrome(num):
#     print("Palindrome")
# else:
#     print("Not palindrome")

n = int(input("Enter the number: "))
original = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

        
