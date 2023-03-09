num1=int(input("Enter 1st Number "))
num2=int(input("Enter 2nd Number "))
num3=int(input("Enter 3nd Number "))
num4=int(input("Enter 4nd Number "))

if(num1>num4):
    F1=num1
else:
    F1=num4
if(num2>num3):
    F2=num2
else:
    F2=num3
if(F1>F2):
    print (str(F1) +"is Greater" )
else:
    print (str(F2) + " is Greater" )
    