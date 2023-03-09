import random


def gamewin(computer, you):
    if computer == you:
        return None
    elif computer == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
    elif computer == 'w':
        if you =='g':
            return False
        elif you == 's':
            return True 
    elif computer == 'g':
        if you =='s':
            return False
        elif you == 'w':
            return True  
  
randno=random.randint(1,3)
if randno==1:
    computer ='s'
elif randno==2:
    computer ='w'
elif randno==3:
    computer='g'
    
print("Computer Turn : Snake (s), Water (w),Gun(g)")

you=input(" Your Turn : Snake (s), Water (w),Gun(g) \n")

a=gamewin(computer , you)
if a ==None :
    print("Game is tie")
elif a:
    print ("You Win")
else:
    print ("You Loose ")
print (f" Computer choose: {computer}")
print(f"You choose : {you}")