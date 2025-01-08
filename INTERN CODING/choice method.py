import random
names=input("Enter everybody's name selected by comma:")
names_list=names.split(",")
person_selected=random.choice(names_list)
print(f"{person_selected} will pay the bill")
