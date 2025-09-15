class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  # Initial balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ {amount} deposited successfully!")
        else:
            print("❌ Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ {amount} withdrawn successfully!")
        else:
            print("❌ Insufficient balance or invalid amount!")

    def check_balance(self):
        print(f"💰 Account Balance: {self.balance}")

    def account_info(self):
        print("\n📄 Account Details")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}\n")


# ------------ Main Program ------------
def main():
    print("🏦 Welcome to Simple Banking System")
    account_number = input("Enter Account Number: ")
    account_holder = input("Enter Account Holder Name: ")

    account = BankAccount(account_number, account_holder)

    while True:
        print("\n=== MENU ===")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Info")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.account_info()
        elif choice == "5":
            print("👋 Thank you for banking with us!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
