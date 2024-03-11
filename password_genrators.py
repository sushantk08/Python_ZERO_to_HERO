from random import *

print("Welcome To Password Generator!!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*','+']

n_letters=int(input("How Many Letters Do You Want? \n"))
n_symbols=int(input("How Many Symbols Do You Want? \n"))
n_numbers=int(input("How Many Numbers Do You Want? \n"))


password=[]

for i in range(1,n_letters+1):
    char=choice(letters)
    password += char
for j in range(1,n_symbols+1):
    sym=choice(symbols)
    password += sym
for k in range(1,n_numbers+1):
    num=choice(numbers)
    password += num

shuffle(password)
password_str=""
for char in password:
    password_str +=char
print(password_str)
