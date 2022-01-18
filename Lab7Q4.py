def factorial(num): #fuction for calculating factorial
 factorial=1 #initializing factorial to one
 i=1 #applying while loop to calculate factorial
 while i<=num:
 factorial*=i
 i=i+1 #to move loop towards sentinel value
 return factorial #returning the output to the function
 
def strong_number(): #function to determine strong number
 n=int(input("Please enter a number:")) #taking input from the user
 sum=0 #initializing sum of factorial to zero
 temp=n #storing input in temp so it can be altered
 while temp >0: #to calculate factorial to individual digits
 remainder=temp%10 #to separate the last digit and calculate its factorial
 fact=factorial(remainder) #calling the above defined function factorial()
 sum+=fact #adding the factorial values
 temp=temp//10 #to separate each digit and move towards sentinel value
 
 if sum==n: #by defination of strong number
 print(n,"is a strong number.") #displaying output if input=strong number
 else: #incase output doesn't match the condition of strong no.
 print(n,"is not a strong number.") #displaying output if number isnt strong no.
 n=str(input("Enter 'y' to continue 'q' to quit:")) #to again continue to exit function
 if n=='y': #if the user wants to continue
 strong_number()
 else: #if user wants to exit
 print("program ended")
strong_number() #calling the function
