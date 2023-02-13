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

class Answers(Base):
    __tablename__ = 'answers'
    answer_id = Column(Integer, primary_key=True)
    answer_value = Column(Integer, nullable=False)

class BlockedList(Base):
    __tablename__ = 'blocked_list'
    user_id = Column(Integer, primary_key=True)
    blocked_id = Column(Integer, nullable=False)

class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_isbn = Column(String(50), nullable=False)
    book_status = Column(Integer, nullable=False)
    book_name = Column(String(50), nullable=False)
    book_author = Column(String(50), nullable=False)
    book_price = Column(Double, nullable=False)
    book_class = Column(Integer)

class BookPublication(Base):
    __tablename__ = 'book_publication'
    publication_id = Column(Integer, primary_key=True)
    publication_text = Column(Text, nullable=False)
    publication_date = Column(Date, nullable=False)
    publication_photo = Column(String(50))
    book_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

class Buildings(Base):
    __tablename__ = 'buildings'
    build_id = Column(Integer, primary_key=True)
    build_name = Column(String(50), nullable=False)
    build_code = Column(String(10), nullable=False)
    build_location = Column(String(50), nullable=False)
    build_photo = Column(String(50), nullable=False)

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

class UserType(Base):
    __tablename__ = 'user_type'
    type_id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)

#missing all relationships