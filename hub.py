x=int(input("enter the number:"))
y=x%3
z=x%5
if(y==0 and z==0):
    print(x,"is divisible both 3 & 5")
else:
    print(x,"is not divisible")

