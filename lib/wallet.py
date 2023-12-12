# wallet.py
from user import User, Transaction
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///t')  # Use your desired database connection URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

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
    withdraw(sender, amount)
    deposit(recipient, amount)

def get_balance(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"{username}'s current balance: {user.balance}")
    else:
        print(f"User {username} not found.")

