from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB
from sqlalchemy import relationship, ForeignKey


class Users (db.Base) :
    __tablename__ = 'users'

    user_id = Column (Integer, primary_key= True)
    publicationsFK = relationship("BookPublications")
    #fml, one acc has one user
    
