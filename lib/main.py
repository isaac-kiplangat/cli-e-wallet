#!usr/bin/env

from wallet import create_user, deposit, withdraw, transfer, get_balance


def main():
    #initilize input descriptions
    while True:
        print("\nE-Wallet CLI:")
        print("0. Create Account")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Exit")

#manage inputs
        choice = input("Enter your choice (0-5): ")
        if choice == "0":
          username = input("Enter a Username: ")
          password = input ("Enter a new Password: ")
          
          create_user(username,password)

        elif choice == "1":
            username = input("Enter username: ")
            amount = float(input("Enter amount to deposit: "))
            password = input("Enter password: ")
            deposit(username,password, amount)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(username, password, amount)
        elif choice == "3":
            sender = input("Enter sender username: ")
            recipient = input("Enter recipient username: ")
            amount = float(input("Enter amount to transfer: "))
            sender_password = input("Enter password: ")
            transfer(sender, recipient,sender_password, amount)
        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            get_balance(username, password)
        elif choice == "5":
            print("Exiting E-Wallet CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()