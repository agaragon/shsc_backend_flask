from app import db

class User(db.Model):
    username = db.Column(db.String,primary_key=True)
    users_email = db.Column(db.String)
    users_password = db.Column(db.String)
    users_address = db.Column(db.String)
    users_token = db.Column(db.String)

    def __init__(self, username, users_password, users_token, users_address, users_email):
        self.username = username
        self.users_password = users_password
        self.users_token = users_token
        self.users_address = users_address
        self.users_email = users_email
