import json
import datetime


current_time_hour_minute =f"{datetime.datetime.now().strftime('%H:%M:%S')}"

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
    

    def as_dictionary(self):

        return self.__dict__


def pool_table_manager():
    print("")

    print(" -- Pool Table Manager --")

    print("")

    print(" - Table Statuses")


    print("")
    view_table_statuses(all_pool_tables)
    print("")
    print("Press 'R': Rent a table")
    print("Press 'E: End rental")
    print("")
    print("How May I Help You?")

    option = input("Enter desired option: ")

    if (option.lower() == 'r'):
        new_game()

    elif (option.lower() == 'e'):
        end_game()

    else:
        print("That is an invalid option.")
        print("Try again")
        pool_table_manager()



def view_table_statuses(all_pool_tables):

    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.loads(json_object.read())

    #print occupancy of each table
        for pool_table in pool_table_number:

            if (pool_table["start_date_time"] == "0"):
                print(f"Table {pool_table['pool_table_number']} - {not_occupied}")

            else:
                print(f"Table {pool_table['pool_table_number']} - {occupied} {datetime.datetime.strptime(pool_table['start_date_time'], '%H%M%S').time()}")

    print("")
    print(f"Current time is - {current_time_hour_minute}")


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


all_pool_tables = [pool_table_1, pool_table_2, pool_table_3, pool_table_4, pool_table_5, pool_table_6, pool_table_7, pool_table_8, pool_table_9, pool_table_10, pool_table_11, pool_table_12]


def new_game():

    print("")
    print("Would you like to start a new game?")
    user_input = input("Y/N?: ")

   
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

    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.load(json_object)

        print(f"Table {pool_table_number[table_selection - 1]['pool_table_number']}")
        occupancy = pool_table_number[table_selection - 1]["start_date_time"]
        # withdraw the specific tables data occupancy
        if (occupancy != "0"):
            
            print("This table is occupied")
            print(occupancy)
            choose_table()

                
        if (occupancy == "0"):
            rent = input("Would you like to rent this table? 'y'/'n': ")

            if (rent == 'y'):
                start = datetime.datetime.now()
                pool_table_number[table_selection - 1]["start_date_time"] = start.strftime('%H%M%S')
                start_time = pool_table_number[table_selection - 1]["start_date_time"]
                print("good to go")
                print("")

   
                with open("pool_table_data.json", "w") as json_object:
                    json.dump(pool_table_number, json_object,indent=4)

            elif (rent == 'n'):

                choose_table()
            else:
                print("That was an invalid option.")
                choose_table()
            
        print("You have now rented this table!")
        print(f"Your start time is {start.strftime('%H:%M')}")

        pool_table_manager()


def end_game():

    print("Are you sure you want to end your session?")

    user_input = input("Y/N?: ")

    if (user_input.lower() == 'y'):
        end_table()

    elif (user_input.lower() == 'n'):
        pool_table_manager()

    else:
        print("That is an invalid option.")


def end_table():

    print("")

    table_selection = int(input("Enter your current table number: "))

    with open("pool_table_data.json", "r") as json_object:
        pool_table_number = json.load(json_object)

        print(f"Table {pool_table_number[table_selection - 1]['pool_table_number']}")

        occupancy = pool_table_number[table_selection - 1]["start_date_time"]

        # withdraw the specific tables data occupancy
        if (occupancy == "0"):
            print("This table is not occupied")
            print(occupancy)
            end_table()

                
        if (occupancy != "0"):
            end = input("Would you like to end this table rental? 'y'/'n': ")

            if (end == 'y'):
                end = datetime.datetime.now()
                pool_table_number[table_selection - 1]["end_date_time"] = end.strftime('%H%M%S')
                end_time = pool_table_number[table_selection - 1]["end_date_time"]

                print("good to go")
                print(end_time)
                
                #pool_table_number[table_selection - 1]["total_time_played"]#= pool_table_number[table_selection - 1]["end_date_time"] #- pool_table_number[table_selection - 1]["start_date_time"]
                end = datetime.datetime.strptime(pool_table_number[table_selection - 1]["end_date_time"], "%H%M%S").time()
                start = datetime.datetime.strptime(pool_table_number[table_selection - 1]["start_date_time"], "%H%M%S").time()
                    
                print(end)
                total_1 = datetime.datetime.combine(datetime.date.today(), end) - datetime.datetime.combine(datetime.date.today(), start)

                print(total_1)
                total_1 = str(total_1)

                #total_1 = repr(datetime.datetime.strptime(total_1, "%H:%M:%S").time())
                #total_1 = datetime.datetime.time(pool_table_number[table_selection - 1]["start_date_time"].strftime('%H%M%S'))
                pool_table_number[table_selection-1]["total_time_played"] = total_1
                
                

                with open("pool_table_data.json", "w") as json_object:
                    json.dump(pool_table_number, json_object,indent=4)


                history_list = []
                with open("pool_table_history.json", "r") as json_object:
                    history = json.load(json_object)
                    history_list = history
                    finished_table = pool_table_number[table_selection - 1]
                    history_list.append(finished_table)


                with open("pool_table_history.json", "w") as json_object:
                    
                    
                    json.dump(history_list, json_object, indent=4)
                    

                pool_table_number[table_selection - 1]["start_date_time"] = "0"
                    
                pool_table_number[table_selection - 1]["end_date_time"] = "0"

                pool_table_number[table_selection - 1]["total_time_played"] = "0"
                with open("pool_table_data.json", "w") as json_object:
                    json.dump(pool_table_number, json_object,indent=4)


            elif (end == 'n'):
                pool_table_manager()

            else:
                print("That was an invalid option.")
                pool_table_manager()


# will completely reset all data inside of the pool_table_data.json file to its base state (DELETES ALL DATA!)
def reset_data():

    with open("pool_table_data.json", "w") as json_object:
        data = []

        for table in all_pool_tables:
            data.append(table.as_dictionary())

        json.dump(data, json_object,indent=4)




pool_table_manager()
