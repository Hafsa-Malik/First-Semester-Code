def strength_checker(passwrd): 		#function to calculate strength of password
    signs=['$','@','#'] 
    strength=0     					#initializing strength to zero
    uppercase=0     				#initializing number of uppercase letters to zero
    lowercase=0     				#initializing number of lowercase letters to zero
    number=0    					 #initializing number of digits to zero
    sign=0    					 #initializing number of signs present to zero
    for letter in passwrd: 				 #this will run for each letter in password
        if letter.isupper():    			#checking if the letter is uppercase
            uppercase+=1        			#increase by 1 if letter is uppercase
        else:
            lowercase+=1       			 #if letter is not uppercase increase lowercase by 1
        if letter in signs:    				 #checking if letter is one of the signs
            sign+=1             				#increase by 1 if letter is present in sign list
        if letter.isdigit():    				#checking if the letter is a digit
            number+=1          				 #increases by 1 if the letter is a digit
    if uppercase>=1 and lowercase>=1: 		#if there's atleast one lowercase and 1 uppercase letter
        strength+=2     				#increasing strength by 2
    if sign>=1:         				#if there's atleast 1 sign present
        strength+=3    				 #increasing strength by 3
    if number>=1:      				 #if there's atleast 1 digit present
        strength+=3    				 #increasing strength by 3
    if len(passwrd)>=8 and len(passwrd)<=16:   	 #if length of password is between 8 and 16
        strength+=2    				 #increasing strength by 2
    return strength    				 #returning the strength of passowrd

def save_in_file(passwrd): 			#function to save password in file
        file=open('password.txt','w')		#creating a file to write
        file.write(passwrd)       			 #writing password in file
        file.close()          				  #closing the file

#MAIN PROGRAM
while True: 					#this loop will run until we get a valid password
    password=str(input('\nEnter your password:'))   	#asking user to enter password
    strength=strength_checker(password)         		#checking strength of password
    print('\nPASSWORD STRENGTH:',strength)      		#displaying password strength to user
    if strength>8:          					#if password's strength exceeds 8
        print('PASSWORD SAVED SUCCESSFULLY')
        save_in_file(password) 				 #to save password in file
        break   						#break the loop
    else:             						 #if passwords strength is 8 or less
        print('Your password is weak.Try using capitalization, symbols(@,#,$), letters and numbers (max:16, min:8).')
        continue       				 #again ask user to enter password
