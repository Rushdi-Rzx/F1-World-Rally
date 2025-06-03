  #CM 1601 Programing Fundementals Coursework

#Student Name - Mohideen Mohamed Rushdi
#RGU ID - 2237950

#-----creating the function-----

def console_menu(): #Function to display the console menu when launched the program
    print("Type ADD for adding driver details")
    print("Type DDD for deleting")
    print("Type UDD for updating driver details")
    print("Type VCT for viewing the rally cross standings table")
    print("Type SRR for simulating a random race")
    print("Type VRL for viewing race table sorted according to the date")
    print("Type STF to save the current data to a text file")
    print("Type RFF to load data from the saved text file")
    print("Type ESC to exit the program. ")
    print("")
    sleep(0.50)

#If user typed ADD
def add_driver_details(): #Function to enter driver details
    driver_details = [] #This list is to add new driver details which is entered by the user
    driver_name = input("Enter Driver name :- ") #Getting user input(Driver's name)
    check_driver_name = False #This variable is to confirm that there's no other drivers with the same exiting name
    for i in range(0, len(main_list)):
        if (main_list[i][0] == driver_name):  # This checks the names from the main_list one by one and finds duplicate names
            sleep(0.50)
            print("")
            print("The name you entered already exists. Use the UDD option to update the driver or select the ADD option and enter a valid driver name. ")  # A message to the user
            heading = ["Name            ", "Age             ", "Team            ", "Car             ", "Current Points  "]
            sleep(0.50)
            print("\n", heading[0], "-    ", main_list[i][0], "\n", heading[1], "-    ", main_list[i][1], "\n"
                  , heading[2], "-    ", main_list[i][2], "\n", heading[3], "-    ", main_list[i][3], "\n", heading[4]
                  , "-    ", main_list[i][4]) #This prints a table with the existing driver details 
            print("")
            print("")
            check_driver_name = True #This variable is to confirm that there are drivers with the same exiting name
            select()
    if check_driver_name == False: #This variable is to confirm that there's no other drivers with the same exiting name
        while True: #Creating a loop to keep asking the age when user input invalid type of value
            driver_age = input("Enter Driver age :- ")#Getting user input(Driver's age)
            try:
                driver_age = int(driver_age) #Convert the user input into an integer (if the user input anything other than a number, error will pop up)
                if driver_age > 0: #age shouldn't be a negative value
                    break
            except:
                sleep(0.50)
                print("")
                print("The Age you entered is incorrect, please enter a valid Age.") #This prints if the user input anything other than a number or an invalid output
                print("")
        driver_team = input("Enter Driver team :- ") #Getting user input(Driver's team)
        driver_car = input("Enter Driver's car :- ") #Getting user input(Driver's car)
        while True: #Creating a loop to keep asking the current points when user input invalid type of value
            driver_current_points = input("Enter Driver current points :- ") #Getting user input(Driver's current points)
            try:
                driver_current_points = int(driver_current_points) #Convert the user input into an integer (if the user input anything other than a number, error will pop up)
                if driver_current_points > 0: #current points shouldn't be a negative value
                    break
            except:
                sleep(0.50)
                print("")
                print("The current driver points you entered is incorrect, please enter a valid point. ") #This prints if the user input anything other than a number or an invalid output
                print("")
    driver_details.append(driver_name) #This adds the user input values into the driver_details list
    driver_details.append(driver_age) #This adds the user input values into the driver_details list
    driver_details.append(driver_team) #This adds the user input values into the driver_details list
    driver_details.append(driver_car) #This adds the user input values into the driver_details list
    driver_details.append(driver_current_points) #This adds the user input values into the driver_details list
    main_list.append(driver_details) #This adds the driver_details list into the main_list list.
    print("")
    sleep(0.50)
    print("Driver Added Successfully.")
    sleep(0.50)
    print("")
    #referred links - https://www.geeksforgeeks.org/python-lists/
    #referred links - https://www.w3schools.com/python/python_lists_loop.asp
    #referred links - https://www.w3schools.com/python/python_try_except.asp
    console_menu()#Display the console menu
    select() #To ask the user again to select an option


