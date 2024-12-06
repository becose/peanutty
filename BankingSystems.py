class BankAccount:
    def __init__(self):
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount
        print("Amount Deposited Successfully")
        print("New Bank Balance: ", self.amount)

    def withdraw_funds(self, amount):
        """
        Withdraw funds from the account if sufficient balance exists.

        Parameters:
        amount (float): The amount to withdraw.
        Returns:
        str: A message indicating the result of the withdrawal.
        """
        if amount <= 0:
            return "Error: Withdrawal amount must be greater than zero."
        elif amount > self.amount:
            return "Error: Insufficient funds."
        else:
            self.amount -= amount
            return f"Success: Withdrawn ${amount:.2f}. New balance: ${self.amount:.2f}"

    def show_balance(self):
        print("Your Balance Is: ", self.amount)

    def transfer(self, destination_account, amount):
        """
        Transfer funds from one account to another.

        Parameters:
        destination_account (BankAccount): The account to transfer to.
        amount (float): The amount to transfer.
        Returns:
        str: A message indicating the result of the transfer.
        """
        if amount <= 0:
            return "Your transfer has to be more than 0"
        elif amount > self.amount:
            return "Sorry you have insufficient funds."
        else:
            self.amount -= amount
            destination_account.amount += amount
            return f" Yay: Your ${amount:.2f} has been transferred to its destination."


def show_account_balance(checking_balance, savings_balance):
    while True:
        try:
            account = input(
                "Type 'checking' for checking account balance or 'savings' for savings account balance? ")

            if account == "checking":
                print(
                    f"Your Checking Account Balance is ${checking_balance.amount:.2f}")
                return

            elif account == "savings":
                print(
                    f"Your Savings Account Balance is ${savings_balance.amount:.2f}")
                return

        except ValueError:
            print("Incorrect. Please try again, type 'checking' for Checking Account Balance or 'savings' for Savings Account Balance. ")


def main():
    checking_balance = BankAccount()
    savings_balance = BankAccount()

    while True:
        print("1-Deposit\n2-Withdraw\n3-Check Balance\n4-Transfer\n5-Exit")
        choice = int(input("Enter Choice: "))
        account_choice = int(input("Choose Account: 1-Checkings 2-Savings\n"))

        if account_choice == 1:
            if choice == 1:
                amount = float(input("Enter Deposit Amount: "))
                checking_balance.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter Withdraw Amount: "))
                print(checking_balance.withdraw_funds(amount))
            elif choice == 3:
                checking_balance.show_balance()
            elif choice == 4:
                amount = float(input("Enter Transfer Amount: "))
                destination_account = savings_balance
                print(checking_balance.transfer(destination_account, amount))
            elif choice == 5:
                exit()
            else:
                print("You Have Chosen an Invalid Choice")

        elif account_choice == 2:
            if choice == 1:
                amount = float(input("Enter Deposit Amount: "))
                savings_balance.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter Withdraw Amount: "))
                print(savings_balance.withdraw_funds(amount))
            elif choice == 3:
                savings_balance.show_balance()
            elif choice == 4:
                amount = float(input("Enter Transfer Amount: "))
                destination_account = checking_balance
                print(savings_balance.transfer(destination_account, amount))
            elif choice == 5:
                exit()
            else:
                print("You Have Chosen an Invalid Choice")
        else:
            print("You Have Chosen an Invalid Choice")


if __name__ == "__main__":
    main()