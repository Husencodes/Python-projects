def task():
    tasks=[]#empty list
    print("-----Welcome to To=do App-----")

    total_task=int(input("Enter Number of tasks:- "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} ")
        tasks.append(task_name)
    print("Tasks added successfully")
    print(f"Todays tasks are:- {tasks}")

    while True:
        operation=int(input("1.Add\n2.Upadate\n3.Delete\n4.View\n5.Exit\n"))
        if operation==1:
            add=input("Enter new task:-")
            tasks.append(add)
            print(f"Task {add} added successfully")

        elif operation==2:
            updated_val=input("Enter task to update:- ")
            if updated_val in tasks:
                up=input("Enter new task:- ")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task{up}")

        elif operation==3:
            del_val=input("Enter task to delete:- ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} is deleted successfully")

        elif operation==4:
            print(f"Total tasks {tasks}")

        elif operation==5:
            print("closing the program.......")
            break

        else:
            print("Invalid input")

task()