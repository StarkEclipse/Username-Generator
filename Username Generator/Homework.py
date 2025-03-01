import random
print("Welcome to my username generator.")

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
Com3 = FirstName + str(Number1)
Com4 = FirstName[0:4] + LastName[-2:]
Choice = [Com1, Com2, Com3, Com4]
Username = random.choice(Choice)
print(Username)


