# student result manager 
#using control statements

student={}

while True:
    print("\n-----Welcome to Student Result Manager-----")
    print('''
            1.Add Student
            2.View Students
            3.Check Results
            4.Exit
               ''')

    choice=input("Enter Your Choice:- ")

    #Add Student 
    if choice=="1":
        name=input("Enter Student Name:- ")
        marks=int(input("Enter Student marks: "))
        student[name]=marks
        print(f"{name} successfully added")


    #View Student
    elif choice=="2":
        if not student:
            print("No student found")
        else:
            for name,marks in student.items():
                print(name,":",marks)

    elif choice=="3":
        name=input("Enter student name:- ")
        if name in student:
            marks=student[name]

            if marks>=40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("Student not found")

    elif choice=="4":
        print("Exiting......")
        break

    else:
        print("Invalid Choice")
