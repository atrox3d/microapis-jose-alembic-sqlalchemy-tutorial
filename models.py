from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine, null
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class UserModel(Base):
    
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)

users = [
    UserModel(first_name='Bob', last_name='Preston', birth=datetime(1980, 5, 2)),
    UserModel(first_name='Susan', last_name='Sage', birth=datetime(1970, 6, 12)),
]

session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users(users:list[UserModel]):
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

create_users(users)