from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB, relationship, ForeignKey

class Classes (db.Base):
    __tablename__ = 'classes'

    class_id = Column(Integer, primary_key=True)
    begin_end_class = Column (String (50))#yeah ik it could be 2 separate ones in date format
    class_sched = Column (String (50), nullable= False) #this is like, Tuesdays and Thrusdays 10 to 11
    professor = Column ( String (50), nullable= False)
    requirements = Column (String (50), nullable=False)
    section = Column (String (50), nullable= False)
    moderator = Column (Integer) #FK TO USERS, one class can have many moderators
    #im fucking missing a thing in  the table where it shows which users are in this class, it would be MANY USERS TO ONE CLASS
    building_id = Column (Integer) #fk to buildings, one class has one building
    room = Column (String(50), nullable= False)

    def __init__(self, begin_end_class, class_sched, professor, requirements, section, moderator, building_id, room):
        self.begin_end_class=begin_end_class
        self.class_sched = class_sched
        self.professor = professor
        self.requirements = requirements
        self. section = section
        self.room = room

#missing RELATIONSHIPS, NOT DONE

