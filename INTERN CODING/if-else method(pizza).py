size = input("What size pizza you want(S/M/L)?")
bill = 0
if size == 'S' or size == 's':
    bill+=100
    print("Small pizza price is 100")
elif size == 'M' or size == 'm':
    bill+=200
    print("Medium pizza price is 200")
else:
    bill+=300
    print("Large pizza price is 300")
add_pepperoni = input("Do you want pepperoni(Y/N)?")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    print("you have selected pepperoni")
    if size == 'S' or size == 's':
        bill+=30
    else:
        bill+=40
extra_cheese = input("Do you want extra cheese(Y/N)?")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill+=20
print(f"Your finall bill is {bill}")
