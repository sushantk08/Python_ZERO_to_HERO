cp=int(input("enter a number: "))
tax=0

if cp>100000:
    tax=7500+(cp-100000)*0.15
    print(tax)
elif cp<=100000 and cp>50000:
    tax=2500+(cp-50000)*0.10
    print(tax)
elif cp<=50000:
    tax=cp*0.05
    print(tax)