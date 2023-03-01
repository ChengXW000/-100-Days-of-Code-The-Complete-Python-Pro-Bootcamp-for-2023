#If the bill was $150.00, split between 5 people, with 12% tip. 
print("WELCOME TO THE TIP CALCULATOR.")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6


tip_percent = (tip_percent/100) + 1


#Format the result to 2 decimal places = 33.60

total = bill * tip_percent
pay_per_person = round(total/people, 2)


print(f"Each person should pay: ${pay_per_person}")

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