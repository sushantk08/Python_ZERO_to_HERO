height=(input("Enter a input: "))
lst=height.split(",")
sum=0
counter=0

for i in lst:
    sum=sum+int(i)
    counter=counter+1
avg=sum//counter

print(avg)