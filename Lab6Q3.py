i=1
while i>=1: 
    n=int(input("Enter a single digit odd number:")) #asking user for input
 
    #To limit output for only single digit odd integers
    if n%2==0 or n//10>1:
        print(n,"is not a sigle digit odd integer. Try again.")
        continue
 
    else: #to print the pattern
        for i in range(n,0,-2): 
            if i==n: #for printing first row
                for j in range(1,i+1):
                    print(n,end=" ")
                print()

            elif i==1: #for printing last row
                 print(" "*((n-i)//2),i)

            else: #for printing middle rows
                 print(" "*((n-i)//2),i," "*(i-3),i)

            i-=1 #to bring loop towards sentinel value
