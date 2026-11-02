#  how functions  are created 
# inbuild

# user defined functions

# defining a function
# def hello():
# print("how are you")

    # calling a function
    # hello()

    # def hey():
        # return "how are you" return the value to the calling block 

    # a = hey() calling block captures the value 
    # print(a)

    # parameters and Arguments
    # def addition (a,b): you accept the parameters
    # print(a + b)
    # def addition(a,b): # and the provide the arguments to the parameters
        # hello(50,50 )

# def palindrome(a):
#  rev = 0
#  copy = a
# while a != 0:
#  rev = rev * 10 + a%10
#  a = a//10
#  if copy == rev:
#    print(copy)

# for i in range(1,1000):
#  palindrome(i)

# parameters and arguments
# default parameters

# def hello (a,b,c,d,e=30):
#     print(a + b)

    # hello(50,50,20,56)

# default arguments
# def information(name, age, number)
# print("hello your info is")
# print(name)
# print(age)
# print(number)

# information(number = 8776655,name = "harsh", age 25)


# print number from 1 - 30.
# you cannot use for and while loop.
# you cannot uses print satement more than 1.

# recursion - a function calling function itself 
def numbers(n):
    if n ==999:
       return
       print(n)
       numbers(n+1)
numbers(1)

def numbers(n):
    if n ==999:
       return
    numbers(n+1)
    print(n)
    
numbers(1)



