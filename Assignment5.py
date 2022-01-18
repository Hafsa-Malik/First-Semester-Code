from tabulate import tabulate
import random
import math

def isPowerOfTwo(n):    					#this function will check if input is power of 2
    num=math.log10(n)/math.log10(2) 			#if input is power of 2 num would an integer
    power=math.ceil(num) == math.floor(num)		#true if power of 2 otherwise false
    return power            					#returns true or false depending on input

def win_rate(win,lose):					 #this function will calculate winning rate
    rate=(win/(win+lose))*100
    return round(rate,2) 					#rounding off rate to 2 decimal place

def win_chance(win_rate1,win_rate2):                #this function will calculate winning chance for two teams
    team_1=(win_rate1/(win_rate1+win_rate2))*100
    team_2=(win_rate2/(win_rate1+win_rate2))*100
    return round(team_1,2),round(team_2,2)		 #returning winning chance after rounding off	
def schedule(team_list):        			#this function will create schedule for given teams in list
    temp_list=team_list[:]      			#to duplicate the input list
    print('\n\t\t\t\tSCHEDULE')
    match=1
    while len(temp_list)>0:     
        team_A=random.choice(temp_list)		 #to randomly select a team from list 
        temp_list.remove(team_A)       		 #removing selected team from list to avoid repetition
        team_B=random.choice(temp_list)		 #to randomly selecting second team for match 
        temp_list.remove(team_B)        
        rateA=win_rate(team_A['won'],team_A['lost'])    	#calling function to calculate win rate
        rateB=win_rate(team_B['won'],team_B['lost'])
        win_chanceA, win_chanceB = win_chance(rateA,rateB)	   #calculating  winning chance of both teams
        print('\n\t\t\tMatch',match,':',team_A['Name'],'vs',team_B['Name'])
        header=['Team','won','lost','winning rate(WR)%','winning chance(WC)%'] 	   #for  printing schedule table
        teams_data=[(team_A['Name'],team_A['won'],team_A['lost'],rateA,win_chanceA),
                    (team_B['Name'],team_B['won'],team_B['lost'],rateB,win_chanceB)]
        print(tabulate(teams_data,headers=header, tablefmt='grid')) 	#using tabulate option from tabulate       									  module to print table
        match+=1

def team_details():   					  #this function will ask for team details
    num_teams=int(input("Enter number of teams(only power of two):"))
    if (isPowerOfTwo(num_teams)): 			  #if entered num of teams are power of 2
        teams_list=[]       				#we will append each team's data in it to create teams list
        for i in range(1,num_teams+1): 		 #to get data for each team 
            team_dict={}   				 #to store data in form of dictionary
            print('---------------------------------------------------------------')
            print(f'\t\t Team {i}')
            name=str(input('Enter name of the team:')) 		#get the name of team
            team_dict.update({'Name':name})            			 #adding teams name in team dictionary
            matches=int(input('Enter number of matches played:'))	#to get matches played by team
            team_dict.update({'Matches Played':matches})    		#adding matches played in teams dictionary
            matches_won=int(input('Enter number of matches won:')) 	 #to get matches won by team
            team_dict.update({'won':matches_won})    	#adding matches won by team in team dictionary
            matches_lost=int(input('Enter number of matches lost:'))   	 #to get matches lost by team
            team_dict.update({'lost':matches_lost})    			 #adding mathes lost in team dictinary
            print('---------------------------------------------------------------')
            teams_list.append(team_dict)    				#appending team dictinary in teams list
        return teams_list      					 #returning the teams list
    else:              							 #if entered num of teams are not power of 2
        return 'invalid'
def results(team_list):       		  #this function will ask for results of round and update dictionary
    result_list=[]
    matches=len(team_list)//2
    for match in range(1,matches+1):   		 #asking result for each match in round
        result=str(input(f'match {match} was won by (team name):'))
        result_list.append(result)      		#appending winners name in winners list
    temp_list=team_list[:]             			 #duplicating the teams list
    for team in temp_list:            			  #updating result for each team in round
        team['Matches Played']+=1
        name=team['Name']
        if name in result_list:     			#if team's name is in winners list
            team['won']+=1
        else:                      				 #if team's name isn't in winners list
            team['lost']+=1
            team_list.remove(team) 			 #removing teams that lost the match from teams list
    if len(team_list)==1:           		#for last round of tournament when only 1 team is left as winner
        winner=team_list[0]
        winner_name=winner['Name']
        print(f'\nCongratulations!!Tournament ended with team {winner_name} as winner.')
        return 'match ended'
                               		 #MAIN PROGRAM
list=[]
while True:    				 #to run the program continously until user wants to exit
    print('\nMENU:\npress\nD-to enter team details\nS-to generate schedule\nU-to update results\nX-to exit the program')
    option=str(input('\nPlease choose your option:'))       #to get options from the user
    print()
    if len(list)==0 and option!='D':          #if user selects any option other then teams data when teams list is empty
        if option=='X':                             
            print('You pressed X to exit the program.')
            break
        else:
            print('Invalid choice.You have to enter teams detail first.')
            continue
    if option=='D':   					#if user wants to enter teams detail
        list= team_details() 				
        if list=='invalid':				#if num of teams are not power of 2
            print('Number of teams should be power of two only.Try again.\n')
            list=team_details()				#again ask user to enter num of teams
            continue
        else:						#if num of teams are power of two
            continue
    elif option=='S':   			#if user wants to generate schedule of matches
        schedule(list)
        continue

    elif option=='U':  			 #if user wants to enter result of match
        if results(list)=='match ended':   	 #incase the current tournament ended
            list=[]                        		 #empty the list
            continue
        else:
            continue
    elif option=='X':   			#if user wants to exit program
        print('You pressed X to exit the program.')
        break          				 #break the loop	
