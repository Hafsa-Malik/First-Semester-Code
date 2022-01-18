n=int(input("Enter number of rows:"))
if n<=0:
 print("enter positive number")
else:
 for i in range(1,n+1):
 for j in range(0,n-i+1):
 print(end=" ")
 for j in range(1,i):
 print("*",end=" ")
 print()
