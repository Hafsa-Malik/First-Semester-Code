number_1=int(input("Enter number 1:"))
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))
if number_1>number_2 and number_1>number_3:
 print(number_1,"is the largest number.")
elif number_2>number_1 and number_2>number_3:
 print(number_2,"is the largest number.")
else:
 print(number_3,"is the largest number.")
if number_1<number_2 and number_1<number_3:
 print(number_1,"is the smallest number.")
elif number_2<number_1 and number_2<number_3:
 print(number_2,"is the smallest number.")
else:
 print(number_3,"is the smallest number.")
