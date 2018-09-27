#adds ability to read and write a json file
import json
import time

occupied = "Occupied"
not_occupied = "Not Occupied"
pool_table_number = ""

# Table class with properties
class PoolTable:
    def __init__(self, pool_table_number, start_date_time = 0, end_date_time = 0):
        self.pool_table_number = pool_table_number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.total_time_played = self.end_date_time - self.start_date_time
    
    # Turns the classes into a dictionary
    def as_dictionary(self):
        return self.__dict__

    # offer options to the user
    def pool_table_manager(self):
        pass


    # Returns and prints the table and if it is occupied or not based on start date time
    def occupancy(self, start_date_time = 0):
        occupancy = ""
        if (start_date_time == 0):
            print(f"Table {self.pool_table_number} - {not_occupied}")
            return not_occupied

        else:
            print(f"Table {self.pool_table_number} - {occupied}")
            return occupied


#prints the current status of all the pool tables at one time
def view_table_statuses(all_pool_tables):
    with open("pool_table_data.json", "r") as json_object:

    #print occupancy of each table
        for pool_table in all_pool_tables:
            pool_table.occupancy()




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

    #rewrites all of the data in the json file with new values
    if (user_input == 'y'):
        with open("pool_table_data.json", "w") as json_object:
            data=[]
            for pool_table in all_pool_tables:
                data.append(pool_table.as_dictionary())
            json.dump(data,json_object)
        choose_table()


    elif (user_input == 'n'):
            #confirms if a user doesnt want to start a new game
            print("Are you sure you don't want to start a new game?")
            user_input_check = input("Enter 'y' for yes or 'n' for no: ")

            if (user_input_check == 'n'):
                new_game()
            
            elif (user_input_check == 'y'):
                print("thank you for coming")

    # restarts the menu if an invalid option is entered        
    else:
        print("That was an invalid option.")
        new_game()
#takes in a user input to choose the table number.
def choose_table():
    table_selection = int(input("Enter the table number: "))

    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.loads(json_object.read())
        print(pool_table_number[0]["pool_table_number"])

        # withdraw the specific tables data occupancy
        if (table_selection == pool_table_number[table_selection - 1]["pool_table_number"]):
            occupancy = all_pool_tables[table_selection - 1].occupancy()
            print(occupancy)

            if (occupancy == occupied):
                print("Table is occupied. choose a new table")
                choose_table()
                
            if (occupancy == not_occupied):
                #start the start time date
                #save that data into the json
                print("This table is free")

        else:
            print("its not working")






print("Pool Table Manager Active")

print(" - Table Statuses")


view_table_statuses(all_pool_tables)

new_game()
