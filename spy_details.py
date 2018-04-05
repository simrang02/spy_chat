from datetime import datetime

# class for storing details
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

# chat class
class ChatMessage:
    def __init__(self, name, message, isItYou):
        self.name = name
        self.message = message
        self.time = datetime.now()
        self.isItYou = isItYou