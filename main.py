# array for old statuses
old_statuses = ["BUSY", "AVAILABLE", "DND", "WEEKEND BINGE", "LIFE IS GOOD"]
current_status = None
#array for spy friends
friends_name = []
friends_age = []
friends_rating = []
friends_isOnline = []
friend_count = 1
# function to select old address
def spy_status_old():
    status_id = 1
    print("Your old statuses are:")
    for i in range(len(old_statuses)):
         print(status_id , old_statuses[i])
         status_id = status_id + 1
    status_option = int(input("Which status would you like to set? \n\n"))
    if status_option < len(old_statuses)+1:
        print("Your current status is: %s" % (old_statuses[status_option-1]))
        print("\n\n")
        # setting up an old status to the current status
        global current_status
        current_status = old_statuses[status_option-1]
        spy_menu()
    else:
        print("Enter a valid option spy!")

#function for new statuses
def new_status():
    global current_status
    print("Your current status is: "+str(current_status))
    spy_status_new = input("What's your new status?")
    if len(spy_status_new)>0:
        old_statuses.append(spy_status_new)
        print("Your current status is: %s" %(spy_status_new))
        print("\n\n")
        # setting up the new status to the current status
        current_status = spy_status_new
        spy_menu()
    else:
        print("Please enter a status spy!")

# function for menu
def spy_menu():
        global current_status
        print("\t\tMENU")
        print("You have the choice of:")
        print("1) Add a status update")
        print("2) Add a friend")
        print("3) Send a secret message")
        print("4) Read a secret message")
        print("5) Read chats from a user")
        print("6) Close application")
        spy_choice = int(input("What action would you like to perform (1-6)?"))
        # for status updates
        if spy_choice == 1:
            print("Your current status is: %s" %(current_status))
            spy_status_input = input("Do you want to select your status from old status updates(Old) or create a new one(New)?")
            if spy_status_input == "Old" or spy_status_input == "old":
                spy_status_old()
                old_statuses[0] = old_statuses[0]
            elif spy_status_input == "New" or spy_status_input == "new":
               new_status()
            else:
                print("Only old or new! Come on  spy!")
        elif spy_choice == 2:
            add_friend()
            spy_menu()
        elif spy_choice == 3:
            print("We'll send a secret message later!")
            spy_menu()
        elif spy_choice == 4:
            print("We'll read a secret message later!")
            spy_menu()
        elif spy_choice == 5:
            print("We'll read chats later!")
            spy_menu()
        elif spy_choice == 6:
            # for quitting the app
            print("Quitting")
            pass
        else:
            print("Invalid entry!")
            spy_menu()

#function for adding friends
def add_friend():
    global friend_count
    print("Enter the details of your friend:")
    friend_salutation = input("Mr.,Ms. or Mrs.?: ")
    friend_name = input("What's your friend's name: ")
    friend_name = friend_salutation + " " + friend_name
    friend_age = input("Age: ")
    friend_rating = float(input("Spy rating: "))
    if len(friend_name) > 0 and friend_age > str(12) and friend_rating >= 2.5:
        friends_name.append(friend_name)
        friends_age.append(friend_age)
        friends_rating.append(friend_rating)
        friends_isOnline.append(True)
    else:
        print("Sorry! Enter valid details!")
    friend_count = len(friends_name)
    print("You total have: "+ str(friend_count) +" friends.")

print("THE SPY CHAT!")
# existing user or create a new user
default_user = input("Would you like to continue with the default user or create a new one (Default or Create) ?")
# for existing user
if default_user == "Default" or default_user == "default":
        import spy_details
        current_status = "ENJOYING :)"
        spy_menu()
# for a new user
elif default_user == "Create" or default_user == "create":
        # asking name
        spy_name = input("What's your name?")
        # checking length of the name
        if len(spy_name) > 0:
            # asking for salutation
            spy_salutation = input("What would you like us to call you (Mr., Ms. or Mrs.) ?")
            # welcome
            print("Welcome to the spy chat " + spy_salutation + " " + spy_name)
            print("Alright " + spy_salutation + " " + spy_name + " I'd like to know a little bit more about you...")
            #checking age
            spy_age = int(input("What's your age?"))
            if spy_age > 12 and spy_age < 50:
                # checking rating
                spy_rating = float(input("What is your spy rating?"))
                if spy_rating > 4.5:
                    print("Outstanding!")
                elif spy_rating > 3.5 and spy_rating <= 4.5:
                    print("Amazing!")
                elif spy_rating >= 2.5 and spy_rating <= 3.5:
                    print("You can surely improve!")
                else:
                    print("Don't Worry! We'll help you!")
                # if spy is online
                spy_is_online = True
                # welcome with details
                print("Authentication complete.")
                print("Welcome " +spy_salutation+" " +spy_name + " your age is " + str(spy_age) + " and rating is " + str(spy_rating) + "!")
                print("Proud to have you onboard!")
                new_status()
            # age is not eligible
            else:
                print ("You are not ready to be a spy yet!")
        # name not provided
        else:
            print("Please provide us with your name first!")
#valid entry
else:
        print("Please enter default or create.")