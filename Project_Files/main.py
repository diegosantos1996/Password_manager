from database import data_

class checker():

    def __init__(self):
        self.answer = ''
        self.x = data_()  # initializes x as data_(), acts as a connector the your database

    def ask(self):
        ask_ = 3

        while ask_ != 0:
            username = input('Please Enter username: ')
            password = input('Please Enter Password: ')

            user_check = self.x.check()  # Uses check and puts it into variable for username/password matching

            if user_check.get(username) == password:
                name_of_user = self.x.match(username)

                print("Access Granted")
                print("Greetings, ", name_of_user[0][0], name_of_user[0][1] )  # Greets with firstname and lastname
                self.answer = username   
                return self.answer   # return statement to break the while loop if it enters a valid username
            else:
                ask_ -= 1
                print("Invalid Username / Password ")
                print(ask_, ' attempt(s) remaining')
                print("Please Try Again")


        if ask_ == 0:
            print('Locked out of account')



    def call(self):
        if len(self.answer) == 0:
            return self.answer       #if self.answer is still '', breaks function

        info = self.x.caller()
        # z




    def store(self):
        pass

    def install(self):
        pass


if __name__ == '__main__':

    y = checker()              #
    y.ask()
    y.call()
    # end = False
    # while end:
    #     y = checker()
    #     y.ask()
