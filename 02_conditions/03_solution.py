# WAP for grading system
# Price for adult (age greater than or equal to 18) is $12 and for children is $8
# Every Wednesday there is a $2 discount for every age group


score = 105

if score >= 101 or score <0:
    print("Please verify your score again")
    exit()

if score >=90:
    grade="A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else: 
    grade = "F"

print("Grade: ",grade)