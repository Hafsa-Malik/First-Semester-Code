a=int(input("Please input a natural number:")) #to get input from user
num=a #storing input in num
reverse=0 #initializing reverse to zero
while a>0: #while loop to calculate reverse 
 reverse=(reverse*10)+(a%10)
 a=a//10 #to push loop towards sentinel value
if reverse==num: #checking if reverse is equal too original number
 print("The number",num,"is palindrome.") #output for palindrome num
else:
 print("The number",num,"is not a palindrome.") #output for non palindrome numbers
