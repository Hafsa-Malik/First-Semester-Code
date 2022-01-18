n=int(input('enter a natural no:'))
sum=0
if n<=0:
 print("Enter a positive number")
else:
 for i in range(1,n+1):
 sum+=i
 
print("the sum of all natural numbers from 1 to",n,"is",sum)
