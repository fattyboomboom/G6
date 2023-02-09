from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB, relationship, ForeignKey

class ClassNotes (db.Base):
    __tablename__ = 'class_note'

    classnote_id = Column (Integer, primary_key=True)
    classnote_text = Column (String (249))
    classnote_photo = Column (String (50))# IK IT SHOULD BE BLOB
    classnote_status = Column (bool)
    class_id = Column (Integer)# FK TO CLASSES, ONE CLASS HAS MANY CLASS NOTES
    #MISSING USER ID HERE

    #DEF NOT DONE
    