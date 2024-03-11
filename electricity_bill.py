units=int(input("enter units of electricity used: "))
amt=0

if units<=100:
    amt=0
    print(amt)
elif units>100 and units<=200:
    amt=(units-100)*5
    print(amt)
elif units>200:
    amt=500+(units-200)*10
    print(amt)