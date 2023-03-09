marks=int(input("Enter Your marks \n"))
if marks>90 :
    grade= " Excellent"
elif marks>80:
    grade="A"
elif marks>60:
    grade="B"
elif marks>40:
    grade="C"
elif marks>20:
    grade="D"
elif marks<20:
    grade="Fail"
    
print ("Your Grade Is :" + grade )