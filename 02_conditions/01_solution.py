# Take user input and convert it into integer
age=int(input("Enter age: "));

if age < 0 :
    print("Invalid age")
elif age < 13 : 
    print("Child")
elif age < 20 : 
    print("Teenager")
elif age< 60:
    print("Adult")
else :
    print("Senior")