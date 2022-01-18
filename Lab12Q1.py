def freq_checker(search_word,word_list):   		 #function to check frequency of word
    freq_list=[]   						 #we will use it to store words and their frequency
    for term in search_word.split():  			  #this loop will run for each given word
        freq=0      						#initializing frequency to zero
        for  word in word_list:    				 #this loop will run for each word in given text file
            if term==word:     				 #if word is same as what we are looking for
                freq+=1       					  #frequency increases by 1
        freq_list.append([freq,term])  			 #appending word's frequency to freq_list
    return freq_list           					 #returning frequency list

def freq_sort(freq_list):     				  #function to sort and print frequency list 
    print(freq_list)
    freq_list.sort()           					 #sorting freq_list in ascending order
    freq_file=open('freq_file.txt','w')			 #creating/opening a file to write
    freq_file.write('Words\t\tFrequency\n')		 #writing in file
    print('\nWord \t\tFrequency')   			#to print a table
    for i in freq_list:         					#this will run for each item in frequency list
        freq_file.write(str(i[1])+'\t\t'+str(i[0])+'\n') 		#to write word and their frequency in file
        print(f'{i[1]}\t\t{i[0]}')  				#printing word and its frequency
    freq_file.close()   					#closing file after saving data 

def word_sentence_checker(data):			 #function to check total words and lines
    word_list=data.split()     				 #spliting text into words list
    sentence_list=data.split('. ') 				#splitting text into sentence list
    return len(word_list),len(sentence_list), word_list 	#returning length of word list,sentence list

def read_file(user_file):  				 #function to read and print file
    print('\n','-'*25,user_file,'-'*25)			 #to display file name at top
    file=open(user_file)        				#opening user's file
    data=file.read()           					 #reading user's file
    print(data)                					 #to print the file
    file.close()               					 #to close the file after reading
    return data                					 #returning the data

#MAIN PROGRAM
user_file=str(input('Enter file name:'))  			  #asking user to enter file
while True:               					  #to continously ask user for option
    print('\nMENU:\nR-Read File\nS-Show Statistics\nF-search words frequency\nX-to exit')
    option=str(input('Enter your option:')) 		#asks user for desired option
    if option=='R':   					  #if user wants to read and print file
        data=read_file(user_file) 				#calling function to read and display file
        continue
    elif option=='S':  					 #if user wants to know words and lines count
        total_words, total_sentence,word_list = word_sentence_checker(data) 
        print('\nTOTAL WORDS:',total_words) 
        print('TOTAL SENTENCES:',total_sentence)
        continue
    elif option=='F':   					#if user wants to check frquency 
        search_word=str(input('\nEnter the words you want to find:'))
        freq_list=freq_checker(search_word,word_list) #calling function to check words frequency 
        freq_sort(freq_list)      #sorting and printing the frequency list
        continue
    elif option=='X':   #if user wants to exit the program
        print('Program ended')
        break
