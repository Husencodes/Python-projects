#Currency converter Indian rupees to other country 
with open('currency.txt') as f:
    lines=f.readlines()


currencyDict={}
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]

amount=int(input("Enter amount:\n"))
print("Enter currency name to convert in available options")
[print(item) for item in currencyDict.keys()]
currency=input=input("Enter values:- \n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")