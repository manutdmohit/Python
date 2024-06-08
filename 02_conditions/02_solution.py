# WAP for ticket pricing system
# Price for adult (age greater than or equal to 18) is $12 and for children is $8
# Every Wednesday there is a $2 discount for every age group


age=16;
day="wednesday"


price=12 if age>=18 else 8

if(day== "wednesday"):
    price-=2

print("The price of the ticket for you is $",price )