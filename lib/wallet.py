# wallet.py
from user import Base, engine

from sqlalchemy import create_engine
from user import User, Transaction
from sqlalchemy.orm import sessionmaker


Base.metadata.create_all(engine)

engine = create_engine('sqlite:///users.db')  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_user(username, password):
    existing_user = session.query(User).filter(User.username == username).first()
    
    if existing_user:
        print("Username already exists. Please choose another.")
    else:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        print(f"User {username} added successfully.")

def deposit(username, amount):
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.balance += amount
        transaction = Transaction(user=user, type='deposit', amount=amount)
        session.add(transaction)
        session.commit()
        print(f"Deposited {amount} into {username}'s account. New balance: {user.balance}")
    else:
        print(f"User {username} not found.")
        
def withdraw(username, amount):
    user = session.query(User).filter_by(username=username).first()
    if user:
        if user.balance >= amount:
            user.balance -= amount
            session.commit()
            print(f"Withdrew {amount} from {username}'s account. New balance: {user.balance}")
        else:
            print("Insufficient funds.")
    else:
        print(f"User {username} not found.")

def transfer(sender, recipient, amount):
    sender_user = session.query(User).filter_by(username=sender).first()
    recipient_user = session.query(User).filter_by(username=recipient).first()

    if sender_user and recipient_user:
        if sender_user.balance >= amount >= 0:
            withdraw(sender, amount)
            deposit(recipient, amount)
            print(f"Transferred {amount} from {sender} to {recipient}")
        else:
            print("Insufficient funds or invalid amount")
    else:
        print(f"User not found. Check sender: {sender} and recipient: {recipient}")

def get_balance(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"{username}'s current balance: {user.balance}")
    else:
        print(f"User {username} not found.")

