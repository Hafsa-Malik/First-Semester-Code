a=int(input("Please input a natural number:")) #to get input from user
num=a #num will be used in final print statement to display output
reverse=0 #initializing reverse to zero
while a>0: #using while loop to perform calculations for reversing the input
 reverse=(reverse*10)+(a%10)
 a=a//10 #to move input towards sentinel value
print("Reverse of",num,"is",reverse) #to display the reverse value of input
