import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("password generator in a easy way")
password_list = ""
for x in range(1,nr_letters+1):
    password_list += random.choice(letters)
for y in range(1,nr_numbers+1):
    password_list += random.choice(numbers)
for z in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

print(password_list)
password_list1 = []
for x in range(1,nr_letters+1):
    password_list1.append(random.choice(letters))
for y in range(1,nr_numbers+1):
    password_list1.append(random.choice(numbers))
for z in range(1,nr_symbols+1):
    password_list1.append(random.choice(symbols))

print(password_list1)
random.shuffle(password_list1)
print(password_list1)

password = ''
for char in password_list1:
    password += char
print(password)