def show_difference(L,W):		#defining  fuction to show subtract area of circle and ellipse
    area_of_circle=0			 #initializing area to zero so we can use it in inner function
    area_of_ellipse=0
    def area(L,W):
        nonlocal area_of_circle     		#so that the changes done in inner fuction should be shown        					in outer function as  well.
        nonlocal area_of_ellipse
        area_of_circle=3.1415*((L/2)**2)*((W/2)**2) 	#formula for area of circle 
        area_of_ellipse=3.1415*(L/2)*(W/2)          		#formula for area of ellipse
    area(L,W)                                       			#calling inner function
    
    diff=area_of_circle - area_of_ellipse           		#difference between both areas
    return diff                    					 #returning difference to out function
#Main Program
print("Welcome to the program.\n\nEnter dimensions of the square")
length=int(input("length of square:")) 			#asking user to enter length
width=int(input("width of square:"))   			 #asking user to enter width
#displaying output after suitable  formating 
print(f"\nArea of circle and ellipse differ by {show_difference (length,width):.2f} sq unit.")
