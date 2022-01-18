def list(num):						 #defining function for creating list
    List=[]			                 #creating an empty list so we can append new numbers in it.
    for i in range(1,num+1):	      #to ask for input depending on how many list elements user wants
        elements=str(input(f"Enter number {i}:"))		#asking for input
        List.append(int(elements))				#appending entered number in empty list
    return List						#returning the list 

def remove_duplicate(List):			#this function will remove duplicates
    temp=[]					#an empty list
    for i in List:					#this will run for reach element of list
        if i not in temp:				#checking if list element is present in temp
            temp.append(i)		        #for appending only those elements which aren’t already present
    return temp					#returning the list without duplicates

def check_freq(list):				#this function will calculate frequency of occurence
    b=remove_duplicate(list)			#new list without duplicates
    freq=0					#initializing frequency to zero
    freq_num_list=[]				#taking an empty num, frequency list
    for i in b:				#this loop will check how many times an element is repeated
        for j in list:	
            if i==j:					
                freq+=1
        if freq>1:			#we only want to display frequency of  num entered multiple times
            freq_num_list.append([freq,i])		#storing num and frequency in form of list
        freq=0					#setting freq again to zero for next num in list
    return freq_num_list				#returning the final num, frequency list
			#MAIN PROGRAM
num_of_ele=int(input("How many numbers you want to enter:"))        #asking user for total num in list
print()						#to print an empty line
num_list=list(num_of_ele)			#to create a list 

print(f'\nList with duplicates: {num_list}')	#displaying list with duplicates to user
print(f'list without duplicates: {remove_duplicate(num_list)}\n')	 #display list after removing duplicates

print("number \t frequency")
sort_freq=check_freq(num_list)			#calling the function to create num, frequency list
sort_freq.sort(reverse=True)			#sorting the list based on highest frequency
for k in sort_freq:				#this loop will print each element of the list
    print(k[1],'\t',k[0])    				#displaying output to the user
