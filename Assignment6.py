from encrypt_password import encrypting     			#importing module to encrypt password

#def encrypting(text):              		 #this function will encrypt the text
    #freq_list=[]                   			 #it will be used to store frequency
    #encrypted=''                    
    #rules={'a':'i','e':'o','i':'u','o':'a','u':'e','b':'m','d':'t','g':'b','m':'d','t':'g','1':'5','3':'7','5':'9','7':'1','9':'3'}
    #for letter in text:             				#this loop will run for each character of text
        #if letter in rules:         				#checking if character needs to be encrypted
            #freq_list.append((letter,rules[letter]))		#creating frequency list
            #encrypted+=rules[letter]   			 #adding encrypted character
        #else:                       					#if character doesn't need to be encrypted
            #encrypted += letter         
    #return encrypted,frequency      			#returning encrypted text and frequency list


def register():         					#function to register new student
    data_dict={}        					#dictionary to store data of new student
    data_dict['Name']=input("\nEnter your name:")
    data_dict['cms_id']=input("Enter your CMS ID:")
    password=input("Enter your passowrd:")
    encrypted_pass=encrypting(password)	 	#encrypting password using encrypting function
    data_dict['encrypted_password']=encrypted_pass
    return data_dict   					 #returning student dictionary

def students_data(file):    				#function to display registered students data
    print('Sr.no\t STUDENT \t CMS ID')
    students=1              						#this will display index of each student
    for student in file:   						 #this loop will run for each line in file
        student=eval(student) 		 				 #to access the dictionary
        print(students,'\t',student['Name'],'\t\t',student['cms_id'])		#printing data in each line
        students+=1	
def login(cms,password):   			 #function to login user after checking password and cms
    file=open('students.txt')   					#opening the students file
    cms_list=[]     	
    pass_list=[]
    for student in file:   						 #this loop will run for each line in file
        student=eval(student)  			 		#to access students dictionary
        cms_list.append(student['cms_id'])				 #to create a list of cms ids
        pass_list.append(student['encrypted_password']) 		#to create a list of passwords
    file.close()
    if cms in cms_list and encrypting(password) in pass_list:   #if entered cms and password is present in lists
        print('**LOGIN SUCCESSFULL**')
        return True
    else:
        print('**INVALID USERNAME/PASSWORD**')  	#if entered cms or pasword isn't present in list
        return False
    
def updated_file(file_data):				#to update the file using updated list
    with open('students.txt', ‘w’) as file:			#opening file for writing 
        file.writelines(file_data)				#writing each item in list on separate line

def change_name(cms):  				 #function to change name of student
    file=open('students.txt')				   #opening students file
    file_data=file.readlines() 				 #to store lines in file in form of list
    students=0          
    for student in file_data:   				#this loop will run for each student dict in list
        student=eval(student)   
        if student['cms_id']==cms: 				 #to separate the user's dictionary
            file_data.pop(students)				 #removing the students dict from list
            print('\nCurrent Name:',student['Name'])		 #to display current name of student
            student['Name']=input('Enter New Name:')	#updating the student dict
            file_data.insert(students,f'{student}\n')		#inserting student dict in list after updating
        students+=1     
    updated_file(file_data)  				 #changing the text in file 

def delete_account(cms):   				 #function to delete account of user
    file=open('students.txt')  				 #opening students file
    file_data=file.readlines() 				 #storing each students dictionary in form of list
    students=0
    for student in file_data:  				 #this loop will run for each student dict in list
        student=eval(student)  				 #to access the dictionary 
        if student['cms_id']==cms:				 #to separate the user's dictionary
            file_data.pop(students)   				  #removing the students dictionary from list
        students+=1
    updated_file(file_data)  				 #changing file according to changes made in list
#MAIN PROGRAM
print('MENU:\nR-to register new student\nD-to get data of registered\nL-to login\nX-to exit')
while True:    							 #to run the program until user wants to exit
    option=input("\nPlease enter your option:")			 #asking user for options
    if option=='R': 						#if user wants to register new student
        data=register()						 #calling the function 
        with open('students.txt','a') as file:				 #opening students file
            file.write(f'{data}\n')    					 #writing students data in file
        
    elif option=='D':   						#if user wants to check registered data
        with open('students.txt') as file: 				 #opening students file to read
            students_data(file)    					 #calling function to display data

    elif option=='L':   						#if user wants to login 
        cms=input('CMS ID:')   					 #asking user for cms id
        password=input('Enter your password:')  			#asking user for password
        result=login(cms,password)  			#calling function to check validity of id and password
        if result==True:   					 #if both inputs are valid
            while True: 					#this loop will run until user wants to log out
                print("\n\t\tENTER n\t\ta. to change name \n\t\tb. to delete account\n\t\tc. to logout")
                choice=input('Enter any of the above options:') 	#asking user for desired option
                if choice=='a':   					  #if user wants to change name
                    change_name(cms)  					  #calling function to change name
                    print('**NAME UPDATED SUCCESSFULLY**')
                elif choice=='b':     					  #if user wants to delete account
                    delete=input('Are you sure you want to delete your account (yes or no):')       #asking for confirmation
                    if delete=='yes':
                        delete_account(cms) 				#calling function to delete account
                        print('**ACCOUNT DELETED SUCCESSFULLY**')
	          break
                elif choice=='c':       					#if user wants to logout
                    print('**LOGGED OUT**')
                    break  						 #applying break to exit the loop
        
    elif option=='X':   						#if user wants to exit program
        print('Program ended')
        break  							 #applying break to exit the loop
