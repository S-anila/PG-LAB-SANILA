n=str(input("enter the string"))
print("the string is",n)
if(n.endswith("lng")):
 n=n+'ly'
else:
  n=n+'ing'
print("the formated string is",n)