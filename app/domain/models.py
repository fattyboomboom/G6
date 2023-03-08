from datetime import datetime
from config import db, ma

class Account(db.Model):
    __tablename__ = 'account'

    acc_id= db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    last_login = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    
    def __repr__(self) :
              return f'Account({self.user_id}, {self.email})'
    
class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True
        sqla_session = db.session

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

class Answers(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_value = db.Column(db.Integer, nullable=False)

    def __init__(self, answer_value):
        self.answer_value=answer_value

    def __repr__(self):
            return f'Account({self.answer_value})'
    

class BlockedList(db.Model):
    __tablename__ = 'blocked_list'
    user_id = db.Column(db.Integer, primary_key=True)
    blocked_id = db.Column(db.Integer, nullable=False)

    # #relationships
    # user_blockedListFK = db.relationship ("Users", back_populates = "BlockedList", uselist= False)# IS THIS ONE ON ONE?
    # blockedUsersFK = db.relationship("Users") #one blocked list has many users

class Books(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    book_isbn = db.Column(db.String(50), nullable=False)
    book_status = db.Column(db.Integer, nullable=False)
    book_name = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    book_price = db.Column(db.Integer, nullable=False)
    book_class = db.Column(db.Integer)


    def __repr__(self) :
        return f'Book ({self.book_isbn},{self.book_price},{self.book_author},{self.book_name}, {self.book_status}, {self.book_class})'

class BookPublication(db.Model):
    __tablename__ = 'book_publication'

    publication_id = db.Column(db.Integer, primary_key=True)
    publication_text = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    publication_photo = db.Column(db.BLOB, nullable=True)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    #relationships
    # booksFK = db.relationship ("Books", back_populates ="children")
    # usersFK = db.relationship ("Users", back_populates ="parents")


    def __repr__ (self) :
        return f'Book Publications ({self.publication_text}, {self.publication_date},{ self.publication_photo},{self.book_id},{self.user_id} )'

class Buildings(db.Model):
    __tablename__ = 'buildings'
    build_id = db.Column(db.Integer, primary_key=True)
    build_name = db.Column(db.String(50), nullable=False)
    build_code = db.Column(db.String(10), nullable=False)
    build_location = db.Column(db.Text, nullable=False)
    build_photo = db.Column(db.String(50), nullable=False)

    # def __init__(self, build_code, build_location, build_photo, build_name):
    #     self.build_code= build_code
    #     self.build_location = build_location
    #     self.build_photo = build_photo
    #     self.build_name = build_name
    
    def __repr__(self):
        return f'Building ({self.build_code},{self.build_name},{self.build_location}{self.build_photo})'

class Classes(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True)
    begin_end_class = db.Column(db.String(50), nullable=False)
    class_sched = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    requirements = db.Column(db.String(50), nullable=False)
    section = db.Column(db.String(50), nullable=False)
    moderator = db.Column(db.Integer, nullable=False)
    building_id = db.Column(db.Integer, nullable=False)
    room = db.Column(db.String(50), nullable=False)



class ClassNote(db.Model):
    __tablename__ = 'class_note'
    classnote_id = db.Column(db.Integer, primary_key=True)
    classnote_text = db.Column(db.Text, nullable=False)
    classnote_photo = db.Column(db.String(50), nullable=False)
    classnote_status = db.Column(db.SmallInteger, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), nullable=False)

class FriendList(db.Model):
    __tablename__ = 'friend_list'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)

class Posts(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.Date, nullable=False)
    post_text = db.Column(db.Text, nullable=False)
    post_photo = db.Column(db.BLOB, nullable=True)
    post_status = db.Column(db.SmallInteger, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

 
    def __repr__(self):
     return f'Post'({self.post_date},{self.post_photo},{self.post_text},{self.post_status},{self.user_id})

class PostsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Posts
        load_instance = True
        sqla_session = db.session

post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)

class Profiles(db.Model):
    __tablename__ = 'profiles'
    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)

class Reports(db.Model):
    __tablename__ = 'reports'
    report_id = db.Column(db.Integer, primary_key=True)
    report_status = db.Column(db.SmallInteger, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    classnote_id = db.Column(db.Integer, db.ForeignKey('class_note.classnote_id'), nullable=False)

class StudentsClassList(db.Model):
    __tablename__ = 'students_class_list'
    class_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)

class StudySessions(db.Model):
    __tablename__ = 'study_sessions'
    ss_id = db.Column(db.Integer, primary_key=True)
    ss_place = db.Column(db.String(50), nullable=False)
    ss_date = db.Column(db.Date, nullable=False)
    ss_time = db.Column(db.String(10), nullable=False)
    build_id = db.Column(db.Integer, nullable=False)
    ss_class = db.Column(db.Integer, nullable=False)
    ss_student_id = db.Column(db.Integer, nullable=False)

class Surveys(db.Model):
    __tablename__ = 'surveys'
    survey_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)

class Users(db.Model):
    __tablename__ = 'users' 

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    major = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.BLOB, nullable=True)
    type_id = db.Column(db.Integer, nullable=False, default=3)
    #type_id = db.Column(db.Integer, db.ForeingKey('user_type.type_id'), nullable = False)
 
    def __repr__(self) :
              return f'Users({self.user_id},{self.user_name},{self.user_last_name},{self.user_major},{self.user_email},,{self.profile_picture},{self.type_id})'
    
class UsersSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
        model = Users
        load_instance = True
        sqla_session = db.session

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)    

class UserType(db.Model):
    __tablename__ = 'user_type'
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)

class UserToken(db.Model):
    __tablename__ = 'user_token'

    user_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=True)

class UserTokenSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserToken
        load_instance = True
        sqla_session = db.session

user_token_schema = UserTokenSchema()
user_tokens_schema = UserTokenSchema(many=True)

#missing all relationships

# if __name__ == '__main__':
#     db.Base.metadata.drop_all(engine)
#     db.Base.metadata.create_all(engine)