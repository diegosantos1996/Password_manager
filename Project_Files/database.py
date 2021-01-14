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


    '''
       Check's main purpose : Username / Password Matching  
    '''
    def check(self):

        self.mycursor.execute("USE passwords")    # Uses table
        self.mycursor.execute("select username,password from users ") # selecting username & password info from users
        result = self.mycursor.fetchall()
        self.dict_users = {x[0]:x[1] for x in result}  # initializes Username and password into dictionary
        return self.dict_users

    def match(self):

        self.mycursor.execut("select u.users_id, ui.info_id, ")
