n=int(input("Please enter a natural number:"))
factorial=1
if n<=0:
 print("please enter a positive number")
else:
 for i in range(1,n+1):
 factorial *= i
 
print("the factorial of",n,"is",factorial)
