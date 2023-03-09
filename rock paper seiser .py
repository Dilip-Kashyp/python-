import random


def gamewin(computer, you):
    if computer == you:
        return None
    elif computer == 'r':
        if you =='s':
            return False
        elif you == 'p':
            return True
    elif computer == 'p':
        if you =='r':
            return False
        elif you == 's':
            return True 
    elif computer == 's':
        if you =='p':
            return False
        elif you == 'r':
            return True  
  
randno=random.randint(1,3)
if randno==1:
    computer ='r'
elif randno==2:
    computer ='p'
elif randno==3:
    computer='s'
    
print("Computer Turn : Rock (r), Paper(p), scissors (s)")

you=input(" Your Turn :  Rock (r), Paper(p), scissors (s) \n")


    
print (f" Computer choose: {computer}")
print(f"You choose : {you}")
a=gamewin(computer , you)
if a ==None :
    print("Game is tie")
elif a:
    print ("You Win")
else:
    print ("You Loose ")