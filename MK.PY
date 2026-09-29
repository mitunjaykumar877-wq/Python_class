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



a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

if a == b and b == c and a == c:
      print("all are eqyal")
elif a == b or b == c or a == c:
       print("any two number are equal")
else:
       print("all are different")

# age = int(input("enter age"))
# if age <=5 and age <=17:
#        print("tikat price free")
# elif age>=18 and age <=59:
#      print("price is 100")
# elif age>=18 and age<=59:
#       print("price is 200")
# elif age<60:
#       print("price is 200")
# else:
#       print("price is 120")


 


num = int(input("enter the number"))
if num>0:
       print("num is +")
       if num>=10:
              print("and num>10")
       else:
              print("and num<10")
else:
       print("num is -")


       num = int(input("enter the number"))
       if num%2==0:
              if num%4==0:
                     print("num is even and not div by 4")
              else:
                     print("num is even and not div by 4")
       else:
              print("num is odd")


              pin = int(input("enter the pin"))
              if pin ==1234:
                     amount = int(input("enter the amount to withdraw"))
                     if amount <=5000:
                            print("withdraw done")
                     else:
                            print("garib ho aap")
              else:
                     print("chor ho aap") 


num = int(input("enter the num"))
if num>0:
       # print("num is +",end="")
       if num%2==0:
              if num%4==0:
                     print("+ and even and div by 4")
              else:
                     print("+ and even and not div by 4")
       else:
              print("and odd")
else:
       print("and odd")