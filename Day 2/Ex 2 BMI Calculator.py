# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
temp = float(height)
new_height = (temp * temp)


new_weight = float(weight)

BMI = new_weight / new_height
print(int(BMI))