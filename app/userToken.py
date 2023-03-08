from datetime import datetime
from flask import abort, make_response
from domain.models import Users, users_schema, user_schema
from domain.models import Account, accounts_schema, account_schema
from domain.models import UserToken, user_token_schema, user_tokens_schema
from config import db

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    user_token = UserToken.query.all()
    return user_tokens_schema.dump(user_token)

# def create(tkn):
#     user_id = tkn.get("user_id")
#     token = tkn.get("token")
#     date = tkn.get("creation_date")

#     if user_id is not None:
#         if UserToken.query.filter(UserToken.user_id == user_id).one_or_none():
#             abort(406, f"Token with user_id {user_id} already exists") 

#         else:
#             user_token = UserToken(
#                 user_id= tkn.get("user_id"),
#                 token= tkn.get("token"),
#                 expiration_date= tkn.get("expiration_date"),
#                 creation_date= tkn.get("creation_date")
#             )
#             db.session.add(user_token)
#             db.session.commit()
#             return make_response(f"{user_id} successfully created", 201)
