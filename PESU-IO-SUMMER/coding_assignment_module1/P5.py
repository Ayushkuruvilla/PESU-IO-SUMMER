data=input("Enter the string")
try:
 num=int(data)
 print("It is an integer")
except ValueError:
 print("It is a string")
