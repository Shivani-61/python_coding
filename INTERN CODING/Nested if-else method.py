height=int(input("What is your height?"))
if height>=3:
    print("You can ride")
    age=int(input("What is your age?"))
    if age<=18:
        print("Pay 250 Rs.")
    else:
        print("Pay 500 Rs.")
else:
    print("Sorry,you cannot ride")
