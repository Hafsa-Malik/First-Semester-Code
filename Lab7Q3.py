def miles_to_km(): #fuction for converting miles to km
 miles=int(input("Please Enter miles:"))
 km=miles*1.60
 print(f'{km:.2f} kilometer.')
def celsius_to_fahrenheit(): #function for converting celsius to fahrenheit
 celsius=int(input("Please Enter celsius:"))
 fahrenheit=((9/5)*celsius)+32
 print(f'{fahrenheit:.2f} fahrenheit.')
def feet_to_meters(): #function for converting feets to meters
 feet=int(input("Please Enter feet:"))
 meters=0.3048*feet
 print(f'{meters:.2f} meter.')
def yards_to_meters(): #funtion for converting yards to meters
 yards=int(input("Please Enter yards:"))
 meters=0.914*yards
 print(f'{meters:.2f} meter.')
print("a) miles to km") #to display options choice to user
print("b) celsius to fahrenheit")
print("c) feets to yards")
print("d) yards to meters")
print("e) exit program") #sentinel value for the loop
i=1
while i<=1: #to ask user for input until he enters sentinel value
 option=str(input("Please choose your selected option:"))
 if option==’a’: #if user selects option 1
 miles_to_km()
 continue #to again ask the user for input after 
 elif option==’b’: #if user selects option 2
 celsius_to_fahrenheit()
 continue
 elif option==’c’: #if user selects option 3
 feet_to_meters()
 continue
 elif option==’d’: #if user selects option 4
 yards_to_meters()
 continue
 else: #if user wants to exit program
 print("Program Ended")
 break
