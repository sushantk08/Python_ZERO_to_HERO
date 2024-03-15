nested_lst=[(i,i**2,i**3) for i in range(1,4)]
lst1=[ j for lst in nested_lst for j in lst ]
print(lst1)