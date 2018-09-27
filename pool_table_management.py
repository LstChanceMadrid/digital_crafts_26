#adds ability to read and write a json file
import json
import datetime

occupied = "Occupied"
not_occupied = "Not Occupied"
pool_table_number = ""


# Table class with properties
class PoolTable:
    def __init__(self, pool_table_number, start_date_time = "0", end_date_time = "0"):
        self.pool_table_number = pool_table_number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.total_time_played = int(self.end_date_time) - int(self.start_date_time)
    
    # Turns the classes into a dictionary
    def as_dictionary(self):
        return self.__dict__

    # offer options to the user
    def pool_table_manager(self):
        pass


    # Returns and prints the table and if it is occupied or not based on start date time

          
            



def view_table_statuses(all_pool_tables):

    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.loads(json_object.read())

    #print occupancy of each table
        for pool_table in pool_table_number:

            if (pool_table["start_date_time"] == "0"):
                print(f"Table {pool_table['pool_table_number']} - {not_occupied}")

            else:
                print(f"Table {pool_table['pool_table_number']} - {occupied}")





# all 12 of the pool classes
pool_table_1 = PoolTable(1)
pool_table_2 = PoolTable(2)
pool_table_3 = PoolTable(3)
pool_table_4 = PoolTable(4)
pool_table_5 = PoolTable(5)
pool_table_6 = PoolTable(6)
pool_table_7 = PoolTable(7)
pool_table_8 = PoolTable(8)
pool_table_9 = PoolTable(9)
pool_table_10 = PoolTable(10)
pool_table_11 = PoolTable(11)
pool_table_12 = PoolTable(12)

# a list containing all the pool tables
all_pool_tables = [pool_table_1, pool_table_2, pool_table_3, pool_table_4, pool_table_5, pool_table_6, pool_table_7, pool_table_8, pool_table_9, pool_table_10, pool_table_11, pool_table_12]

#prompts user if starting a new game
def new_game():
    print("Would you like to start a new game?")
    user_input = input("Enter 'y' for yes or 'n' for no: ")

   
    if (user_input == 'y'):
        print("")
        view_table_statuses(all_pool_tables)
        print("")
        
        choose_table()


    elif (user_input == 'n'):
            #confirms if a user doesnt want to start a new game
            print("Are you sure you don't want to rent this table?")
            user_input_check = input("Enter 'y' for yes or 'n' for no: ")

            if (user_input_check == 'n'):
                new_game()
            
            elif (user_input_check == 'y'):
                print("thank you for coming")
                print("")
                view_table_statuses(all_pool_tables)
                new_game()

    # restarts the menu if an invalid option is entered        
    else:
        print("That was an invalid option.")
        print("")
        new_game()

#takes in a user input to choose the table number.
def choose_table():
    print("")
    table_selection = int(input("Enter an available table number: "))
    

# NOT USEDturn the dictionaries back to an object
    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.load(json_object)
        #NOT USEDfor pool_table in pool_table_number
        #NOT USEDname_of_the_table = pool_table["name"]
        #NOT USEDsame_pool_table = PoolTable(name_of_the_table)
        print(pool_table_number[table_selection - 1]["pool_table_number"])
        occupancy = pool_table_number[table_selection - 1]["start_date_time"]
        # withdraw the specific tables data occupancy
        if (occupancy != "0"):
            
            print("This table is occupied")
            print(occupancy)
            choose_table()

                
        if (occupancy == "0"):
            rent = input("Would you like to rent this table? 'y'/'n': ")
            if (rent == 'y'):
                pool_table_number[table_selection - 1]["start_date_time"] = datetime.datetime.now().time().strftime('%H:%M:%S')
                start_time = pool_table_number[table_selection - 1]["start_date_time"]
                print("good to go")
                print(start_time)
                print("")

   
                with open("pool_table_data.json", "w") as json_object:
                    json.dump(pool_table_number, json_object)
            elif (rent == 'n'):

                choose_table()
            else:
                print("That was an invalid option.")
                choose_table()
            

    
            

    
                    
                
                

                #start the start time date
                #save that data into the json
        print("You have now rented this table!")
        print(f"Your start time is ")
        new_game()








print("")

print("Pool Table Manager Active")

print("")

print(" - Table Statuses")

print("")

view_table_statuses(all_pool_tables)

print("")

print(f"Current time is - {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")

print("")

new_game()
