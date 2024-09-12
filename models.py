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

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        fields = ', '.join([f'{col}={getattr(self, col)}' for col in self.__table__.columns.keys()])
        return f'UserModel({fields})'

users = [
    UserModel(first_name='Bob', last_name='Preston', birth=datetime(1980, 5, 2)),
    UserModel(first_name='Susan', last_name='Sage', birth=datetime(1970, 6, 12)),
]

session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users(users:list[UserModel], delete=True):
    with session_maker() as session:
        if delete:
            session.query(UserModel).delete()
        for user in users:
            session.add(user)
        session.commit()

def print_users():
    with session_maker() as session:
        users = session.query(UserModel).all()
        for user in users:
            print(user.full_name)

create_users(users)
print_users()
