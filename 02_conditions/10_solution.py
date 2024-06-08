pet='Dog'
age=1


if (pet == "Dog") and (age < 2):
    print ("The recommended food is Puppy Food")
elif (pet == "Dog") and (age > 2):
    print ("The recommended food is Dog Food")
elif (pet == "Cat") and (age < 5):
    print ("The recommended food is Junior cat food")
elif (pet == "Cat") and (age > 5):
    print ("The recommended food is Senior cat food")
else:
    print ("Please provide valid data.")



# pet = input("Enter Pet Type: ")
# pet_age = int(input("Enter Pet Age: "))

# if pet == "Dog":
#     if pet_age < 2:
#         print ("Puppy Food")
#     else:
#         print("Adult Food")
# elif pet == "Cat":
#     if pet_age > 5:
#         print ("Senior cat food")
#     else:
#         print("Baby cat food")
# else:
#     print("Please provide valid data")