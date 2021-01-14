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
        print('-------------------------------------------')

        for num, val in enumerate(result):
            print(num, val[0],"  |  ", val[1], "   |   ", val[2])
