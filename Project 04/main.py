# Rent calculator

rent=int(input("Enter your hostel / flat rent:- "))
food=int(input("Enter amount of food orderd :-" ))
electricity_spend=int(input("Enter the total of electercity spend:- "))
charge_per_unit=int(input("Enter charge per unit :- "))
persons=int(input("Enter the nimber of persons living in room/flat:- "))

total_bill=electricity_spend * charge_per_unit

output=(food+rent+total_bill)//persons

print(f"Each persons will pay :-{output}")

               