# for an existing user
from datetime import datetime

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = "Enjoying :)"

existing_spy = Spy("Simran", "Ms.", 21, 4.6)


friend_one = Spy("Sahil", "Mr.", 21, 4.1)
friend_two = Spy("Sudhanshu", "Mr.", 21, 4.4)
friend_three = Spy("Tanya", "Ms.", 23, 4.5)

friends = [friend_one, friend_two, friend_three]

class ChatMessage:
    def __init__(self, message, isItYou):
        self.message = message
        self.time = datetime.now()
        self.isItYou = isItYou









