from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB

#i would like to know why i made so many FCKNG FKs

class Buildings(db.Base):
    __tablename__ = 'buildings'

    build_id = Column (Integer, primary_key= True)
    build_code = Column (String (10), nullable=False)
    build_name = Column (String(50), nullable= False)
    build_location = Column (String (50), nullable=False) # this is the google maps adress, is it a blob? wtf is a blob?
    build_photo = Column (String (50), nullable= False)# same as line 12

    #relations
    #one building to many : classes and study_sessions
    #fuck that

    def __init__(self, build_code, build_location, build_photo, build_name):
        self.build_code= build_code
        self.build_location = build_location
        self.build_photo = build_photo
        self.build_name = build_name
    
    def __repr__(self):
        return f'Building ({self.build_code},{self.build_name},{self.build_location}{self.build_photo})'

    #missing relations NOT DONE
