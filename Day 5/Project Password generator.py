# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 52
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #10
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] #9
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password1 = ""
password2 = ""
letter_rand = random.randint(0, 51)
number_rand = random.randint(0, 9)
symbol_rand = random.randint(0, 8)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(0, nr_letters):
  letter_rand = random.randint(0, 51)
  password1 += letters[letter_rand]
for symbol in range(0, nr_symbols):
  symbol_rand = random.randint(0, 8)
  password1 += symbols[symbol_rand]
for number in range(0, nr_numbers):
  number_rand = random.randint(0, 9)
  password1 += numbers[number_rand]

print("Your password is: " + password1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = password1
password2 = ''.join(random.sample(password2, len(password2)))
print("Your shuffled password is: " + password2)