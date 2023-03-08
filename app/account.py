from datetime import datetime
from flask import abort, make_response
from domain.models import Account, accounts_schema, account_schema
from domain.models import Users, users_schema, user_schema
from config import db
from userToken import create as create_token
import json

#this API is
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    cuentas = Account.query.all()
    return accounts_schema.dump(cuentas)


def validate (acc):
    email = acc.get("email")
    password = acc.get("password")

    account = Account.query.filter(Account.email == email).one_or_none()

    if account is not None:
        if password == account_schema.dump(account).get('password'):
            usuario = Users.query.filter(Users.email == email).one_or_none()
            tk={"user_id": usuario.user_id}
            data=create_token(tk)
            data["type_id"]= usuario.type_id
            print (data)
            type_id= usuario.type_id
            if type_id == 3:
                return make_response(data, 200)
            if type_id == 2:
                return make_response(data, 201) 
            if type_id == 1:
                return make_response(data, 202)
   
    abort(404, "Email or password incorrect")
     