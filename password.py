import  string
import random 
A=string.ascii_uppercase #A to Z
a=string.ascii_lowercase #a to z
n=string.digits #0 to 9
p=string.punctuation # all symbols 
length=int(input("Enter Password Length\n" ))
P=[]
P.extend(list(A))
P.extend(list(a))    
P.extend(list(n))
P.extend(list(p))
random. shuffle(P) 

print ("Your Password is:  ")

print("".join(P[0:length]))