import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

# BankAccount class to manage individual accounts
class BankAccount:
    _account_number = 1000

    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.account_number = BankAccount._account_number
        self.transaction_history = [(datetime.now(), "Initial Deposit", initial_balance)]

        BankAccount._account_number += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now(), "Deposit", amount))
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), "Withdrawal", -amount))
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

# Bank class to manage multiple bank accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        else:
            return False

    def get_account(self, account_number):
        return self.accounts.get(account_number)

def main():
    bank = Bank()

    # Main loop of the program
    while True:
        # Display main menu
        root = tk.Tk()
        root.withdraw()
        menu = "Welcome to the Bank of Chicago!\n\n" \
               "1. Create Account\n" \
               "2. Deposit\n" \
               "3. Withdraw\n" \
               "4. Check Balance\n" \
               "5. Transaction History\n" \
               "6. Exit"
        choice = simpledialog.askinteger("Bank Account System", menu)

        if choice == 1:
            # Create a new account
            name = simpledialog.askstring("Bank Account System", "Enter your name:")
            initial_balance = simpledialog.askfloat("Bank Account System", "Enter your initial balance:")
            if initial_balance is not None:
                account = BankAccount(name, initial_balance)
                bank.add_account(account)
                messagebox.showinfo("Bank Account System", f"Account created! Your account number is {account.account_number}.")
            else:
                messagebox.showerror("Bank Account System", "Invalid initial balance.")

        elif choice in [2, 3, 4, 5]:
            # Get the account number
            account_number = simpledialog.askinteger("Bank Account System", "Enter your account number:")

            # Get the account from the bank
            account = bank.get_account(account_number)

            if account:
                if choice == 2:
                    # Deposit
                    amount = simpledialog.askfloat("Bank Account System", "Enter deposit amount:")
                    if account.deposit(amount):
                        messagebox.showinfo("Bank Account System", f"Deposited ${amount:.2f}. New balance: ${account.get_balance():.2f}")
                    else:
                        messagebox.showerror("Bank Account System", "Invalid deposit amount.")

                elif choice == 3:
                    # Withdraw
                    amount = simpledialog.askfloat("Bank Account System", "Enter withdrawal amount:")
                    if account.withdraw(amount):
                        messagebox.showinfo("Bank Account System", f"Withdrew ${amount:.2f}. New balance: ${account.get_balance():.2f}")
                    else:
                        messagebox.showerror("Bank Account System", "Invalid withdrawal amount or insufficient balance.")

                elif choice == 4:
                    # Check balance
                    balance = account.get_balance()
                    messagebox.showinfo("Bank Account System", f"{account.name}'s account balance: ${balance:.2f}")

                elif choice == 5:
                    # Transaction history
                    transactions = account.get_transaction_history()
                    transaction_text = ""
                    for timestamp, transaction_type, amount in transactions:
                        transaction_text += f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {transaction_type}: ${abs(amount):.2f}\n"
                    messagebox.showinfo("Bank Account System", f"Transaction history for account {account.account_number}:\n\n{transaction_text}")

            else:
                messagebox.showerror("Bank Account System", "Account not found.")

        elif choice == 6:
            # Exit
            messagebox.showinfo("Bank Account System", "Thank you for using the Bank Account System. Goodbye!")
            break

        else:
            # Invalid choice
            messagebox.showerror("Bank Account System", "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
