from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from user import create_user
from wallet import deposit
from wallet import withdraw
from wallet import transfer
from wallet import get_balance

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


def main():
    while True:
        print("\nE-Wallet CLI:")
        print("0. Create Account")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Exit")

        choice = input("Enter your choice (0-5): ")
        if choice == "0":
          username = input("Enter a Username: ")
          password = input ("Enter a new Password: ")
          
          create_user(username,password)

        elif choice == "1":
            username = input("Enter username: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(username, amount)
        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter amount to withdraw: "))
            password = input("Enter password: ")
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