from database import data_

class checker():

    def __init__(self):
        pass

    def ask(self):
        ask_ = 3
        process = True
        while ask_ != 0 and process:
            username = input('Please Enter username: ')
            password = input('Please Enter Password: ')
            x = data_()  # initializes x as data_(), acts as a connector the your database
            user_check = x.check()  # Uses check and puts it into variable for username/password matching

            if user_check.get(username) == password:
                print("Access Granted")
                print("Greetings", )
                process = False
            else:
                ask_ -= 1
                print("Invalid Username / Password ")
                print(ask_, ' attempt(s) remaining')
                print("Please Try Again")


        if ask_ == 0:
            print('Locked out of account')




    def call(self):
        pass

    def store(self):
        pass

    def install(self):
        pass


if __name__ == '__main__':

    y = checker()
    y.ask()
    # end = False
    # while end:
    #     y = checker()
    #     y.ask()
