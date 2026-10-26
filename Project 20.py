
# Project under building Completing soon......
# Expense tracker


transactions=[]
Category=[]

while True:
    print("1.Add budget")
    print("2.Add Expense")
    print("3.Show transactions")
    print("4.Delete Expense")
    print("5.Check balance")

    user=input("Enter your choice:- ")

    if user=="1":
        Budget=int(input("Enter total Budget:- "))

    elif user=="2":
        note=input("Enter Note:- ")
        Expense=int(input("Enter amt to you spend:- "))
        Budget=Budget-Expense
        Category.append(note)
        transactions.append(Expense)

    elif user=="3":
        print(note)
        print(transactions)

    elif user=="4":
        del_transcation=int(input("Enter transaction to delete :- "))
        if del_transcation in Category:
            del del_transcation
            del_transcation+=Budget

    elif user=="5":
        print(Budget)



    else:
        print("Invalid Choice")


