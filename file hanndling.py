
# mkdir -> to create a new folder/directory.
# rmdir -> to remove any folder/directory.
# Files.
# x -> This mode will only create the file and if already exists we will get an error back.
# w -> Agr file exist nahi kar rahi hai so mode will be create and insert the content inside the file.  
# a -> add text at the last.
# r -> 
# Mode 1: x
# open("Garba.txt","x")

# Mode 2: w -> if there is any content inside the file so the new one will replce the old one.
# file = open("Garba.txt","w")
# file.write("khelo garba khub khelo din raat khelo")
# file.write("Enjoy karo job hi job hai")

# Mode 3: a -> add text at the last.
# file = open("Garba.txt","a")
# file.write("\nThis message is newly added")

# Mode 4: r -> read the content inside of the file.
# file=open("Garba.txt","r")
# print(file.read())
# file.close()


# import os
# os.mkdir("Hello")
# os.rmdir("Hello")

# with open("sample.txt","w") as file:
#     file.write("This is new file.")

# CRUD - CREATE , READ , UPDATE  , DELETE.
# os.remove("Garba.txt")


 