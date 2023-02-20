from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# engine = create_engine("mysql:///?User=webtofly_db_user&Password=bw1L[{wezRx9&Database=webtofly_asegurarse&Server=db&Port=3306")
engine = create_engine("mysql+mysqldb://webtofly_db_user:bw1L[{wezRx9@bases_de_datos/webtofly_asegurarse")
Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'

    user_id = Column(Integer(), primary_key=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    last_login = Column(Date, nullable=False)
    creation_date = Column(Date, nullable=False)

    def __repr__(self) :
        return f'Account({self.user_id}, {self.email})'

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    