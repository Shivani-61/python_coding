num=int(input("Enter the number:"))
if num==1:
    print("One")
elif num==2:
    print("Two")
elif num==3:
    print("Three")
else:
    print("Wrong input")




height=int(input("What is your height?"))
if height>=3:
    print("You can ride")
    age=int(input("What is your age?"))
    if age<12:
        print("Pay 150 Rs.")
    elif age<=18:
        print("pay 250 Rs.")
    else:
        print("Pay 500 Rs.")
else:
    print("Sorry,you cannot ride")
