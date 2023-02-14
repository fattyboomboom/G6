from sqlalchemy import Column, Integer, String, Date, Double, Text, relationship, ForeignKey, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    user_id = Column(Integer, primary_key=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    last_login = Column(Date, nullable=False)
    creation_date = Column(Date, nullable=False)

    def __init__(self, password, email, last_login, creation_date) :
            self.password = password
            self.email = email
            self.last_login = last_login
            self. creation_date = creation_date

    def __repr__(self) :
              return f'Account({self.email}, {self.password}, {self.last_login}, {self.creation_date})'

class Answers(Base):
    __tablename__ = 'answers'
    answer_id = Column(Integer, primary_key=True)
    answer_value = Column(Integer, nullable=False)

class BlockedList(Base):
    __tablename__ = 'blocked_list'
    user_id = Column(Integer, primary_key=True)
    blocked_id = Column(Integer, nullable=False)

    #relationships
    user_blockedListFK = relationship ("Users", back_populates = "BlockedList", uselist= False)# IS THIS ONE ON ONE?
    blockedUsersFK = relationship("Users") #one blocked list has many users

class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_isbn = Column(String(50), nullable=False)
    book_status = Column(Integer, nullable=False)
    book_name = Column(String(50), nullable=False)
    book_author = Column(String(50), nullable=False)
    book_price = Column(Double, nullable=False)
    book_class = Column(Integer)

    def __init__(self, book_isbn, book_status, book_name, book_author, book_price, book_class):
        self.book_isbn = book_isbn
        self.book_status = book_status
        self.book_name = book_name
        self.book_author = book_author
        self.book_price = book_price
        self.book_class = book_class
    
    def __repr__(self) :
        return f'Book ({self.book_isbn},{self.book_price},{self.book_author},{self.book_name}, {self.book_status}, {self.book_class})'

class BookPublication(Base):
    __tablename__ = 'book_publication'
    publication_id = Column(Integer, primary_key=True)
    publication_text = Column(Text, nullable=False)
    publication_date = Column(Date, nullable=False)
    publication_photo = Column(String(50))
    book_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    #relationships
    booksFK = relationship ("Books", back_populates ="publications_booksFK")
    usersFK = relationship ("Users", back_populates ="publications_usersFK")

    def __init__ (self, publication_text,publication_date, publication_photo, book_id, user_id):
        self.publication_text = publication_text
        self.publication_date = publication_date
        self.publication_photo = publication_photo
        self.book_id = book_id
        self.user_id = user_id

    def __repr__ (self) :
        return f'Book Publications ({self.publication_text}, {self.publication_date},{ self.publication_photo},{self.book_id},{self.user_id} )'

class Buildings(Base):
    __tablename__ = 'buildings'
    build_id = Column(Integer, primary_key=True)
    build_name = Column(String(50), nullable=False)
    build_code = Column(String(10), nullable=False)
    build_location = Column(String(50), nullable=False)
    build_photo = Column(String(50), nullable=False)

    def __init__(self, build_code, build_location, build_photo, build_name):
        self.build_code= build_code
        self.build_location = build_location
        self.build_photo = build_photo
        self.build_name = build_name
    
    def __repr__(self):
        return f'Building ({self.build_code},{self.build_name},{self.build_location}{self.build_photo})'

class Classes(Base):
    __tablename__ = 'classes'
    class_id = Column(Integer, primary_key=True)
    begin_end_class = Column(String(50), nullable=False)
    class_sched = Column(String(50), nullable=False)
    professor = Column(String(50), nullable=False)
    requirements = Column(String(50), nullable=False)
    section = Column(String(50), nullable=False)
    moderator = Column(Integer, nullable=False)
    building_id = Column(Integer, nullable=False)
    room = Column(String(50), nullable=False)

    def __init__(self, begin_end_class, class_sched, professor, requirements, section, moderator, building_id, room):
        self.begin_end_class=begin_end_class
        self.class_sched = class_sched
        self.professor = professor
        self.requirements = requirements
        self. section = section
        self.room = room

class ClassNote(Base):
    __tablename__ = 'class_note'
    classnote_id = Column(Integer, primary_key=True)
    classnote_text = Column(Text, nullable=False)
    classnote_photo = Column(String(50), nullable=False)
    classnote_status = Column(SmallInteger, nullable=False)
    class_id = Column(Integer, ForeignKey('classes.class_id'), nullable=False)

class FriendList(Base):
    __tablename__ = 'friend_list'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    friend_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)

class Posts(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    post_date = Column(Date, nullable=False)
    post_text = Column(Text, nullable=False)
    post_photo = Column(String(50), nullable=True)
    post_status = Column(SmallInteger, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    def __init__(self, post_date, post_text, post_photo, post_status, user_id):
        self.post_date= post_date
        self.post_photo = post_photo
        self.post_status = post_status
        self.post_text = post_text
        self.user_id = user_id
    
    def __repr__(self):
        return f'Post'({self.post_date},{self.post_photo},{self.post_text},{self.post_status},{self.user_id})

class Profiles(Base):
    __tablename__ = 'profiles'
    profile_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)

class Reports(Base):
    __tablename__ = 'reports'
    report_id = Column(Integer, primary_key=True)
    report_status = Column(SmallInteger, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id'), nullable=False)
    classnote_id = Column(Integer, ForeignKey('class_note.classnote_id'), nullable=False)

class StudentsClassList(Base):
    __tablename__ = 'students_class_list'
    class_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)

class StudySessions(Base):
    __tablename__ = 'study_sessions'
    ss_id = Column(Integer, primary_key=True)
    ss_place = Column(String(50), nullable=False)
    ss_date = Column(Date, nullable=False)
    ss_time = Column(String(10), nullable=False)
    build_id = Column(Integer, nullable=False)
    ss_class = Column(Integer, nullable=False)
    ss_student_id = Column(Integer, nullable=False)

class Surveys(Base):
    __tablename__ = 'surveys'
    survey_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=False)

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_email = Column(String(50), nullable=False)
    user_phone = Column(Integer, nullable=False)
    user_dob = Column(Date)
    preferred_pronouns = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    profile_picture = Column(String(100), nullable=False)
    type_id = Column(Integer, nullable=False)

    #relationships
    

class UserType(Base):
    __tablename__ = 'user_type'
    type_id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)

#missing all relationships