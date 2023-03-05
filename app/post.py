from datetime import datetime
from flask import abort, make_response
from domain.models import Posts, posts_schema, post_schema
from config import db

def get_timestamp():
     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    post = Posts.query.all()
    return posts_schema.dump(post)


