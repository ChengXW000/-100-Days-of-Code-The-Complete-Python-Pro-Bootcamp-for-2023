# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
num_of_people = 0
#Write your code below this row 👇
for height in student_heights:
    total_height += height
    num_of_people += 1

average_height = round(total_height/num_of_people)
print(average_height) 

