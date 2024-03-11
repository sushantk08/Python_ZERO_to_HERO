size=input("Enter which size of pizza do you want (S/M/L)?")
sum=0
if size=="s" or size=="S":
    sum+=100
    print("Small Pizza Price is 100 Rs.")
elif size=="m" or size=="M":
    sum+=200
    print("Medium Pizza Price is 200 Rs.")
elif size=="l" or size=="L":
    sum+=300
    print("Large Pizza Price is 300 Rs.")
else:
    print("plz enter valid pizza size")

pepporoni=input("do you want to add pepporoni (Y/N)?")
if pepporoni=="Y" or pepporoni=="y":
    if size == "s" or size == "S":
        sum+=30
    else:
        sum+=50

cheese=input("do you want to add extra cheese (Y/N)?")
if cheese=="Y"or cheese=="y":
    sum+=20
print(f"your total bill is {sum} Rs.")



