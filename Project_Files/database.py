import mysql.connector
from time import sleep  # For Delays
import os               # Find alternative for clear screen

# Replace with your own
mydb = mysql.connector.connect(
    host='-- Input your hostname--',  
    user='-- input your user--',
    password='-- input your password',
)


class data_():
    '''
    1. Initializes mycursor so you can call it on every function
    2. dict_users = {} shows you all available users
    3. user_id = {] used to join User_id and collection_id
    4. id_number = basis for join

    '''
    def __init__(self):
        self.mycursor = mydb.cursor()
        self.dict_users = {}
        self.user_id = {}
        self.id_number = 0


    '''
       Check's main purpose : Username / Password Matching  
    '''
    def check(self):

        self.mycursor.execute("USE passwords")    # Uses table
        self.mycursor.execute("select username,password,users_id from users ") # selecting username & password info from users
        result = self.mycursor.fetchall()
        self.dict_users = {x[0]: x[1] for x in result}  # username: password        || initializes Username and password into dictionary
        self.user_id = {x[0]: x[2] for x in result}  # username : users_id
        return self.dict_users



    '''
     Gives the Statistics of the user ( Name, Age,)
    '''
    def match(self,id):

        self.id = id
        self.id_number = self.user_id.get(self.id)
        self.mycursor.execute(f'select first_name, last_name from user_info where info_id = "{self.id_number}"')
        result = self.mycursor.fetchall()
        return result


    '''
    1. Main Bulk of the program
    2. Recursively calls caller to initiate different options until you want to exit
    3. Ability to call ADD, EDIT, DELETE function
    4. Shows a dashboard of your collection.
    '''

    def caller(self):
        # TODO = Password Hashing

        self.mycursor.execute(f'select Entity, username, password from collection where collection_id = "{self.id_number}"')
        result = self.mycursor.fetchall()
        print('-----------Structure-----------------------')
        print("Index# |  Entity  |   Username  |   Password")
        print('-------------------------------------')

        result_list = [x for x in result]
        print(result_list)
        print(len(result_list))
        for num, val in enumerate(result):
            print(num, val[0],"  |  ", val[1], "   |   ", val[2])
        print('----------END---------')
        print('----------------------')
        print("What do you want do?")
        print("Options: (A) Add / (E) Edit / (D) Delete / (L) Leave")
        option_ask = True
        while option_ask:
            answer = input("Please input your answer: ")
            if answer in "AEDL":
                option_ask = False
            else:
                print("Please choose from the choices")
                option_ask = True

        if answer.upper() == "A":             # Process for adding
            answer = self.ask_mediator()
            if answer.upper() == 'Y':
                self.add()
                self.caller()
            else:
                # Todo: Add Delay, and clear list
                print('Okay, Going back...')
                self.caller()
                return 0
        elif answer.upper() == "D":           # Process for deleting
            answer = self.ask_mediator()
            if answer.upper() == 'Y':
                delete_ask = True
                while delete_ask:
                    print("Please input Index # of the row you want to delete, starts at 0")  # IN stands for index number
                    IN = int(input('If you want to exit, type "-1" if you want to exit.:  '))

                    if IN >= 0 and IN < len(result_list):
                        self.delete_(result_list[IN][0], result_list[IN][1], result_list[IN][2])
                        self.caller()
                        delete_ask = False
                    elif IN == -1:
                        ask_ = self.ask_mediator()
                        if ask_.upper() == 'Y':
                            print('Understood, returning to dashboard')
                            delete_ask = False
                            self.caller()
                        elif ask_.upper() == 'N':
                            print('Okay, returning delete process')
                            delete_ask = False
                    else:
                        print("Please input number in valid range and make sure it is a digit")
                        print('If you want to exit, please type the letter "E" ')
                        delete_ask = True
            elif answer.upper() == 'N':
                # Todo: add time.sleep() and clear list
                print('Okay, undestood. Going back')
                sleep(2)
                # os.system('cls') # Todo: system clear not working look for alternatives.
                print('Clearing list')
                sleep(2)
                self.caller()
        elif answer.upper() == "E":  # for editing password, assuming that you are only changing the password
            answer = self.ask_mediator()
            if answer.upper() == 'Y':
                print("Please input Index # of the row you want to edit, starts at 0")  # IN stands for index number
                IN = int(input('If you want to exit, type "-1" if you want to exit.:  '))

                if IN >= 0 and IN < len(result_list):
                    self.edit(result_list[IN][0], result_list[IN][1], result_list[IN][2])    # Only taking it entity and username for row matching in MySQL, get password for previous password checking
                    self.caller()
            else:
                print('Okay, Going back...')
                sleep(2)
                self.caller()
                return 0
        elif answer.upper() == "L":
            answer = self.ask_mediator()
            if answer.upper() == 'Y':
                print('Understood, Good bye.')
                return 0
            else:
                print('Okay, going back to options: ')
                self.caller()


    # def cls(self):
    #     os.system('cls' if os.name=='nt' else 'clear')  # Look for alternatives




    def ask_mediator(self):   # Will pass through all decision makers here inputing if Yes or No for all options
        add_ask = True
        while add_ask:
            x = input("Do you want to continue? (Y) Yes/ (N) No? ")
            if x.upper() in 'YN':
                return x
            else:
                print("Invalid answer")
                add_ask = True



    def add(self):
        '''
        1. Add Website/app, username, password
        2. Automatically inputs into the database
        3. Gives you a recap before finalization
        4. Asks what you to do, add again or exit out of the recursion back to caller function
        '''
        print(self.id_number, self.dict_users)
        add_final = True
        while add_final:

            entity = input("Please enter website/app name: ")
            username = input("Please input your username: ")
            password = input("Pleas input your password: ")
            print("--Recap---")
            print(f"Website: {entity}")
            print(f"Username: {username}")
            print(f"password: {password}")
            print("-----")
            final_try = True
            while final_try:
                finalize = input("Do you want to finalize the add?: (Y) / (N): ")
                if finalize.upper() in "YN":
                    final_try = False
                else:
                    print("Please enter valid answer")
                    final_try = True
            if finalize.upper() == "Y":
                self.mycursor.execute(f'insert into collection (collection_id, Entity, username, password) values ("{self.id_number}","{entity}","{username}","{password}")')  # Inserts your input into MySQL
                mydb.commit() # Crucial!! This is necessary otherwise nothing will happen in your Database, always run this insert,delete etc.

                print("Successfuly Added")

                ask_again = True
                while ask_again:
                    answer_1 = input('Do you want to add another?: (Y) Yes / (N) No ')
                    if answer_1 in "YN":
                        ask_again = False
                    else:
                        print("Please input correct Yes or No")
                        asK_again = True
            if answer_1.upper() == 'Y':
                print('Okay understood.')
                add_final = True
            else:
                print('Okay, understood. Going Back to options. ')
                add_final = False

    def delete_(self,entity_delete,username_delete,password_delete):
        '''
        1. Inputs Website, Username, password from result_list by getting the index_number and partition them by indexing the tupple
        2. Presents you a verification of the info that you want to delete.
        3. Has the functionality to exit if you don't want to delete anything
        4. Verification upon deleting row.
        5. Connects to your mysql, and automatically deletes the row for you.

        ++ Take note: TODO = Adds a multi-select delete ( delete multiple selected rows):
        '''
        print("-----Deleting-----")
        print("Website/App: ", entity_delete)
        print("  Username : ", username_delete)
        print("  Password : ", password_delete)
        print("-----Deleting-----")
        delete_ask = True

        while delete_ask:
            print("Once delete process has been completed, you can't change it back.")
            x = self.ask_mediator()
            if x == 'Y':
                self.mycursor.execute(f'delete from collection where Entity = "{entity_delete}" and username = "{username_delete}" and password = "{password_delete}"') # Deletes the row with the info above
                mydb.commit()
                print('----Row Deleted----')
                print('-------------------')
                print('Going back to dashboard ')
                print('-------------------')
                print('-------------------')
                delete_ask = False
            if x == 'N':
                sleep(1)
                print('Okay, returning')
                self.cls()
                return 0



    def edit(self,entity,username,password):
        '''
        1. Allow updating password
        2. Verify before going through
        3. Goes back to caller() after
        '''
        sleep(1)
        print('----Current-----')
        print('  Website/ App    : ', entity)
        print('   Username       : ', username)
        print('Previous Password : ', password)
        sleep(2)
        edit_ask = self.ask_mediator()
        if edit_ask == 'Y':
            update_password = input('Please input password you want to change: ')
            sleep(1)
            print('Preview')
            print('  Website/ App  : ', entity)
            print('   Username     : ', username)
            print('Updated Password: ', update_password)
            sleep(2)
            final_ask = self.ask_mediator()
            if final_ask == 'Y':
                self.mycursor.execute(f'update collection set password = "{update_password}" where Entity = "{entity}" and username = "{username}"')
                mydb.commit()
            else:
                print('Going back to start, edit')
                sleep(1)
                self.edit()
        else:
            return 0



