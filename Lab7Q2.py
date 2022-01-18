import math #to use built in squareroot function
def point_distance(x1,y1,x2,y2): #defining function for calculating distance
 distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2)) #mathematical formula for distance
 print(f"The distance bettween these points is {distance:.2f}") #displaying output after 
 rounding off
a=float(input("Enter X1:")) #inputs from user
b=float(input("Enter Y1:"))
c=float(input("Enter X2:"))
d=float(input("Enter Y2:"))
point_distance(a,b,c,d) #calling the function
