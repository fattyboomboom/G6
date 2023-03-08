from datetime import datetime
from flask import abort, make_response
from domain.models import Posts, posts_schema, post_schema
from config import db

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    post = Posts.query.all()
    return posts_schema.dump(post)

# def create():
#     post = Posts(
#           post_date= get_timestamp(),
#           post_text= pst.get("post_text"),
#           post_photo= pst.get("post_photo"),


#     )
#     db.session.add(post)
#     db.session.commit()
#     return post_schema.dump(post),make_response(f"Post successfully created", 201)
