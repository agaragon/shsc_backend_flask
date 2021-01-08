from flask import request
# from ...core.database import users
from ...main import app


@app.route("/registration/", methods=['POST'])
def route_registration():
    # username = request.args['username']
    # userspassword = request.args['userspassword']
    # token = request.args['token']
    # email = request.args['usersemail']
    # address = request.args['usersaddress']
    # users_data = []
    # for user in users:
    #     user_data = {"name": user.name, "email": user.email}
    #     users_data.append(user_data)
    return {}
