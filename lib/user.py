# user.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    balance = Column(Float, default=0.0)
    transactions = relationship('Transaction', back_populates='user')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, Sequence('transaction_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(20), nullable=False)  # deposit, withdraw, transfer
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='transactions')
