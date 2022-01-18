a=int(input("Enter natural number 1:"))
b=int(input("Enter natural number 2:"))
if a%b==0:
 print("l.C.M of",a,"and",b,"is",a)
elif b%a==0:
 print("l.C.M of",a,"and",b,"is",b)
else:
 for i in range(1,a*b+1):
 if i%a==0 and i%b==0:
 print("L.C.M of",a,"and",b,"is",i)
 break
