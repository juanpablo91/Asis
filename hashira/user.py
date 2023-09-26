class User:
    def __init__(self,username,email,preserences):
        self.username = username
        self.email = email 
        self.preferences = preferences
    def save(self):
        #save in local or data base. to define

    @classmethod
    def load(cls,username):
        #load the user in data base
        pass
    