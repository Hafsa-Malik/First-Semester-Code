import math        				 #we will use its squareroot funtion
def distance_calculate(pointA,pointB):      	#this function will calculate distance   
    distance = math.sqrt(((pointA[0]-pointB[0])**2)+((pointA[1]-pointB[1])**2))
    return distance                         			#returning the distance between tuples
                    #MAIN PROGRAM
total_points=int(input('Enter total number of points:'))    #to get total number of points from user
print()                         
point_list=[]                                           			    #we will append all points in this list
for i in range(1,total_points + 1):                         		   #to get points from the user
    point=eval(input(f'Enter point {i} in form of (x,y):'))
    point_list.append(point)                               		 #appending points in initially empty list

total_distance=0                                           		  #initializing total distance to zero
for i in point_list:                                      		                 #to calculate distance between two points of list
    index=point_list.index(i)                              		   #calculate index of eack point in list
    if index!=(total_points-1):                             
        distance=distance_calculate(i,point_list[index+1])     #calculating distance between point i and next point
        total_distance += distance                        		  #adding distance to total distance
        
print(f'\nDistance from {point_list[0]} to {point_list[total_points-1]} is {total_distance:.2f} units')													#displaying output
