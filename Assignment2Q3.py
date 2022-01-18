rows=int(input("Enter number of rows:"))			#to get input from the user
n=0                				 #temporary variable that will be used to print numbers
space = rows     				#it will be used to provide range for printing spaces
for i in range(1,rows+1): 		#for printing each row
    n=i             		#so that we can change i in inner loops without changing i in outerloops too
    for j in range(1, space):		#loop for printing spaces
        print("   ", end="") 
    space= space – 1			 #as the spaces in each successive row decrease by 1
          
    for j in range(1,i+1): 			#for printing left half of the pyramid
        print('%3d'%n, end="") 
        n+=1              	  #in each column number increases by one in left half pyramid
      
    n - = 2    		#difference b/w ending n for left half and starting n in right half is of two digits                    
    for j in range(1,i):    	#for printing right half of the pyramid
        print('%3d'%n, end="") 
        n-=1              	  #in each column number decreases by one in right half pyramid
    print()                 	  
