n=int(input("enter number of rows:"))
for i in range(1,n+1):
 print(" "*(i-1),end="")
 for j in range(0,2*(n-i)+1):
 print("* ",end="")
 print()
