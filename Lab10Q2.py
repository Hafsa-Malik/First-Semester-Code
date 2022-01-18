def sort_matrix(matrixc): 			#defining function for sorting the matrix
    matrixc.sort(key=sum,reverse=True)	         #using built in sort function to sort the list using sum as key
    return matrix					#returning the sorted matrix		

def column_checker(matrixc):                     #this function will check if no. of columns in each row are same
    columns=len(matrixc[0])	#initializing columns to no. of elements  in first row
    no_of_columns=''	#this will be used to display if columns are same or not
    for i in matrixc[1:]:                    #this loop will check if all other rows have same no. of elements as row 1
        if len(i)!=columns:	#if rows have different no. of elements
            no_of_columns='different'	
            break
        else:	#if the rows have same no. of elements
            no_of_columns='same'
    return no_of_columns  	#returning the output

print('welcome to matrix sorter!!')	
print('Enter matrix in the form of list and rows as sub-lists.')
while True:	#this loop will continue until user enters correct matrix
    matrix=eval(input("\nEnter your matrix:"))	#asking user for input
    check=column_checker(matrix)	#calling function to check if columns are same
    if check=='same':	#if columns are same sort the matrix
        print('..........................................................')
        print(f'Sorted Matrix: {sort_matrix(matrix)}')	#displaying output to the user
        print('..........................................................')
        break		#to end the program
    else:	#if no. of columns are not same
        print('All rows should have same number of elements.Try again')
        continue	#this will again ask user to input correct matrix
