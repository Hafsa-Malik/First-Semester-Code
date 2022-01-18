import math			#we will use the ceiling function from it to round off answers

def tiles_in_room(L,W,Tile_Size):	#this function will calculate number of tiles for each room
    room_area=L*W			#to calculate area of the room
    tiles_required=room_area/Tile_Size	#divide area of room by area of tile to get number of tiles req
    return math.ceil(tiles_required)	#returning the number of tiles after rounding off

def tiles_boxes(num_of_tiles):		#this function will calculate boxes of tiles required
    tiles_per_box=25			
    boxes_req=num_of_tiles/tiles_per_box	#dividing no. of tiles by tiles per box to get boxes req
    return math.ceil(boxes_req)			#returning the answer after ceiling
					#MAIN PROGRAM
rooms=int(input('Enter number of rooms:'))	#getting number of rooms from the user
tile_size=int(input("Enter size of tiles in square feet:"))	#to get the size of tiles
main_list=[]					#we will append all lists for rooms  in it to get final list
sum=0						#initializing sum to zero
while rooms>0:					#this loop will ask input for all rooms
    room_list=[]					#we will append room name, length,width and tiles in it.
    room_name=str(input("\nEnter the name of room:"))		#asking user for name of the room.
    room_list.append(room_name)				#appending name in room list		
    length=int(input(f"Enter the length of {room_name}  in feets:"))        #asking user for length of the room
    room_list.append(length)					#appending length in room list
    width=int(input(f"Enter width of the {room_name}  in feets:"))           #asking user for width of the room
    room_list.append(width)					#appending width in room list
    needed_tiles=tiles_in_room(length,width,tile_size)		#calling function to calculate req tiles
    room_list.append(needed_tiles)				#appending req tiles in room list
    print(f'Tiles required for {room_name}: {needed_tiles}') 	#displaying num of tiles req to user
    main_list.append(room_list)					#appending room list in main list 
    sum+=needed_tiles						#to calculate total tiles req for all rooms
    rooms-=1							#to move onto next room
    
print(f'\nTotal number of tiles required for all rooms:{sum}')	#displaying total tiles required to user
tile_boxes=tiles_boxes(sum)					#calling function to calculate req boxes
print(f'Boxes of tiles required :{tile_boxes}')		              #displaying boxes of tiles required to user
unused_tiles=(tile_boxes*25)-sum				#calculating unused tiles
print(f'Number of tiles left un-used :{unused_tiles}')              	#displaying unused tiles to user	
