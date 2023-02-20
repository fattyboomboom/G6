from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("mysql+mysqldb://webtofly_db_user:bw1L[{wezRx9@bases_de_datos/webtofly_asegurarse")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()