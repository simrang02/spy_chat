print("THE SPY CHAT!")
# existing user or create a new user
default_user = input("Would you like to continue with the default user or create a new one (Default or Create) ?")
# for existing user
if default_user == "Default" or default_user == "default":
        import spy_details
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
            # age is not eligible
            else:
                print ("You are not ready to be a spy yet!")
        # name not provided
        else:
            print("Please provide us with your name first!")
#valid entry
else:
        print("Please enter default or create.")
