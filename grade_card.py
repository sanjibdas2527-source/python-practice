print("***********************GRADE CARD*************************")




print("*********************ENTER YOUR MARK************************")
Ba=int(input("Enter the Bangali mark :"))
En=int(input("Enter the English  mark :"))
Math=int(input("Enter the Mathematics mark :"))
phy=int(input("Enter the physics mark :"))
Chem=int(input("Enter the Chemistry mark :"))




print("**********************TOTAL MARK***********************")
N=Ba+En+Math+phy+Chem
print("Total mark=",N)




print("***********************PARCENTAGE*************************")

MaxMark=int(input("Enter your total Maximum Mark:"))
parcen=(N/MaxMark)*100
print("Parcentage=",parcen,"%")



print("*******************SUBJECT GRADE******************************")



if (Ba<=100 and Ba>=90):
    print("Excellent")
    print("Grade= AA")
elif Ba<=89 and Ba>=80:
    print("Very Good")
    print("Grade=A+")
elif Ba<=79 and Ba>=70:
    print("Good")
    print("Grade=A")
elif Ba<=69 and Ba>=60:
    print("Grade=B")  
elif Ba<=59 and Ba>=50:
    print("Grade=C")
elif Ba<=49 and Ba>=30:
    print("Grade=D")
else:
    print("Fail")                      

if (En<=100 and En>=90):
    print("Excellent")
    print("Grade= AA")
elif En<=89 and En>=80:
    print("Very Good")
    print("Grade=A+")
elif En<=79 and En>=70:
    print("Good")
    print("Grade=A")
elif En<=69 and En>=60:
    print("Grade=B")  
elif En<=59 and En>=50:
    print("Grade=C")
elif En<=49 and En>=30:
    print("Grade=D")
else:
    print("Fail")                      

if (Math<=100 and Math>=90):
    print("Excellent")
    print("Grade= AA")
elif Math<=89 and Math>=80:
    print("Very Good")
    print("Grade=A+")
elif Math<=79 and Math>=70:
    print("Good")
    print("Grade=A")
elif Math<=69 and Math>=60:
    print("Grade=B")  
elif Math<=59 and Math>=50:
    print("Grade=C")
elif Math<=49 and Math>=30:
    print("Grade=D")
else:
    print("Fail")                      

if (phy<=100 and phy>=90):
    print("Excellent")
    print("Grade= AA")
elif phy<=89 and phy>=80:
    print("Very Good")
    print("Grade=A+")
elif phy<=79 and phy>=70:
    print("Good")
    print("Grade=A")
elif phy<=69 and phy>=60:
    print("Grade=B")  
elif phy<=59 and phy>=50:
    print("Grade=C")
elif phy<=49 and phy>=30:
    print("Grade=D")
else:
    print("Fail")                      

if (Chem<=100 and Chem>=90):
    print("Excellent")
    print("Grade= AA")
elif Chem<=89 and Chem>=80:
    print("Very Good")
    print("Grade=A+")
elif Chem<=79 and Chem>=70:
    print("Good")
    print("Grade=A")
elif Chem<=69 and Chem>=60:
    print("Grade=B")  
elif Chem<=59 and Chem>=50:
    print("Grade=C")
elif Chem<=49 and Chem>=30:
    print("Grade=D")
else:
    print("Fail")       



print("*************DISPLay PASS  OR FAIL***************")
if N<=500 and N>=320:
    print("pass")
else:
    print("Fail")    
