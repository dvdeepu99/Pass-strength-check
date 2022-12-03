import string

pwd = input("Enter your password: ")
flag = bool(True)

if not any(x.isupper() for x in pwd):
  flag = False
  print("Uppercase not found.")

if not any(x.islower() for x in pwd):
  flag = False
  print("Lowercase not found.")

if not any(x.isnumeric() for x in pwd):
  flag = False
  print("Numeric digit not found.")

if not any(c in string.punctuation for c in pwd):
  flag = False
  print("Special character not found.")

if (len(pwd)) < 12:
  flag = False
  print("Password length is too weak.")

with open('blacklist.txt') as texts:
  if pwd in texts.read():
    print('String is in the blacklist')
    flag = False

if flag:
  print("The password meets the criteria!")
else:
  print("Since the password doesn't meet in at least one of the", end='')
  print(" above mentioned criterion, you should probably change it.")
