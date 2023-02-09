from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB
from sqlalchemy import relationship, ForeignKey, ForeignKeyConstraint

class BookPublications(db.Base) :
    __tablename__ = 'book_publication'

    publication_id = Column (Integer, primary_key=True)
    publication_text = Column (String (249), nullable= False)
    publication_date = Column (DateTime)
    publication_photo = Column (BLOB, nullable= True)# idk if i made it nullable, in the db its a varchar but ik it has to be BLOB VINH, I JUST DON'T KNOW WHAT A BLOB IS OK?
    book_id = Column (Integer, ForeignKey("book.book_id") ) #many publications to one book
    booksFK = relationship ("Books", back_populates ="publications_booksFK")
    user_id = Column (Integer, ForeignKey("users.user_id")) #many publications to one user
    usersFK = relationship ("Users", back_populates ="publications_usersFK")

    def __init__ (self, publication_text,publication_date, publication_photo, book_id, user_id):
        self.publication_text = publication_text
        self.publication_date = publication_date
        self.publication_photo = publication_photo
        self.book_id = book_id
        self.user_id = user_id

    def __repr__ (self) :
        return f'Book Publications ({self.publication_text}, {self.publication_date},{ self.publication_photo},{self.book_id},{self.user_id} )'

#done?

