import mysql.connector

# Replace with your own
mydb = mysql.connector.connect(
    host='-- Input your hostname--',  
    user='-- input your user--',
    password='-- input your password',
)


class data_():
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
     Gives the Statistics of the user ( Name, Age, 
    '''
    def match(self,id):

        self.id = id
        self.id_number = self.user_id.get(self.id)
        self.mycursor.execute(f'select first_name, last_name from user_info where info_id = "{self.id_number}"')
        result = self.mycursor.fetchall()
        return result


    def caller(self):

        self.mycursor.execute(f'select Entity, username, password from collection where collection_id = "{self.id_number}"')
        result = self.mycursor.fetchall()
        print('-----------Structure-----------------------')
        print("Index# |  Entity  |   Username  |   Password")
        print('-------------------------------------')

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

        if answer.upper() == "A":
            answer = self.ask_mediator()
            if answer.upper() == 'Y':
                self.add()
                self.caller()
            else:
                return 0






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




