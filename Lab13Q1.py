import warnings
warnings.simplefilter('ignore') 

def history():          					#function to print data stored in file
    with open('history.txt', 'r') as file:			  #opening file to read
        for exp in file:                   				 #this loop will run through each line of file
            print(exp, end="")             				 #printing each line in file

def clear_history():   					 #function to clear history 
    with open('history.txt', 'w') as file: 			 #opening the file to write
        pass                       					 #passing the blank file without writing anything
                				#MAIN PROGRAM
print('''Welcome to the interactive calculator.

Enter:  'Exit' to end the program.
\t'History' to show previous expressions.
\t'Clear' to erase history.''')

total_exp = 1       				             #to store total number of expressions entered by user
while True:        				 		#to run program continously until user wants to exit
    expression=str(input("\nEnter your expression:"))   	#asking user for input
    
    if expression == 'History':    				 #if user wants to see history 
        history()                   					#calling the history function

    elif expression == 'Clear':     				#if user wants to clear history
        clear_history()            				 #calling the clear_history function

    elif expression == 'Exit':     				 #if user wants to end the program
        print('program ended.Thank you for using it.')
        break                       					#applying break to come out of loop
    else:
        with open('history.txt', 'a') as file: 			 #opening file to store expressions
            file.write(f'{total_exp}.\t{expression}\n')		 #adding expressions in file using proper formatting
        try:                 					#incase no error occurs                    
            print(f'Answer= {eval(expression)}')    		#evaluate expression and print its output
        						          #to print different statements in case of different errors    
        except ZeroDivisionError :      
            print('Math Error has occured. Recheck your expression.')
        except TypeError :
            print('Error. Use appropriate mathematical operators in expression.')
        except (NameError, SyntaxError):
            print('Error. Mathematical steps cannot be applied on alphabets.')
        except Exception as e:  			      #in case any error other then the above mentioned occurs 
            print(f'Error \'{e}\' has occured. Recheck your expression.')

        total_exp += 1  	#increasing number of entered expressions by one each time user enters expression
