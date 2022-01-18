def addition(x,y): 			#function to calculate sum of two numbers
    return x+y				#to return the sum
def subtraction(x,y):			#function to calculate difference of two numbers
    return x-y				#to return the difference
def multiplication(x,y):			#function to calculate product of two numbers
    return x*y				#to return the product
def division(x,y):			#function to divide two numbers
    return x/y				#to return the output after division
def remainder(x,y):			#function to display remainder of x divided by y
    return x%y				#return the output 
def expo(x,y):				#funtion to calculate x raised to power y
    return x**y				#return the output
def calc(): 			#funtion to perform calculation depending on what user  selected
        if option=='a':		#if user selects a perform addition
            print(f'{num_1} + {num_2} ={addition(num_1,num_2)} \n')
        elif option=='s':		#if user wants to perform subtraction  
            print(f'{num_1} - {num_2} = {subtraction(num_1,num_2)} \n')
        elif option=='m':		#if user wants to perform multiplication
            print(f' {num_1} x {num_2} = {multiplication(num_1,num_2)} \n')
        elif option=='d': 		#if user wants to perform division
            print(f'{num_1} / {num_2} = {division(num_1,num_2)} \n')
        elif option=='r': 		#if user wants to calculate remainder of x divided by y
            print(f'remainder of {num_1} divided by  {num_2} is {remainder(num_1,num_2)} \n')
        elif option=='e': 		#if user wants to raise x to power y
            print(f'{num_1} raised to power {num_2} is {expo(num_1,num_2)} \n')
