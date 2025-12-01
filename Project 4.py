#Project 4
#Andrew Blanchard

#A neat idea I had to save time while testing, just import random to do it most of the tedious work for me
import random
randomPlaneTwoCharacterList = ["AA", "DL", "UA", "EA", "SW", "NW", "NE", "SE", "UN", "JA"]
randomOriginList = ["LAS", "MDW", "RNO", "STL"]
randomDestinationList = ["BOS", "SLC", "MHT", "MCO"]

#This just creates the mostly random flight numbers you see
def createRandomFlightNumber():
    randomNameCharacters = random.choice(randomPlaneTwoCharacterList)
    randomNameNumbers = str(random.randint(100,999))
    #For this purpose, I am just making this to save time. The likelyhood they are the same is just so small.

    NewFlightNumber = randomNameCharacters + randomNameNumbers
    return NewFlightNumber

#Imports heapq
import heapq
priorityQ = []
orderOfRequest = 0

#This creates a new plane landing or departure request
def new_plane_request(x):
    priority = int(input("\nEnter the priority level of this task. \n1 = Emergency Landing \n2 = Urgent Schedule \n3-10 = Routine Operations \n\n\tENTER HERE: "))
    description = createRandomFlightNumber()
    print(f"\nLatest called in and approved flight number *{description}* detected, automatic input.")
    travelStatus = str(input("Enter whether plane is: Arrival or Departure. \n\n\tENTER HERE: "))
    origin = random.choice(randomOriginList)
    destination = random.choice(randomDestinationList)
    x += 1

    new_task =(priority, x, description, travelStatus, origin, destination) #create the new task as a tuple

    heapq.heappush(priorityQ, new_task) #this ensures that when we add a new task, the list pq remains a minimum heap
    if(priority == 1):
        print(f"\nEMERGENCY, FLIGHT NUMBER *{description}* NEEDS TO LAND ASAP to {destination}; origin: {origin}")
    elif(priority == 2):
        print(f"\nUrgent, NOT Emergency, Flight Number *{description}* needs swifter landing ASAP to {destination}; origin: {origin}")
    else:
        print(f"\nFlight with a priority of {priority}, flight number of *{description},* travel status {travelStatus}, \nwith the origin as {origin}, and destination as {destination}, has been succesfully added!")
    return x

#This just sees the next plane ready to land in the first slot of the priority
def peek_next_plane():
    if priorityQ:
        print(f"\nThe next plane has a priority of {heapq.nsmallest(1, priorityQ)[0][0]} and has the flight number: *{heapq.nsmallest(1, priorityQ)[0][2]}.*")
    else:
        print("\nYour priority list has no planes in it.")

#This completes the next plane in the list of priority
def process_plane():
    if priorityQ:
        completed_task = heapq.heappop(priorityQ) #This pops the highest-priority plane while keeping our pq a minimum heaep
        if(completed_task[0] == 1 or completed_task[0] == 2):
            print(f"\nPHEW, crisis averted. Priority of {completed_task[0]}. Flight *{completed_task[2]}* has {completed_task[3]} safely to {completed_task[5]}; origin: {completed_task[4]}")
        else: 
            print(f"\nPriority of {completed_task[0]}. Flight *{completed_task[2]}* has {completed_task[3]} safely to {completed_task[5]}; origin: {completed_task[4]}")
    else:
        print("\nYour priority list has no planes in it.")

#This displays al of the planes in the list
def print_waiting_plane_list():
    if priorityQ:
        for plane in priorityQ:
            print(plane)
            print("--------------------------------------------------------------------------------------------\n")
    else:
        print("\nYour priority list has no planes in it.")

#I had fun making this code complex in a fun way!
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main Code:
name = input("\n\tEnter username to enter One Runway Airport Priority Queue System. Enter name HERE: ")
while(True):
    print(f"\n\nHello {name}! This is the plane priority queue management system: \n-------------------------------------------------------------------------------------------- \nPress 1 to *Create a new plane request.* \tPress 2 to *View next scheduled plane.* \nPress 3 to *Dispatch next plane.* \t\tPress 4 to *Show all planes in queue.* \nPress 5 to *Exit the program.*")
    value = int(input("\n\tEnter Number HERE: "))
    if(value <= 5 and value >= 1):
        #Calls on the functions depending on what number was input.
        if(value == 1):
            orderOfRequest = new_plane_request(orderOfRequest)
        elif(value == 2):
            peek_next_plane()
        elif(value == 3):
            process_plane()
        elif(value == 4):
            print_waiting_plane_list()
        elif(value == 5):
            value2 = input("\n\tAre you sure you want to quit? Y or N. Enter HERE: ")
            if (value2 == "Y" or value2 == "y" or value2 == "yes" or value2 == "Yes" or value2 == "YES"):
                print("\nLeaving Program, thank you!\n-------------------------------")
                break
            else:
                print("\nProgram exit canceled. Program resuming... \n-----------------------------------------")
    else:
        print("\nTry Again, invalid selection \n-------------------------------")