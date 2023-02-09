from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB, ForeignKey, relationship

class Profiles(db.Base):
    __tablename__= 'profiles'

    profile_id = Column (Integer, primary_key= True)
    user_id = Column (Integer) #FK TO USERS, one user one profile
    post_id = Column (Integer) #FK TO POSTS, one profile many posts

    #def not done, missing FKS
    
