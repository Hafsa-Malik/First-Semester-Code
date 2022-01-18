def length(a):   			#we will use length to calculate position of each digit
    length=0   
    while a>0: 			  #this loop will run until number becomes 0
        length+=1 			#length increases by one for each iteration
        a=a//10   			 #number of digits decrease by one until become zero
    return length

def check_disarium(num):	 #defining function for calculating disarium
    sum=0              		 #initializing sum to zero
    temp=num           		 #so we can apply calculation on num value without changing it
    power=length(num)   		#initial power is equal to total digits in number
    while temp>0:       		#loop will iterate until there are no digits left in temp
        remainder=temp%10   	#to isolate last digit of temp
        expo=remainder**power     #raise each digit to its position
        power-=1           		 #power decreases by 1
        sum+=expo     		  #to sum each exponentiation
        temp=temp//10  		 #to continuously isolate each digit until temp=0

    if sum==num:        		#condition for disarium number
        return 'disarium'
    else:               			#if the condition isnt satisfied
        return 'not disarium'

#Main Program
print("welcome to disarium checker.")  		#describing to function to user
while True:           		  #to continue the loop until break function is applied
    n=int(input("\nEnter a number:"))		 #asking user for input
    x=check_disarium(n) 				#checking if entered number is disarium or not
    if x=='disarium':   		#incase number is a valid disarium  break the loop
        print(f'{n} is a valid disarium.\n\nProgram ended.Hope you had a good experience.')
        break
    else:               			#incase it isnt a valid disarium continue asking for input
        print(f'{n} is not a valid disarium.')
        continue
