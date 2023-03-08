from datetime import datetime
from flask import abort, make_response
from domain.models import Users, users_schema, user_schema
from domain.models import Account, accounts_schema, account_schema
from config import db
from userToken import create as create_token
# from emailthing.emailthing import create_account

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    user = Users.query.all()
    return users_schema.dump(user)


def create(usr):
    email = usr.get("email")
    password = usr.get("password")
    
# check if email is present in the database
    if email is not None:
        if Users.query.filter(Users.email == email).one_or_none():
            abort(406, f"Account with email {email} already exists") 


        else:
            user = Users(
                name= usr.get("name"),
                last_name= usr.get("last_name"),
                major= usr.get("major"),
                email= usr.get("email"),
                password= usr.get("password"),

            )
            db.session.add(user)
            db.session.commit()
            usuario = Users.query.filter(Users.email == email).one_or_none()
            account = Account(
                user_id= usuario.user_id,
                email= usr.get("email"),
                password= usr.get("password"),
                last_login= get_timestamp(),
                creation_date= get_timestamp()
            )
            db.session.add(account)
            db.session.commit()
            
            return make_response(f"{email} successfully created", 201)