class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print("new user created..")
user_1 = User("555", "Monkeyface")
user_2 = User("777", "Pancake")
print(user_2.username)


