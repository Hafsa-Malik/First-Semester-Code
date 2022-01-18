print("Count sum of 10 even numbers entered by user")
a=10
total=0 #initializing
while a>0:
    print("Remaining number:",a,end=",")
    b=int(input("Enter an even number:")) #to get input from user
    if b%2!=0: #to get sum for only even numbers
        print(b,"is not an even number. Try again.\n")
        continue
    total+=b #this function will sum the user inputs
    a-=1 #to bring loop towards sentinel value
print("The sum of 10 even numbers is",total) #to display the sum
