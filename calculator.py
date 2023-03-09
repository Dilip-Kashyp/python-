A = input("enter value " )
print(" Operators(+,-,*,%, /)" )

operator =input ("Enter operator : " )
B = input("second value ")
A= int(A)
B= int(B)

if operator == "+" :
    print (A + B)
elif operator == "-":
    print(A - B)
elif operator == "*":
    print(A * B)
elif operator == "%":
    print(A % B)
elif operator == "/":
    print(A /B)
    
else:
    print ("invalid  operator" )
    
    