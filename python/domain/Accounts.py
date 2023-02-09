from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB
from sqlalchemy import *

class Accounts (db.Base):
        __tablename__= 'account'

        user_id= Column (Integer, primary_key= True)
        password = Column (String (50), nullable= False)
        email = Column (String (50), nullable=False)
        last_login = Column (DateTime)
        creation_date = Column (Date)

        def __init__(self, password, email, last_login, creation_date) :
            self.password = password
            self.email = email
            self.last_login = last_login
            self. creation_date = creation_date

        def __repr__(self) :
              return f'Account({self.email}, {self.password}, {self.last_login}, {self.creation_date})'
        