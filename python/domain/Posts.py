from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB, ForeignKey, relationship

class Posts (db.Base):
    __tablename__ = 'posts'

    post_id = Column (Integer, primary_key= True)
    post_date = Column (DateTime) # can i do  datetime in mysql?
    post_text = Column (String (255), nullable= False)# how many chaaracters in text again?
    post_photo = Column (String(250), nullable= True) # GUESS WHAT, ITS A BLOB
    post_status = Column (bool)
    user_id = Column (Integer) # FK TO USERS TABLE, ONE USER MANY POSTS

    def __init__(self, post_date, post_text, post_photo, post_status, user_id):
        self.post_date= post_date
        self.post_photo = post_photo
        self.post_status = post_status
        self.post_text = post_text
        self.user_id = user_id
    
    def __repr__(self):
        return f'Post'({self.post_date},{self.post_photo},{self.post_text},{self.post_status},{self.user_id})
    
    #missing FK TO USERS, MANY POSTS ONE USER
    #DEF NOT DONE
    