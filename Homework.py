import random
print("Welcome to my username generator.")
while True:
    Name = input("Enter your full name:")
    NameParts = Name.split()

    if len(NameParts) < 2:
        Name = input("Enter the name again.")
        NameParts = Name.split()

    FirstName = NameParts[0]
    LastName = NameParts[-1]

    Com1 = FirstName + LastName
    Com2 = LastName + FirstName
    Number1 = random.randint(1,10)
    Number2 = random.randint(1,9999)
    Number3 = random.randint(100,999)
    Number4 = random.randint(10,99)
    Com3 = FirstName + str(Number1)
    Com4 = FirstName[0:4] + LastName[-2:]
    Com5 = FirstName + "_" + LastName  
    Com6 = LastName + "." + FirstName  
    Com7 = FirstName + str(Number4)
    Com8 = LastName + "#" + str(Number3)
    Com9 = FirstName[0] + "_" + LastName + str(Number1)
    Com10 = FirstName[:3] + "~" + LastName[-3:] + "!" 
    Com11 = FirstName + "$" + str(Number2) 
    Com12 = FirstName[0:2] + "*" + LastName[-2:] + str(Number1)
    Choice = [Com1, Com2, Com3, Com4, Com5, Com6, Com7, Com8, Com9, Com10, Com11, Com12]
    Username = random.choice(Choice)

    response = input(f"{Username}\nDo you like this username? (yes/no)").lower()

    if response == "yes":
        print("Nice! Glad you like it.")
        break

    if response == "no":
        print(f"Try again,", {Name})

    else:
        print("Please answer with 'yes' or 'no'.")






