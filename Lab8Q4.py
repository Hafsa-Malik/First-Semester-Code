def next_prime(num): 			#defining the function for printing next prime
    def is_prime(num):  			#defining the function for checking if num=prime
        if num>1: 				#any number = or < 1 is not prime
            for i in range(2,num): 
                if num%i==0: 			#condition for not being prime
                    print(f"{num} isn't a prime number.")
                    return False 			#number isn’t prime
            else:   				#if the number isn’t divisible by any i in range
                print(f"{num} is a prime number.")
                return True 			#number is prime
        else:
            print(f"{num} isn't a prime number.\n")			 #for numbers =< 1
    is_prime(num)						#calling the function
    k=num+1 				#checking if the next number is prime
    while True: 				#using loop to continously check for prime number
        for i in range(2,k+1): 
            if k%i==0: 			#if the number isnt prime come out of for loop
                break
        if i==k: 			         #if the number is prime print the number and break while loop
            print(f'Next prime number is {k}')
            break
        else:
            k+=1   			#to keep on checking numbers after input  num until prime is found
#Main program
print("Welcome to next prime number generator.") 
while True: 						#to continously ask user for input
    x=input("\nPlease enter a number:")			#asking user for input
    if x.isdigit()==True: 					#if input is an integer continue
        n=int(x)
        next_prime(n) 					 #calling the function
        continue
    else:				 #incase user enters string end the program
        print("Program ended.Thank you for using it.")
        break
