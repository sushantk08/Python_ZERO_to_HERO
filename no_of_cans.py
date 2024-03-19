from math import *
def no_of_cans(h,w,coverage):
    cans=(h*w)/coverage
    return ceil(cans)




h=int(input("enter height of a wall: "))
w=int(input("enter width of a wall: "))
coverage=7

print(no_of_cans(h,w,coverage))