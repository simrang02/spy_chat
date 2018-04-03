from datetime import datetime

#general class for storing details
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.master_friends = []
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = "Enjoying :)"

# for an existing user
existing_spy = Spy("Simran", "Ms.", 21, 4.6)

#existing friends
friend_one = Spy("Sahil", "Mr.", 21, 4.1)
friend_two = Spy("Sudhanshu", "Mr.", 21, 4.4)
friend_three = Spy("Tanya", "Ms.", 23, 4.5)

master_friends = [friend_one, friend_two, friend_three]

#chat class
class ChatMessage:
    def __init__(self, message, isItYou):
        self.message = message
        self.time = datetime.now()
        self.isItYou = isItYou









