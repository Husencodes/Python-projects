# Library Management

books={'c programming':400,
       'python':250,
       'dsa':900,
       'c#':150,
       'c++':250,
       'logic building':150,
       'java':150
       }

borrow_books=[]

while True:
    print("-----Welcome to tech library-----")
    print("1.Show books")
    print("2.Borrowing Book")
    print("3.Purchase Book")
    print("4.Returning Book")
    print("5.Exit")

    user=input("Enter your choice:- ")

    # 1.Show books
    if user=="1":
        print("Available books with price",books)

    #2.Borrow books
    elif user=="2":
        borrow_book=input("Which book you want read ? :- ").lower()
        if borrow_book in books:
            if borrow_book in borrow_books:
                            print(f"{borrow_book} is already taken")
            elif borrow_book  not in  borrow_books:
                borrow_books.append(borrow_book)
                print(f"{borrow_book} is available and read freely and return properly")
                                 
        else:
            print(f"{borrow_book} is not available")

    #3.Purchase book
    elif user=="3":
        purchase_book=input("Which book you want purchase:- ").lower()
        if purchase_book in books:
             print(f"{purchase_book} is available and pay {books[purchase_book]} to purchase (yes/no)")
             pay=input( )
             if pay=='yes':
                 print("Purchased successfully")
             else:
                 print("Thanks visit again")
        else:
            print(f"{purchase_book} is not available")

    #Returning book
    elif user=='4':
        return_book=input("Which book you returning:- ").lower()
        if return_book in borrow_books:
            borrow_books.remove(return_book)
            print("Thanks returning our book properly")

        else:
            print(f"{return_book}  book wasn't borrowed from your library.")

    #exiting
    elif user=='5':
        print("Exiting......")
        break


    else:
        print("Invalid choice")
       
