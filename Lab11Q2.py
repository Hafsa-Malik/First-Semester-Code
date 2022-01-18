def freq(list):                    			 #function to calculate and print repetition in a list
    list.sort()                     			#sorting list in ascending order
    fre_dic={}                      		#empty dict wil be used to create sorted frequency dict
    for item in list:              		 #to store freq of list in form of dictionary
        freq_dic[item]=list.count(item)
    print('\nrule\t\tfrequency')
    for key,value in freq_dic.items():  	#to print sorted frequency table
        print(key[0],'->',key[1],' \t ',value)

def encrypting(text):              		 #this function will encrypt the text
    freq_list=[]                   			 #it will be used to store frequency
    encrypted=''                    
    rules={'a':'i','e':'o','i':'u','o':'a','u':'e','b':'m','d':'t','g':'b','m':'d','t':'g','1':'5','3':'7','5':'9','7':'1','9':'3'}
    for letter in text:             				#this loop will run for each character of text
        if letter in rules:         				#checking if character needs to be encrypted
            freq_list.append((letter,rules[letter]))		#creating frequency list
            encrypted+=rules[letter]   			 #adding encrypted character
        else:                       					#if character doesn't need to be encrypted
            encrypted += letter         
    return encrypted,frequency      			#returning encrypted text and frequency list

def decrypting(text):               				#function to decrypt text
    freq_list=[]                   					 #it will be used to create frequency list
    decrypted=''
    rules={'i':'a','o':'e','u':'i','a':'o','e':'u','m':'b','t':'d','b':'g','d':'m','g':'t','5':'1','7':'3','9':'5','1':'7','3':'9'}
    for letter in text:             				#this loop will run for each character of text
        if letter in rules:       				  #checking if character needs to be decrypted
            freq_list.append((letter,rules[letter])) 		#creating frequency list           
            decrypted+=rules[letter]        			#adding decrypted character
        else:                      					 #if character doesn't need to be decrypted
            decrypted += letter
    return decrypted,freq_list      				#returning decrypted text and frequency list
               			 #MAIN PROGRAM
print('Enter\nA-to encrypt\nB-to decrypt\nX-to exit')	#displaying options to the user
while True:                                         			#run program until break is applied
    option=str(input('\nchoose your option:'))     		 #ask user to enter their option
    if option=='X':                                			 #if user wants to exit program
        print('Program ended.')
        break                                       				#breaking the loop
    original=str(input('\nOrignal text:'))          		#asking user to enter text
    if option=='A':                                 			#if user wants to encrypt text
        encrypt,frequency=encrypting(original)      	#calling function for encryption and storing output
        print('Encrypted text:',encrypt)            		#to display encrypted text
        freq(frequency)                           			  #calling function to print frequency table
    elif option=='B':                             			  #if user wants to decrypt text
        decrypt,frequency=decrypting(original)     	 #calling function for decryption and storing output
        print('Decrypted text:',decrypt)           		 #displaying decrypted text
        freq(frequency)                            			 #calling function to print frequency table
