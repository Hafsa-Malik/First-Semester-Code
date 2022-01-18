print("Welcome to the interactive calculator.")       #introducing the program
while True:					#to continuously ask user for input until break
    n=str(input("\nEnter your expression:")) 	#to get input from the user
    if n!='Quit':					#incase user doesn’t enter quit
        print(f'Answer= {eval(n)}')			#to evaluate and display user input
        continue					#come out of if condition and again ask for input
    elif n=='Quit':					#incase user wants to end the program
        print('program ended.Thank you for using it.')
        break					#break the loop
