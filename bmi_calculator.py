weight=int(input("enter weight in kg: "))
height=float(input("enter height in meters: "))

bmi=round(weight/(height**2))
print(bmi)

if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("healthy")
elif bmi>=25 and bmi<=29.9:
    print("overweight")
elif bmi>=30 and bmi<=39.9:
    print("obesity")
else:
    print("severe obesity")

