#!usr/bin/env

from wallet import create_user, deposit, withdraw, transfer, get_balance


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