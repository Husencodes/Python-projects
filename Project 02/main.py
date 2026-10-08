# Shopping Bill Calculator
import random
sum=0
discount=random.choice([25,50,100,150,200])
while(True):
    userInput=int(input("Enter Item price or click 1 to know your discount or click 0 to exit:-  "))
    if(userInput!=0):
        sum=sum+userInput
        print(f"total so far :- {sum}")
       
    
    elif(userInput!=00 and sum>200):
        print(f"Your discount is {discount}")
    
    else:
        print(f"Your total bill is {sum} \npayable amt :- {abs(sum-discount)} \nThankyou for shopping ,visit again!")
        break
    
        
