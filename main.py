# array for old statuses
old_statuses = ["BUSY", "AVAILABLE", "DND", "WEEKEND BINGE", "LIFE IS GOOD"]
current_status = "ENJOYING :)"
# function to select old address
def spy_status_old():
    print("Your old statuses are:")
    print(old_statuses[0])
    print(old_statuses[1])
    print(old_statuses[2])
    print(old_statuses[3])
    print(old_statuses[4])
    status_option = input("Which status would you like to set (1-5)? \n\n")
    if status_option == "1":
        old_statuses[0] = old_statuses[0]
    elif status_option == "2":
        old_statuses[0] = old_statuses[1]
    elif status_option == "3":
        old_statuses[0] = old_statuses[2]
    elif status_option == "4":
        old_statuses[0] = old_statuses[3]
    elif status_option == "5":
        old_statuses[0] = old_statuses[4]
    else:
        print("Enter a valid option spy!")
    print("Your current status is: %s" %(old_statuses[0]))
    print("\n\n")
    # setting up an old status to the current status
    global current_status
    current_status = old_statuses[0]
    spy_menu()

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
                spy_status_new = input("What's your new status?")
                new_status = old_statuses.append(spy_status_new)
                print("Your current status is: %s" %(spy_status_new))
                print("\n\n")
                # seeting up the new status to the current status
                current_status = spy_status_new
                spy_menu()
            else:
                print("Only old or new! Come on  spy!")
        elif spy_choice == 2:
            print("We'll add a friend later!")
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

print("THE SPY CHAT!")
# existing user or create a new user
default_user = input("Would you like to continue with the default user or create a new one (Default or Create) ?")
# for existing user
if default_user == "Default" or default_user == "default":
        import spy_details
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
                spy_menu()
            # age is not eligible
            else:
                print ("You are not ready to be a spy yet!")
        # name not provided
        else:
            print("Please provide us with your name first!")
#valid entry
else:
        print("Please enter default or create.")