n=int(input("Please input a natural number:"))
if n<=0:
 print("Please enter a positive number")
else:
 print("The multiplication table of",n,"is:")
 for i in range(1,11):
 print(n," x ",i,"=",n*i)
