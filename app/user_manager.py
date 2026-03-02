class UserManager:
    def __init__(self):
        self.users = []
    def add_user(self, username):
        if not username:
            raise ValueError("Username cannot be empty")   
        if username in self.users:
            raise ValueError("Username already exists")
        self.users.append(username)
    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("Username does not exist")
        self.users.remove(username)
    def count_users(self):
        return len(self.users)
def count_users(self):
        return len(self.users)