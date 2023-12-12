from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    balance = Column(Float, default=0.0)
    # transactions = relationship('Transaction', back_populates='user')

engine = create_engine('sqlite:///users.db') 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print(f"User {username} added successfully.")

