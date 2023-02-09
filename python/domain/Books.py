from engine import db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, BLOB, relationship, Double, ForeignKey


class Books (db.Base):
    __tablename__= 'books'

    book_id= Column(Integer, primary_key= True)
    publications_booksFK = relationship("BookPublications") #many publications to one book
    book_isbn = Column (String (50), nullable= True)
    book_status = Column (Integer) #dropdown of statuses. like 1 = terrible, 3= almost new
    book_name= Column (String (50))
    book_author = Column (String(50))
    book_price = Column (Double)
    book_class = Column (int) #list of the classes dropdown
    #FML ANOTHER FK FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    #do we do the dropdown options here?

    def __init__(self, book_isbn, book_status, book_name, book_author, book_price, book_class):
        self.book_isbn = book_isbn
        self.book_status = book_status
        self.book_name = book_name
        self.book_author = book_author
        self.book_price = book_price
        self.book_class = book_class
    
    def __repr__(self) :
        return f'Book ({self.book_isbn},{self.book_price},{self.book_author},{self.book_name}, {self.book_status}, {self.book_class})'
    
    #not done, missing class FK
