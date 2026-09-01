
while True:

    print("=======================")
    print("1.Add\n2.Substract\n3.Multiply\n4.Division\n5.Exit")
    n=int(input("Enter your choice:"))
    print("=======================")
    if n==1:
        a=int(input("Enter Your First Number:"))
        b=int(input("Enter Your Second Number:"))
        print("=======================")
        print("Sum is:",a+b)
        print("=======================")
    elif n==2:
        a=int(input("Enter Your First Number:"))
        b=int(input("Enter Your Second Number:"))
        print("=======================")
        print("Sub is:",a-b)
        print("=======================")
    elif n==3:
        a=int(input("Enter Your First Number:"))
        b=int(input("Enter Your Second Number:"))
        print("=======================")
        print("Mul is:",a*b)
        print("=======================")
    elif n==4:
        a=int(input("Enter Your First Number:"))
        b=int(input("Enter Your Second Number:"))
        print("=======================")
        print("Div is:",a/b)
        print("=======================")
    else:
        print("=======================")
        print("Good Bye")
        print("=======================")
        break
