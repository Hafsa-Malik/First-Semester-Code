def len(num):          				 #to calculate length of a number       
    length=0           				 #initializing length to zero
    while num!=0:      				 #this loop will run until number becomes 0 
        length+=1     			 	 #length increases by one for each iteration
        num=num//10    				 #number of digits decrease by one until become zero  
    return(length)     				 #returning the length

def maxi_num(num):         			 #function for calculating maximum num
    largestNum=9           				 #initially largest single digit  is 9
    Max=0                   				#initializing maximum num to 0
    while largestNum>=0:  		 	 #this loop will run for each largest num
        temp=num           				 #storing input in temporary variable
        for i in range(len(num)):  			 #this loop will run for each digit of input
            remainder=temp%10       			#extracting last digit of the input
            if remainder==largestNum:		#checking if last digit= largest num
                Max=(Max*10)+largestNum		 #changing maximum if any digit is equal to largest num
            temp=temp//10          			 #removing last digit of input
        largestNum-=1      				 #decreasng largestnum by 1 until becomes 0
    return Max             				 #returning the maximum number to function

def mini_num(num):    				 #function for calculating smallest num
    temp=maxi_num(number)   			#assigning maximum num to a variable
    Min=0              				 #initializing minimum num to zero
    while temp>0:      				 #this loop is used to reverse the maximum number
        Min=(Min*10)+(temp%10)			#changing min num to reverse of max num
        temp=temp//10   				#to remove last digit of the number
    return Min          				#returning the minimum number
               			 #MAIN PROGRAM
i=1                     
while i==1:    					 #this loop will check if the entered number is natural
    number=eval(input("Enter a natural number:")) 		#asking for input
    if number>0 and type(number)==int:     			 #if the number is a natural num
        i+=1                   						 #terminate the loop
    else:                       						#incase input isn't a natural num
        print(f"\n{number} is not a natural number.Try again\n")       #loop continues

print(f'\nAfter rearranging the digits \nlargest number: {maxi_num(number)}')
print(f'smallest number: {mini_num(number)}') 			  #displaying output to the user 
