class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to procedd?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exist           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter you email here ->")
        pwd = input("setup your password here ->")
        self.username = email
        self.password = pwd
        print("You have signed up successfully!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
           print("Please signup first by pressing 1 in the main menu")
        else:
            username = input("enter your email/uername here ")
            pwd = input("enter your password here ")
            if self.username==username and self.password==pwd:
                print("you have signed in successfully !!")
                self.loggedin = True 
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()  

    def my_post(self):
        if self.loggedin==True:
            txt = input("enter you message ")
            print(f"following content has been posted {txt}")
        else:
            print("you need to signin first to post somethng..")
        print("\n")
        self.menu()                      

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("enter you message here  ")
            frnd = input("whom to send the msd?  ")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to signin first to post somethng..")
        print("\n")
        self.menu()     

user1 = chatbook()