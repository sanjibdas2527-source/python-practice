dob={}

print("press 1 to Insert new data")
print("press 2 to Delete existing data")
print("press 3 to Update existing data")
print("press 4 to display all names and DOB")
print("press 5 to Exit")

while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        name=input("Write new name:")
        if name in dob:
            print("Name already exist")
        else:
            date=input("Write DOB in (DD-MM-YYYY):")
            dob[name]=date
            print("Registered Successfully")
    elif ch==2:
        name=input("Enter the name you want to delete:")
        
        if name in dob:
            dob.pop(name,None)
            print("Deleted successfully")
        else:
            print("name not fount")
    elif ch==3:
        name=input("Enter the name:")
        if name in dob:
            dob[name]=input("Enter new DOB:")
            print("Updated successfully")
        else:
            print("Name not found")
    elif ch==4:
        if dob:
            
            for name, date in dob.items():
                print(f"{name} : {date}")
        else:
            print("No records found")

    elif ch == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1–5.")