#If user typed DDD
def delete_driver(): #Function to delete a driver by searching the name
    sleep(0.50)
    deleting_driver = str(input("Enter deleting driver's name : "))#To get the name that user wants to delete
    for driver_details in main_list:#this is loop to check each element of the driver_details list in the main_list
        if deleting_driver in driver_details:#this checks if the user input name is in the driver_details list
            index = main_list.index(driver_details)#this is to get the index number of the deleting_driver from the driver_details list and check which index it is in the main_list
            main_list.pop(index)#this removes the driver details from the main_list
            print("")
            sleep(0.50)
            print("Driver Deleted Successfully")#A message to the user
            print("")
            break #break the for loop after deleting the driver
    else:
        print("")
        sleep(0.50)
        print("Delete unsuccessful, Please enter a valid name and Try again")#A message to the user
        print("")
        sleep(0.50)
        print("Returning to the console menu...")
        sleep(1)
        print("")
        console_menu()#Display the console menu
        select()  # To ask the user again to select an option
    # referred links - https://www.geeksforgeeks.org/python-lists/
    sleep(0.50)
    console_menu()#Display the console menu
    sleep(0.50)
    select() #To ask the user again to select an option


#If user typed UDD
def update_driver(): #Function to allow the user to update driver details by searching the name
    try:
        sleep(0.50)
        updating_driver = input("Enter the driver's name to update :- ")#To get the name that user wants to update
        print("")
        for driver_details in main_list:
            assert driver_details[0] != updating_driver #to go into the expect part
    except:
        index = main_list.index(driver_details) #to get the index of the driver that have to update
        driver_details = [] #making an empty list to insert updating details
        sleep(0.50)
        updating_name = str(input("Enter Driver name :- ")) #getting the update name
        for i in range(0, len(main_list)): #loop to check the list details one by one
            while (main_list[i][0] == updating_name): #loop to check the update name is already taken or not
                sleep(0.50)
                print("Name already exists. please enter a valid name!")
                sleep(0.50)
                updating_name = input("Enter driver's name: ") #getting the update name

        while True:
            updating_age = input("Enter Driver age :- ") #getting the update age
            try:
                updating_age = int(updating_age)#Convert the user input into an integer (if the user input anything other than a number, error will pop up)
                if updating_age > 0:#age shouldn't be a negative value
                    break
            except:
                sleep(0.50)
                print("The Age you entered is incorrect, please enter a valid Age.")

        updating_team = str(input("Enter driver's team: "))#getting the update team

        updating_car = str(input("Enter driver's car: "))#getting the update car

        while True:
            updating_current_points = input("Enter Driver current points :- ")#getting the update current points
            try:
                updating_current_points = int(updating_current_points)#Convert the user input into an integer (if the user input anything other than a number, error will pop up)
                if updating_current_points > 0:#current points shouldn't be a negative value
                    break
            except:
                sleep(0.50)
                print("The current driver points you entered is incorrect, please enter a valid point. ")

        driver_details.append(updating_name)#This adds the user input values into the driver_details list
        driver_details.append(updating_age)#This adds the user input values into the driver_details list
        driver_details.append(updating_team)#This adds the user input values into the driver_details list
        driver_details.append(updating_car)#This adds the user input values into the driver_details list
        driver_details.append(updating_current_points)#This adds the user input values into the driver_details list
        main_list[index] = driver_details#This makes the selected main_list index to the driver_details list
        print("")
        sleep(0.50)
        print("Driver Updated Successfully.")
        print("")
    else:  # if try fails to run else won't run
        print("")
        sleep(0.50)
        print("The name you entered does not exist, Please Try again")
        print("")
        sleep(0.50)
        update_driver()
    # referred links - https://www.w3schools.com/python/python_lists_loop.asp
    # referred links - https://www.w3schools.com/python/python_try_except.asp
    sleep(0.50)
    console_menu()#Display the console menu
    select() #To ask the user again to select an option

#If user typed VCT
def view_standing_table(): #To display the championship standings ordered by points in descending order
    length = len(main_list)
    for i in range(0,length):
        for j in range(0,length -i -1):
            if main_list[j][4]<main_list[j+1][4]:
                temp=main_list[j]
                main_list[j]=main_list[j+1]
                main_list[j+1]=temp
    #This code is referred by the link - https://linuxhint.com/sort-nested-list-python/
    #Author - Kalsoom Bibi
    sleep(0.50)
    from tabulate import tabulate #import the tabulate library to make a table
    head = ["Name","Age","Team","Car","Points"] #table head
    print(tabulate(main_list, headers=head, tablefmt="fancy_grid"))
    # This code is referred by the link - https://www.askpython.com/python-modules/tabulate-tables-in-python
    print("")
    sleep(0.50)
    console_menu() #Display the console menu
    select() #To ask the user again to select an option


