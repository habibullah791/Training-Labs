from utils import *


def registerAccount():
    """
         Allows a user to create a new account.

        @param a: first number (3-digit account number)
        @param b: second number (4-digit password)
        @desc: Create a new account with an initial balance of 100 if the account number is unique.
        @return: None
        """
    registerHeader()

    while True:
        accountNumber = validateUserInput(
            0, 999, "Enter 3 digit Account Number")
        accountPassword = validateUserInput(0, 9999, "Enter 4 digit password")

        accountNumber = "ATM" + str(accountNumber).zfill(3)
        if isAccountExist(accountNumber):
            accountExistMsg()
        else:
            atmData.append({
                "account_number": accountNumber,
                "account_password": accountPassword,
                "account_balance": 100
            })
            accountCreatedMsg()
            break


def checkBalance(accountNumber):
    """
        Allows a user to check their account balance.

        @param accountNumber: The account number of the user.
        @desc: This function takes an account number as an argument, 
            reads data from a file, and iterates through the data
            to check the balance of the user.

        @return: The account balance of the user.
    """

    for account in atmData:
        if accountNumber == account["account_number"]:
            return account["account_balance"]


def withdrawAmount(accountNumber):
    """
        Allow a user to withdraw funds from their account.

        @param accountNumber: The account number of the user.
        @desc: This function reads data from a file, iterates through the data,
            and checks if the withdrawal amount is equal to or greater than
            the account balance. If sufficient funds are available, it updates
            the account balance accordingly.

        @return: The updated account data.
    """

    withdrawAmount = validateUserInput(
        0, 99999999, "Enter Amount to withdraw: ")

    for account in atmData:
        if accountNumber == account["account_number"]:
            account_balance = int(account["account_balance"])
            if withdrawAmount <= account_balance:
                account["account_balance"] = str(
                    account_balance - withdrawAmount)
                return True
            else:
                return False


def depositAmmount(accountNumber):
    """
        Allows a user to Deposit funds into their account.

        @param accountNumber: The account number of the user.
        @desc: This function takes the account number as an argument,
            reads data from a file, iterates through the data,
            and checks if the deposit amount is valid.
        @return: Updated atmData, which is an array of user dictionaries
                that have been updated after the deposit has been made.
    """

    depositAmmount = validateUserInput(0, 99999999, "Enter Amount to withdraw: ")

    for account in atmData:
        if accountNumber == account["account_number"]:
            account_balance = int(account["account_balance"])
            account["account_balance"] = str(account_balance + depositAmmount)
            return True
        else:
            False


def loginAccount():
    """
        User Account Login Function

        @param account_number: The user's account number (in the format ATM000).
        @param password: A 4-digit password for account authentication.
        @desc: Allows a user to log in to their account by verifying the provided credentials.
            If successful, it presents a menu for balance checking, withdrawal, deposit, or quitting.
        @return: None
    """
    loginHeader()

    while True:
        accountNumber = input("Enter your account no : i.e ATM000 : ")
        accountPassword = validateUserInput(0, 9999, "Enter 4-digit password")

        if isUserExist(accountNumber, accountPassword):
            while True:
                loginMenu()
                choice = validateUserInput(1, 4, "Enter Your Choice : ")

                if choice == 1:
                    balance = checkBalance(accountNumber)
                    print("Account balance is : ", balance)
                elif choice == 2:
                    withdrawAmount(accountNumber)
                    withdrawAmountMsg()
                elif choice == 3:
                    depositAmmount(accountNumber)
                    depositAmmountMsg()
                else:
                    print("Quitting")
                    return
        else:
            accountNotExistMsg()


if __name__ == "__main__":

    """
        This script presents a menu-driven program for user account management.

        It repeatedly displays a menu with two options: login or register an account. 
        The user is prompted to choose one of these options, and their choice is validated. 
        After performing the chosen action (login or registration), the user is asked if they want to continue. 
        The program continues to run until the user decides to exit.
    """

    # Call the readDataFromFile function to populate atmData
    readDataFromFile()

    while True:
        startProgram()
        choice = validateUserInput(1, 2, "Enter Your Choice : ")

        if choice == 1:
            loginAccount()
        else:
            registerAccount()

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != "yes":
            updatfileData()
            break
