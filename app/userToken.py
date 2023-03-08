from datetime import datetime
from flask import abort, make_response
from domain.models import Users, users_schema, user_schema
from domain.models import Account, accounts_schema, account_schema
from domain.models import UserToken, user_token_schema, user_tokens_schema
from config import db
import uuid

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    user_token = UserToken.query.all()
    return user_tokens_schema.dump(user_token)

def create(tkn):

    user_id = tkn.get("user_id")
       
    if user_id :
        ut = UserToken.query.filter(UserToken.user_id == user_id).one_or_none()
        token= str(uuid.uuid4()).replace('-', '')
        if ut:
            ut.token = token
            ut.date = get_timestamp()
            db.session.merge(ut)
            db.session.commit()
           
        else:
            user_token = UserToken(
                user_id= tkn.get("user_id"),
                token= token,
                date = get_timestamp()
            )
            db.session.add(user_token)
            db.session.commit()
        response= {"token": token, "user_id": user_id}
        return response
    else:
        abort(406, f"User_id {user_id} not found")