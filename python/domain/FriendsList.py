from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB

class FriendsList(db.Base) :
    __tablename__ = 'friend_list'

    user_id = Column(Integer, primary_key= True)
    friend_id = Column (Integer, primary_key= True)

    #one user, many friends?

    #here one user is going to have many blocked?
    #??????????????????????????? double PK?????