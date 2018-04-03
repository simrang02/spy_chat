# importing required packages
from steganography.steganography import Steganography
from spy_details import *
friend_id = 0

# array for old statuses
old_statuses = ["BUSY", "AVAILABLE", "DND", "WEEKEND BINGE", "LIFE IS GOOD"]
current_status = None
# dictionary for spy friends
master_friends = []
friends = {"name": "",
           "salutation": "",
           "age": 0,
           "rating": 0.0,
           "isOnline": ""
           }

# function to select old address
def spy_status_old():
    status_id = 1
    print("Your old statuses are:")
    for i in range(len(old_statuses)):
         print(status_id , old_statuses[i])
         status_id = status_id + 1
    status_option = int(raw_input("Which status would you like to set? \n\n"))
    if status_option < len(old_statuses)+1:
        print("Your current status is: %s" % (old_statuses[status_option-1]))
        print("\n\n")
        # setting up an old status to the current status
        global current_status
        current_status = old_statuses[status_option-1]
        spy_menu()
    else:
        print("Enter a valid option spy!")

# function for new statuses
def new_status():
    global current_status
    print("Your current status is: "+str(current_status))
    spy_status_new = raw_input("What's your new status?")
    if len(spy_status_new) > 0:
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
        spy_choice = int(raw_input("What action would you like to perform (1-6)?"))
        # for status updates
        if spy_choice == 1:
            print("Your current status is: %s" %(current_status))
            spy_status_raw_input = raw_input("Do you want to select your status from old status updates(Old) or create a new one(New)?")
            if spy_status_raw_input == "Old" or spy_status_raw_input == "old":
                spy_status_old()
                old_statuses[0] = old_statuses[0]
            elif spy_status_raw_input == "New" or spy_status_raw_input == "new":
                new_status()
            else:
                print("Only old or new! Come on  spy!")
        elif spy_choice == 2:
            add_friend()
            spy_menu()
        elif spy_choice == 3:
            send_a_message()
            send_a_message()
            spy_menu()
        elif spy_choice == 4:
            read_a_message()
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

# function for adding friends
def add_friend():
    print("Enter the details of your friend:")
    friends["salutation"] = raw_input("Mr.,Ms. or Mrs.?: ")
    friends["name"] = raw_input("What's your friend's name: ")
    friends["name"] = friends["salutation"] + " " + friends["name"]
    friends["age"] = raw_input("Age: ")
    friends["rating"] = float(raw_input("Spy rating: "))
    if len(friends["name"]) > 0 and friends["age"] > str(12) and friends["rating"] >= 2.5:
        master_friends.append(friends.copy())
    else:
        print("Sorry! Enter valid details!")
    friend_count = len(master_friends)
    print("You total have: " + str(friend_count) + " friends.")

# function to select a friend
def select_a_friend():
    global friend_id
    if len(friends["name"]) <= 0:
        print("You have no friends spy!")
    else:
        print("Your friends are:")
        print("S.NO. NAME AGE RATING")
        for i in range(len(master_friends)):
             print(friend_id+1," ", master_friends[friend_id]["name"]," ", master_friends[friend_id]["age"]," ", master_friends[friend_id]["rating"])
             friend_id = friend_id + 1
        friend_option = int(raw_input("Which friend would you like to select? \n"))
        if friend_option <= friend_id and friend_option != 0:
            print("You have selected %s with index %d!" % (friends["name"], friend_option-1))
            return friend_option - 1
        else:
            print("Enter a valid option spy!")

# function to send messages
def send_a_message():
    selected_friend = select_a_friend()
    input_image = raw_input("Which image do you want to add spy?")
    import imghdr
    image_extension = imghdr.what(input_image)
    # checking image file extensions
    if image_extension == "jpeg" or image_extension == "png" or image_extension == "gif" or image_extension == "bmp":
        output_image = 'output.jpg'
        spy_text = raw_input("What is the text that you want to add to the image?")
        Steganography.encode(input_image, output_image, spy_text)
        c = ChatMessage(spy_text, True)
        master_friends[selected_friend]["chats"] = c
        print("Your message is ready to be delivered spy!")
        spy_menu()
    else:
        print("Select a friend first!")

# function to read messages
def read_a_message():
    sender_spy = select_a_friend()
    output_path = raw_input("What is the name of the image file?")
    secret_text = Steganography.decode(output_path)
    print("Your secret message is: " + secret_text + "!")
    c = ChatMessage(secret_text, False)
    master_friends[sender_spy]["chats"] = c
    print("Your secret message has been received spy!")
    # above and beyond objective 1
    split = secret_text.split()
    for i in split:
        if i == "SOS" or i == "sos" or i == "save" or i == "help" or i == "Emergency" or i == "danger":
            print("Don't panic spy!")
            print("I'm coming for your rescue!")
            break
    spy_menu()

print("THE SPY CHAT!")
# existing user or create a new user
default_user = raw_input("Would you like to continue with the default user or create a new one (Default or Create) ?")
# for existing user
if default_user == "Default" or default_user == "default":
        question = raw_input("Do you want to continue as " + existing_spy.salutation + " " + existing_spy.name + " (Y)?")
        if question == "Y" or question == "y":
            spy_menu()
        else:
            print("Then choose create user!")
            pass
# for a new user
elif default_user == "Create" or default_user == "create":
        # asking name
        Spy.name = raw_input("What's your name?")
        # checking length of the name
        if len(Spy.name) > 0:
            # asking for salutation
            Spy.salutation = raw_input("What would you like us to call you (Mr., Ms. or Mrs.) ?")
            # welcome
            print("Welcome to the spy chat " + Spy.salutation + " " + Spy.name)
            print("Alright " + Spy.salutation + " " + Spy.name + " I'd like to know a little bit more about you...")
            # checking age
            Spy.age = int(raw_input("What's your age?"))
            if Spy.age > 12 and Spy.age < 50:
                # checking rating
                Spy.rating = float(raw_input("What is your spy rating?"))
                if Spy.rating > 4.5:
                    print("Outstanding!")
                elif Spy.rating > 3.5 and Spy.rating <= 4.5:
                    print("Amazing!")
                elif Spy.rating >= 2.5 and Spy.rating <= 3.5:
                    print("You can surely improve!")
                else:
                    print("Don't Worry! We'll help you!")
                # if spy is online
                spy_is_online = True
                # welcome with details
                print("Authentication complete.")
                print("Welcome " + Spy.salutation +" " + Spy.name + " your age is " + str(Spy.age) + " and rating is " + str(Spy.rating) + "!")
                print("Proud to have you here spy!")
                spy_menu()
            # age is not eligible
            else:
                print ("You are not ready to be a spy yet!")
        # name not provided
        else:
            print("Please provide us with your name first!")
# valid entry
else:
        print("Please enter default or create.")