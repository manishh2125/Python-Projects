choice=input("What would you like to have? espresso, latte, or cappuccino :\n").lower()
guess=choice
espresso={'water':50,'coffee':18,'milk':0,'cost':2.5}
latte={'water':200,'coffee':24,'milk':150,'cost':4.0}
cappuccino={'water':250,'coffee':24,'milk':100,'cost':5.0}

if choice=='espresso':
    costof=2.5
elif choice=='latte':
    costof=4.0
else:
    costof=5.0

resourcess={'water':500,'coffee':100,'milk':250}

if choice=='espresso':
    if resourcess['water']>espresso["water"] and resourcess['milk']>espresso["milk"] and resourcess['coffee']>espresso["coffee"]:
        print("We can make one for you.. Please wait!\n")
    else:
        print("Sorry but there is not enough incredients..")
elif choice=='latte':
    if resourcess['water']>latte["water"] and resourcess['milk']>latte["milk"] and resourcess['coffee']>latte["coffee"]:
        print("We can make one for you.. Please wait!\n")
    else:
        print("Sorry but there is not enough incredients..")
else:
    if resourcess['water']>cappuccino["water"] and resourcess['milk']>cappuccino["milk"] and resourcess['coffee']>cappuccino["coffee"]:
        print("We can make one for you.. Please wait!\n")
    else:
        print("Sorry but there is not enough incredients..")

print("Please insert the coins in the machine:\n")
quarters=float(input("insert the quarters:"))
dimes=float(input("insert the dimes:"))
nickels=float(input("enter the nickels: "))
pennies=float(input("insert the pennies: "))

total_amount= 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies

if total_amount < costof:
    print("You don't have enough money..\n")
else:
    change= total_amount-costof
    change=round(change,2)
    print(f"Here is your change {change} dollars.")
    print(f"And here is your Coffee! Thank you for the wait.")
