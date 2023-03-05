from datetime import datetime
from flask import abort, make_response
from domain.models import Users, users_schema, user_schema
from config import db

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    user = Users.query.all()
    return users_schema.dump(user)


def create(usr):
    email = usr.get("email")
    password = usr.get("password")
    
    user = Users.query.filter(Users.user_email == email).one_or_none()
# check if email is present in the database
    if email is not None:
        if email is not user.email: 
            user = Users(
                user_name= usr.get("name"),
                user_last_name= usr.get("last_name"),
                #user_major= usr.get("major"),
                user_email= usr.get("email"),
                user_password= usr.get("password"),
                #user type sets automatically to 3? how?
                #user_type= usr.get(3), #?????

            )
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user), 201
        else:
         abort(406, f"Account with email {email} already exists")

