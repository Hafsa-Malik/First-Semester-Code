import area_calc 			       #import the module mentioned below for area calculations

def surface_area_cyl(r,h):		               #defining function to calculate surface area of cylinder 
    area=(2*3.14*r*h)+(2*3.14*(r**2))			#mathematical formula
    return area						#returning the answer to main function
					#MAIN PROGRAM
print(f'welcome to area calculator\n\nEnter the shape type') 	#explaining the program to user
print(f't-For triangle\nr-For rectangle\nc-For circle\ncyl-For cylinder\nx-To exit')

while True: 				             #to continuously ask user for input until break is applied
    shape=str(input('\nShape Type:'))			#ask user to enter shape
    if shape=='r':						#if user wants to calculate area of rectangle
        length=int(input("\nEnter Length:"))		#ask for length of rectangle
        Width=int(input("Enter Width:"))			#ask for width of rectangle
        print(f'area of rectangle is {area_calc.area_rectangle(length,Width)} sq unit')            #display output
        continue 						#to again go back to input option
    if shape=='t': 						#if user wants to calculate area of triangle
        base=int(input("\nEnter base:")) 			#ask for base of triangle
        height=int(input("Enter height:")) 			#ask for height of triangle
        print(f'area of triangle is {area_calc.area_triangle(base,height)} sq unit')	             #display output
    if shape=='c': 						#if user wants to calculate area of circle
        radius=int(input("\nEnter radius:")) 		#ask for radius of circle
        print(f'area of circle is {area_calc.area_circle(radius)} sq unit')  		            #display output
    if shape=='cyl': 				         #if user wants to calculate surface area of cylinder
        radius=int(input("\nEnter radius:")) 		#ask for radius of cylinder
        height=int(input("Enter height:")) 			`#ask for height of cylinder
        print(f'surface area of cylinder is {surface_area_cyl(radius,height)} sq unit')  	            #display output
    if shape=='x': 						#if user wants to end the program
        print("program ended.")
        break						#break the loop
