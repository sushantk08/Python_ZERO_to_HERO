numbers=input('enter numbers: ')
lst=numbers.split(",")
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
max=lst[0]
for j in lst:
    if j>max:
        max=j
print(max)