#If user typed SRR
def simulate_random_race(): #Function to simulate a random race and assign points to each driver accordingly
    global race_date #making the race_date variable global
    import random #importing the random library to select a random location
    while race_date < 32:
        race_location = ["Nyirád", "Höljes","Montalegre", "Barcelona", "Riga", "Norway"] #a list to store the given locations
        file = open("data.txt", "a+")  # opening the data.txt file and a+ is used for appending and reading
        file.write("\n") #going into the next line
        file.write("\n") #going into the next line
        file.write("Location :- ")
        file.write(str(race_location[random.randint(0,5)])) #sleceting a random location from race_location list and writing it on the text file
        file.write("\t\t\tDate :- 2022 SEPTEMBER ") #\t is used for the tab spaces
        file.write(str(race_date)) #writing the date race
        race_date = race_date + 1 #going to the next day race
        file.write("\n") #going into the next line
        length=len(main_list)
        random.shuffle(main_list)  #to shuffle the main_list indexes
        #referred by the link - https://www.w3schools.com/python/ref_random_shuffle.asp
        for i in range(1,length+1): #going into the indexes after shuffling the list
            if i == 1:
                file.write("\nPosition :- ")
                file.write(str(i)) #this prints 1
                file.write("\t\t\t")#tab spaces
                file.write(main_list[0][0]) #this prints the name of the driver
                file.write("\t\t\tPoints :- 10")
                main_list[0][4]=main_list[0][4]+10 #this adds the race points into the current points
            elif i == 2:
                file.write("\nPosition :- ")
                file.write(str(i))#this prints 2
                file.write("\t\t\t") #tab spaces
                file.write(main_list[1][0]) #this prints the name of the driver
                file.write("\t\t\tPoints :- 7")
                main_list[1][4] = main_list[1][4] + 7 #this adds the race points into the current points
            elif i == 3:
                file.write("\nPosition :- ")
                file.write(str(i))#this prints 3
                file.write("\t\t\t") #tab spaces
                file.write(main_list[2][0]) #this prints the name of the driver
                file.write("\t\t\tPoints :- 5")
                main_list[1][4] = main_list[1][4] + 5 #this adds the race points into the current points
            else: #if there's no drivers left
                file.write("\nPosition :- ")
                file.write(str(i)) #this prints 0
                file.write("\t\t\t") #tab spaces
                file.write(main_list[i-1][0])
                file.write("\t\t\tPoints :- 0")
                main_list[i-1][4] = main_list[i-1][4] + 0 #this adds the race points into the current points
        file.close() #closing the data.txt file
        break
    #referred link - https://www.w3schools.com/python/python_file_handling.asp
    #referred link - https://www.programiz.com/python-programming/file-operation
    #referred link - https://www.geeksforgeeks.org/file-handling-python/
    #referred link - https://www.youtube.com/watch?v=DmHSwTiD5Tk
                    #channel link - https://www.youtube.com/@SimplilearnOfficial

    sleep(0.50)
    print("")
    print("Simulating a random race.")
    sleep(1)
    print("")
    print("Race simulated successfully and saved in data.txt")
    print("")
    sleep(0.50)
    print("Returning to the main menu...")
    sleep(1)
    console_menu() #Display the console menu
    select() #To ask the user again to select an option

#If user typed VRL
def view_race_table(): #Function to display all the races in the championship sorted according to the date
    sleep(0.50)
    print("")
    print("Viewing the race details")
    sleep(0.50)
    print("")
    file = open("data.txt", "r") #opening the data.txt file to read
    print("File name :- ", file.name) #showing the user the file name
    print(file.read()) #displaying the document in the console
    sleep(0.50)
    print("")
    print("Race details loaded...")
    sleep(0.50)
    print("")
    print("Returning to the main menu...")
    print("")
    sleep(0.50)
    console_menu() #Display the console menu
    select() #To ask the user again to select an option
    # referred link - https://w3schools.com/python/python_file_handling.asp
    # referred link - https://www.programiz.com/python-programming/file-operation
    # referred link - https://www.geeksforgeeks.org/file-handling-python/
    # referred link - https://www.youtube.com/watch?v=DmHSwTiD5Tk
    # channel link - https://www.youtube.com/@SimplilearnOfficial

