a=int(input("Enter nonzero integer 1:"))
b=int(input("Enter nonzero integer 2:"))
c=int(input("Enter nonzero integer 3:"))
if a==0 or b==0 or c==0:
 print("sides can not be zero.")
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
 print("Given integers are sides of a right-angled triangle.")
else:
 print("Given integers are not sides of a right-angled triangle.")
