def custom_print(*values,sep=" ",end="\n"): #to set default values of end,sep,and get variable  
     									  length arguments
    list_items=(values)                     	#Assigning variable length arguments to another variable
    length=len(list_items)                 	 #calculating length of input values
    for i,item in enumerate(list_items):      #for loop to individually print each number
        if i<(length-1):                     		#for printing all values other than end value
            print(f"{item}{sep}",end="")
        if i==(length-1):                 		  #for printing end value
            print(f"{item}{end}")
