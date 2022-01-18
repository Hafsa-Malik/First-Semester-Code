import random                			#to generate random number
x=random.randint(1,1000)       		#start stop range for random number
def guess():                   			 #defining the fuction
    n=int(input("Enter your guess:"))   	#asking user for input
    if (n-x)==0:               			 #if user's guess is correct
        print(f"Yay! you got it {n} is the right answer:)")	#display output to user
    elif (n-x)>200:            			#if guessed num is more than 200 num ahead
        print("oops! too high :(")
        guess()               			#again calling the function to repeat procedure
    elif (n-x)>10:            			#if guessed num is more than 10 num ahead
        print("high")
        guess()
    elif (n-x)>0 and (n-x)<11:  		#if guessed num is less than or equal to 10 num ahead
        print("slightly high.You are very close.")
        guess()
    elif (x-n)>0 and (x-n)<11:  		#if guessed num is less than or equal to 10 num behind
        print("slightly low.")
        guess()
    elif (x-n)>10 and (x-n)<=200:		#if guessed num is more than 10 num behind
        print("low")
        guess()
    elif (x-n)>200:           			  #if guessed num is more than 200 num behind
        print("oops! too low :(")
        guess()
guess()                         			#calling the function
