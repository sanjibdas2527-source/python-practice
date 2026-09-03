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

def grade(marks):
    if marks <= 100 and marks >= 90:
        print("Excellent")
        print("Grade = AA")

    elif marks <= 89 and marks >= 80:
        print("Very Good")
        print("Grade = A+")

    elif marks <= 79 and marks >= 70:
        print("Good")
        print("Grade = A")

    elif marks <= 69 and marks >= 60:
        print("Grade = B")

    elif marks <= 59 and marks >= 50:
        print("Grade = C")

    elif marks <= 49 and marks >= 30:
        print("Grade = D")

    else:
        print("Fail")



print("Bengali:")
grade(Ba)

print("English:")
grade(En)

print("Math:")
grade(Math)

print("Physics:")
grade(phy)

print("Chemistry:")
grade(Chem)



print("*************DISPLAY PASS  OR FAIL***************")
if N<=500 and N>=250:
    print("pass")
else:
    print("Fail")    
