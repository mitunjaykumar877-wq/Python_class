# from cryptography.fernet import fernet
master_pwd = input("What is the master password")
def view():
   pass


# def write_key():
#    key = fernet.generate_key()
#    with open("key.key","wb") as key_file:
#        key_file.write(key)

#  def load_key():
#    file = open("key.key", "rb")
#    key = file.read()
#    file.close()
#    return key


# master_pwd = input("What is the master password ")
# key = load_key() + master_pwd.bytes
# fer = fernet(key)


# def write_key():
#    key = fernet.generate_key()
#    with open("key.key","wb")as key_file:
#        key_file.write(key)

# def load_key():
#    file = open("key.key", "rb")
#    key = file.read()
#    file.close()
#    return key


def view():
   with open('password.txt', 'r') as f:
      for line in f.readlines():
         # print(line.rstrip())
         data =line.rstrip()
         user, passw = data.split("|")
         print("user:", user, "Password:",passw)
         # print("user:", user,"|password:", str(fer.encrypt(passw.encode())))


def add():
   name = input('Account Name: ')
   pwd = input("password: ")

   with open('password.txt', 'a') as f:
      f.write(name + "|" + pwd + "\n")
      # f.write(name + "|" +str(fer.encrypt(pwd.encode())) + "\n")

while True:
   mode = input("Would you like to add a new password of view existing ones(view, add), press q to quit ? ")
   if mode == "q":
      break
   if mode == "view":
       view()
   elif mode == "add":
       add()
   else:
      print("Invalid mode.")
      continue

 