#If user typed STF
def save_data(): #Function to save the current data to a text file in a way that the data can be retrieved easily
    length = len(main_list) #hetting the length of the main_list
    gap = ''*3 #a variable to make spaces in the table
    equal_line = '=' * 110 #a variable to make a line with the equal symbol
    single_line = '-' * 110 #a variable to make a line with the line symbol
    stf = open("stf.txt", "a+")  # opening the stf.txt file and a+ is used for appending and reading
    rec = f"{'Name' :30s}{gap}{'Age':10s}{gap}{'Team':30s}{'Car':20s}{'Points':5s}" #the table head
    stf.write(equal_line) #writing the equal lines using the equal_line variable
    stf.write("\n") #going into the next line
    stf.write(rec) #writing the table head
    stf.write("\n") #going into the next line
    stf.write(equal_line)#writing the equal lines using the equal_line variable
    stf.write("\n") #going into the next line
    for i in range(0, length):
        rec_1 = f"{main_list[i][0]:30s}{gap}{str(main_list[i][1]):10s}{gap}{main_list[i][2]:30s}{gap}" \
                f"{main_list[i][3]:20s}{gap}{str(main_list[i][4]):5s}" #variable to get the driver_list items in the main_list
        stf.write("\n") #going into the next line
        stf.write(rec_1) #writing driver_list items in the main_list
        stf.write("\n") #going into the next line
        stf.write(single_line)#writing the single lines using the single_line variable
        stf.write("\n") #going into the next line
    stf.close() #closing the stf.txt file
    # This code is referred by the link - https://www.youtube.com/watch?v=fsBslGyCeYI
    # Author's Channel  - https://www.youtube.com/@LearnWithYK
    print("")
    print("Data is saving...")
    print("")
    sleep(1)
    print("Data saved successfully")
    sleep(1)
    print("")
    print("Returning to the menu...")
    sleep(1)
    print("")
    console_menu() #Display the console menu
    select() #To ask the user again to select an option
    # referred link - https://w3schools.com/python/python_file_handling.asp
    # referred link - https://www.programiz.com/python-programming/file-operation
    # referred link - https://www.geeksforgeeks.org/file-handling-python/
    # referred link - https://www.youtube.com/watch?v=DmHSwTiD5Tk
    # channel link - https://www.youtube.com/@SimplilearnOfficial

#If user typed RFF
def load_data(): #Function to load the current data from the text file to enable resume capabilities
    print("Driver Details")
    stf = open("stf.txt","r") #opening the stf.txt file to read
    print("File Name : ", stf.name) #displaying the file name
    display = stf.read()
    print(display) #displaying the contents in the stf.txt file
    sleep(1)
    print("To edit the file go back to main menu and select your option")
    print("")
    sleep(1.5)
    print("Returning to the main menu...")
    sleep(1)
    console_menu() #Display the console menu
    select() #To ask the user again to select an option
    # referred link - https://w3schools.com/python/python_file_handling.asp
    # referred link - https://www.programiz.com/python-programming/file-operation
    # referred link - https://www.geeksforgeeks.org/file-handling-python/
    # referred link - https://www.youtube.com/watch?v=DmHSwTiD5Tk
    # channel link - https://www.youtube.com/@SimplilearnOfficial

#If user typed ESC
def exit_program(): #Function to exit the program
    print("")
    print("Closing the program...")
    sleep(2)
    exit() #this exits the program

def select(): #Function to let the user to select an option
    option = input(str("Please select your option :- ")) #getting usere's option
    print("")
    if option == "ADD" :
        add_driver_details()

    elif option == "DDD" :
        delete_driver()

    elif option == "UDD" :
        update_driver()

    elif option == "VCT" :
        view_standing_table()

    elif option == "SRR" :
        simulate_random_race()

    elif option == "VRL" :
        view_race_table()

    elif option == "STF" :
        save_data()

    elif option == "RFF" :
        load_data()

    elif option == "ESC" :
        exit_program()

    else :
        sleep(0.50)
        print("Invalid option, please try again.")
        sleep(0.50)
        print("")
        console_menu() #Display the console menu
        print("")
        select() #To ask the user again to select an option


#-----time-----
import time #importing the time library
from time import sleep #to delay the texts when displaying

#-----list-----
main_list = [['John', 24, 'Team Alpha', 'Toyota', 67], ['Simon', 27, 'Team Beta', 'Audi', 89], ['Josh', 31, 'Team Gama', 'Ford', 76]] #this list is to store all the driver details

#-----files-----
file = 0
file = open("data.txt","a+") # opening the data.txt file and a+ is used for appending and reading
print(file.read())


#-----main program-----

print("=====WORLD RALLY CROSS CHAMPIONSHIP MANAGEMENT=====")
sleep(0.5)
print("")
race_date=1
console_menu() #Display the console menu
print("")
select() #To ask the user again to select an option
