from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB
from sqlalchemy import relationship, ForeignKey

class BlockedList(db.Base) :
    __tablename__ = 'blocked_list'

    user_id = Column(Integer, primary_key= True)
    blocked_id = Column (Integer, primary_key= True)

    user_blockedListFK = relationship ("Users", back_populates = "BlockedList", uselist= False)# IS THIS ONE ON ONE?

    blockedUsersFK = relationship("Users") #one blocked list has many users

    #here one user is going to have many blocked?
    #??????????????????????????? double PK?????