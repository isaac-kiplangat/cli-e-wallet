from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    balance = Column(Float, default=0.0)

engine = create_engine('sqlite:///:memory:')  # Use your desired database connection URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()

def deposit(username, amount):
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.balance += amount
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

def main():
    while True:
        print("\nE-Wallet CLI:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter username: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(username, amount)
        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(username, amount)
        elif choice == "3":
            sender = input("Enter sender username: ")
            recipient = input("Enter recipient username: ")
            amount = float(input("Enter amount to transfer: "))
            transfer(sender, recipient, amount)
        elif choice == "4":
            username = input("Enter username: ")
            get_balance(username)
        elif choice == "5":
            print("Exiting E-Wallet CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
