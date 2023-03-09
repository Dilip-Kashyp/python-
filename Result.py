sub1=int(input("Enter Math Marks\n"))
sub2=int(input("Enter English Marks\n"))
sub3=int(input("Enter Computer Marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print ("Result: fail" )
in
 
elif(sub1+sub2+sub3)/3 < 40:
    print (" Result:Fail" )
else:
    print ("Result: Pass")