# list...                             
# a=[10,'MITUNJAY',43.3]                  
# print(type(a))

# # tuple....
# a=(10,'mk',98.3)
# print(type(a))

# # set
# a={12,'yadav',239}
# print(type(a))

# # dict
# a={'age':21}
# print(type(a))
# print(a.get('age'))


# var=eval(input("enter data:"))
# print(type(var))



# print("Hello","Mk","Dk",sep="_")

# print("Hello",end="\n\n")
# print("world")

# user_input = int(input("enter a number :" ))

# if user_input % 2 == 0:
#     print("number is even")
# else :
#     print("number is odd")


# age = int(input("enter a number :" ))
# if age <18:
#     print('you are too young to marry')
# elif age>60:
#     print('you are too old for marry')
# else:
#     print("we will find a perfect match for you")

# what is thread:

# Thread is a predefine class which is available in 
# threading module
# run multiple rask as same time
# with out earch other thread.

# Thread class method:
# 1) run() 2) start() 3) join() 4)isAlive() 
# 5)setname() 6)getname()

# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(3):
#             print("yadav ji")
#             sleep(1)

# class B(Thread):
#     def run(self):
#         for i in range(3):
#             print("mitunjay")
#             sleep(1)

# t1=A()
# t2=B()

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print("aman")







# math = (input("enter the subject:"))
# science = (input("enter the sunject:"))
# English = (input("enter the subject"))
# if maths>=40 and eng>=40 and science>=40



# a = int(input("enter the number"))
# b = int(input("enter the number"))
# c = int(input("enter the number"))

# if a == b and b == c and a == c:
#       print("all are eqyal")
# elif a == b or b == c or a == c:
#        print("any two number are equal")
# else:
#        print("all are different")

# # age = int(input("enter age"))
# # if age <=5 and age <=17:
# #        print("tikat price free")
# # elif age>=18 and age <=59:
# #      print("price is 100")
# # elif age>=18 and age<=59:
# #       print("price is 200")
# # elif age<60:
# #       print("price is 200")
# # else:
# #       print("price is 120")


 


# num = int(input("enter the number"))
# if num>0:
#        print("num is +")
#        if num>=10:
#               print("and num>10")
#        else:
#               print("and num<10")
# else:
#        print("num is -")


#        num = int(input("enter the number"))
#        if num%2==0:
#               if num%4==0:
#                      print("num is even and not div by 4")
#               else:
#                      print("num is even and not div by 4")
#        else:
#               print("num is odd")


#               pin = int(input("enter the pin"))
#               if pin ==1234:
#                      amount = int(input("enter the amount to withdraw"))
#                      if amount <=5000:
#                             print("withdraw done")
#                      else:
#                             print("garib ho aap")
#               else:
#                      print("chor ho aap") 


# num = int(input("enter the num"))
# if num>0:
#        # print("num is +",end="")
#        if num%2==0:
#               if num%4==0:
#                      print("+ and even and div by 4")
#               else:
#                      print("+ and even and not div by 4")
#        else:
#               print("and odd")
# else:
#        print("and odd")



# 1 se 50 tak print karna hai while loop
# i = 1
# while i <= 50:
#     print(i)
#     i = 1 + i

# i = 1
# while i <= 40:
#    print(i)
#    i = 1 + i

# i = 10
# while i >= 1:
#    print(i)
#    i = i - 1


# password = "90555"
# while password != "90555":
#        password = input("enter password")
#        print("access granted")

# PRACTICE QUESTION

# n = int(input("enter the number"))
# count = 0
# for i in range(1, n + 1):
#        if i % 3 ==0 and i%5==0:
#               count+=1
#               print(f"count :{count}")

# FACRORIAL

# n = int(input("enter the number"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*1
# print(f"{n}! is {n}fact)")


# n = int(input("enter a number"))
# temp = n
# sum = 0
# while n >0:
#     digit = n%1
#     fact_of_digit = 1
#     for i in range(1,digit+1):
#       fact*=i
#       sum+=fact_
#     n = n//10
#     if temp == sum:
#        print("strong number")
#     else:
#        print("not a strong number")

# n  = int(input("enter  a number:- "))
# sum = 0
# for i  in range(1,n+1):
#     if i%2 !=0:
#         sum +=i
# print(sum)

# a = float(input("please tell the first number:"))
# b = float(input("please rell the second number:"))

# if a>b:
#     print(f"{a} is greater than{b}")
# elif b>a:
#     print(f"{b} is greater than{a}")
# else:
#     print(f"{a} is equal to {b}")

# gen = input("please tell your gender in character(m,f):-")
# if gen == 'm':
#     print("hello sir how are you")
# else:
#     print("hello maam how are you")


# gen = input("please tell your gender in character(m,f):-")
# if gen == 'm' or gen == "M":
#     print("hello sir how are you")
# elif gen == "F" or gen == "f":
#     print("hello maam how are you")
# else:
#     print("wrong input only provide m or f")

# a = int(input("enter the number"))
# if a%2== 0:
#     print("your number is even")
# else:
#     print("your number is odd")



# name = input("please tell your name:")
# age = int(input("please tell your age:"))
# if age >= 18:
#     print(f"Hello {name} you can vote")
# else:
#     print(f"Hello{name} sorry you can vote after{18-age} year")



# a = int(input("please tell you day(1-7):-"))
# if a == 1:
#     print("Monday it is")
# elif a == 2:
#       print("Tuesday it is")
# elif a == 3:
#        print("wednesday it is")
# elif a == 4:
#       print("thursday it is")
# elif a == 5:
#       print("friday it is")
# elif a == 6:
#        print("saturday it is")
# elif a == 7:
#         print("sunday it is")
# else:
#        print("sorry your inpur is wrong")


# a =int(input("please tell your number:- "))
# b =int(input("please tell your number:- "))
# c =int(input("please tell your number:- "))

# if a== b and b == c:
#     print("all the number are equal")
# elif a == b or b == c or c==a:
#     print("any two numbers are equal")
# elif a>b and a>c:
#     print(f"{a} is the greatest number")
# elif b > a and b> c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")\


# Question 8
# year = int(input("please tell your tear:"))
# if year % 100 == 0 and year %400 == 0:
#     print("its a leap year")
# elif year%100 != 0 and year % 4 == 0:
#     print("its a leap year")
# else:
#     print("sorry its not a leap year ")


# bill = int(input("please tell your total amount"))
# if bill >= 1000 and bill<= 4999:
#     print(f"you get a discount of 10% your final amount is {(bill *90)/100}")

# elif bill >= 5000:
#         print(f"you get a discount of 10% your final amount is {(bill *80)/100}")
# else:
#      print("sorry no discount for you")



# char = input("please tell you Alphabet:")
# if char in "aeiouAEIOU":
#     print("its a vowel")
# else:
#     print("its consonent")
    
# for i in range(20):
#     print("hello i am mitunjay")
