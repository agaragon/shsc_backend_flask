from flask import jsonify

# from ...core.database import users
from ...models.user import User
from ...main import app


@app.route("/users/")
def route_users():
    users = User.query.all()
    users_data=[]
    for user in users:
        user_data = {"name": user.username, "email": user.users_email}
        users_data.append(user_data)
    return jsonify(users_data)
