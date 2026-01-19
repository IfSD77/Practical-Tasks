# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    name = input("Enter the account holder's name: ").strip()
    if name in account_holders:
        print("An account with this name already exists.")
        return
    account_holders.append(name)
    balances.append(0)
    transaction_histories.append([])
    loans.append(0)
    print(f"Account successfully created for {name}.")


def deposit():
    """Deposit money into an account."""
    name = input("Enter the account holder's name: ").strip()
    if name in account_holders:
        deposit_amount = float(input("Enter the amount to deposit: "))
        index = account_holders.index(name)
        balances[index] += deposit_amount
        transaction_histories[index].append(f"Deposited: {deposit_amount:.2f}lv.")
        print(f"The updated balance for {name} is: {balances[index]:.2f}lv.")
    else:
        print("An account with this name does not exist.")


def withdraw():
    """Withdraw money from an account."""
    name = input("Enter the account holder's name: ").strip()
    if name in account_holders:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        index = account_holders.index(name)
        if balances[index] >= withdraw_amount:
            balances[index] -= withdraw_amount
            transaction_histories[index].append(f"Withdrawn: {withdraw_amount:.2f}lv.")
            print(f"The updated balance for {name} is: {balances[index]:.2f}lv.")
        else:
            print("Insufficient balance.")
    else:
        print("An account with this name does not exist.")


def check_balance():
    """Check the balance of an account."""
    name = input("Enter the account holder's name: ").strip()
    if name in account_holders:
        index = account_holders.index(name)
        print(f"The current balance for {name} is: {balances[index]:.2f}lv.")
    else:
        print("An account with this name does not exist.")


def list_accounts():
    """List all accounts and their balances."""
    if len(account_holders) > 0:
        for index, account in enumerate(account_holders):
            print(
                f"The account holder's name: {account}, balance: {balances[index]:.2f}lv., outstanding loan amount: {loans[index]:.2f}lv."
            )
    else:
        print("The accounts list is empty.")


def transfer_funds():
    """Transfer funds between two accounts."""
    sender_name = input("Enter the sender's name: ").strip()
    recipient_name = input("Enter the recipient's name: ").strip()
    if sender_name in account_holders and recipient_name in account_holders:
        transfer_amount = float(input("Enter the amount to transfer: "))
        sender_index = account_holders.index(sender_name)
        recipient_index = account_holders.index(recipient_name)
        if balances[sender_index] >= transfer_amount:
            balances[sender_index] -= transfer_amount
            balances[recipient_index] += transfer_amount
            transaction_histories[sender_index].append(f"Transferred to {recipient_name}: {transfer_amount:.2f}lv.")
            transaction_histories[recipient_index].append(f"Received from {sender_name}: {transfer_amount:.2f}lv.")
            print(f"The transfer amount of {transfer_amount:.2f} was successful.")
        else:
            print("Insufficient balance.")
    else:
        print("One or both accounts do not exist.")


def view_transaction_history():
    """View transaction history for a specific account."""
    name = input("Enter the account holder's name: ")
    if name in account_holders:
        index = account_holders.index(name)
        if transaction_histories[index]:
            print(f"Transactions for {name}:")
            for transaction in transaction_histories[index]:
                print(f"- {transaction}")
        else:
            print("No transactions found.")
    else:
        print("An account with this name does not exist.")


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ").strip()

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ").strip()

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


main()