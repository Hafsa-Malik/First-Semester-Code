def list():		#defining function for creating list
    List=[]		#creating an empty list so we can append new numbers in it.
    while True:		#to continuously ask user to enter numbers until break is applied
        elements=str(input("Enter a number:"))	#asking for input
        if elements=='X':				#if user wants to stop adding new numbers in list
            break					#to end the loop
        else:		#to append entered numbers in empty list
            List.append(int(elements))
    return List		#returning the list

def sort_list(List):			#defining function to sort the list in ascending manner
    i=0				#it will be used to separate each element if list to compare	
    temp=0			#it will be used to switch the numbers 
    while i<len(List):		#we want the loop to run one time less than the numbers in list
        j=i+1			#it will used to provide rest of the numbers of list to compare to i
        while j<len(List):		#we want the loop to run one time less than the total numbers in it
            if List[i]>List[j]:		#comparing if first number is greater than second
                temp=List[j]		#if true than switch them using temp
                List[j]=List[i]
                List[i]=temp
            j+=1			#increase by one to compare with next number in the list
        i+=1			# increase by one to compare next number in the list with the rest
    return List			#return the sorted list

def maximum_num(list):	#defining function to calculate maximum number 
    max_num=list[0]		#initializing maximum num to first number in the list
    i=0				
    while i<len(list):		#while loop to compare initial max_num with every other number
        if list[i]>max_num:		#incase any other num in list is greater than initial max 
            max_num=list[i]		#set maximum num to that number
        i+=1			#keep incrementing i by one to compare next element of list with max
    return max_num		#return the final answer
def minimum_num(list): 	#defining function to calculate minimum number
    min_num=list[0] 		#initializing minimum num to first number in the list
    i=0
    while i<len(list): 		#while loop to compare initial min_num with every other number
        if list[i]<min_num: 		#incase any other num in list is smaller than initial max
            min_num=list[i] 		#change minimum num to that number
        i+=1			#keep incrementing i by one to compare next element of list with min

    return min_num		#return the final answer
					#MAIN PROGRAM
num_list=list()			#calling the function to create a list
print(f'The number list is {num_list}')		#displaying the list to user
print("\nYour have following options.\n")	#describing the program and functions to user
print("a.Enter new list\nb.Maximum and minimum numbers in the list")
print("c.Sum of the squares of each number in list")
print("d.Sort list in ascending order\ne.Exit the program")
while True:				#to continuously ask user for input until break is applied
    option=str(input("\nchoose your option:"))	#asking input from the user
    if option=='a':				#incase user chooses option a
        num_list=list()			#again calling list() function to create new list
        print(num_list)			#printing new list
        continue				#go back to the input option
    if option=='b':			#if user wants to calculate maximum minimum numbers
        print(f'maximum number is {maximum_num(num_list)}’)
        print(f’minimum number is {minimum_num(num_list)}')

    if option=='c':				#if user wants to calculate sum of square of elements
        num_squared=map(lambda x:x**2,num_list) 	# anonymous function for squaring elements
        Sum=0				#initializing sum to zero
        for num in num_squared:		#for summing each element of list having squared elements
            Sum+=num
        print(f'sum of elements squared is {Sum}')
    if option=='d':							#if user wants to sort the list
        print(f'sorted list in ascending order is {sort_list(num_list)}')		#displaying output
    if option=='e':				#if user wants to end the program
        print("program ended.")		
        break				#break the loop so it no longer asks for input 
