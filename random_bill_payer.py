import random

persons=input("enter person names: ")
lst=persons.split(",")
a=random.randint(0,len(lst))
print(f"{lst[a]} will pay the entire bill")