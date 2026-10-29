
# Project under building Completing soon......
# Expense tracker
# due to acadamic exams 

transactions=[]
categories = {
    1: "Food",
    2: "Travel",
    3: "Shopping",
    4: "Education",
    5: "Healthcare",
    6: "Bills",
    7: "Entertainment",
    8: "Mobile & Recharge",
    9: "Personal Care",
    10: "Rent & Housing",
    11: "Savings",
    12: "Bank Charges",
    13: "Gifts & Donations",
    14: "Others"
}

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
        Expense=int(input("Enter amt to you spend:- "))
        print("Select Category")
        print(
    "Food\n"
    "Travel\n"
    "Shopping\n"
    "Education\n"
    "Healthcare\n"
    "Bills\n"
    "Entertainment\n"
    "Mobile & Recharge\n"
    "Personal Care\n"
    "Rent & Housing\n"
    "Savings\n"
    "Bank Charges\n"
    "Gifts & Donations\n"
    "Others\n"
)
          cate=input("Enter Category:- ").title()
        Budget=Budget-Expense
        categories=categories.get(cate,0)+Expense
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


