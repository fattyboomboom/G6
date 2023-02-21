
from datetime import datetime
from config import db, ma

class Account(db.Model):
    __tablename__ = 'account'

    user_id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    last_login = db.Column(db.Date, nullable=False)
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