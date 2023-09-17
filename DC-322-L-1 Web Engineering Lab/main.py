import utils


def registerAccount():
    """
        Allows a user to create a new account.

        This function prompts the user to enter a 3-digit account number and a 4-digit password.
        It checks if the entered account number already exists. If it does, a message is displayed.
        If the account number is unique, the function creates a new account with an initial balance of 100
        and stores the account details in a data file.

        Returns:
        None
        """

    accountDetails = []
    utils.registerHeader()

    while True:
        accountNumber = utils.validateUserInput(
            0, 999, "Enter 3 digit Account Number")
        accountPassword = utils.validateUserInput(
            0, 9999, "Enter 4 digit password")

        accountNumber = "ATM" + str(accountNumber).zfill(3)
        if utils.isAccountExist(accountNumber):
            utils.accountExistMsg()
        else:
            accountDetails = [accountNumber, accountPassword, 100]
            utils.writeDataToFile(accountDetails)
            break


def checkBalance(accountNumber):
    """
        Allows a user to check his/her balance.

        This function will take account number as an argument
        read data from file and on through iterating that data
        check the balance of the user

        Returns:
        account balance
    """
    atmData = utils.readDataFromFile()

    for account in atmData:
        if accountNumber == account["account_number"]:
            return account["account_balance"]


def withdrawAmount(accountNumber):
    """
        Allows a user to withdraw his/her funds.

        This function will take account number as an argument
        read data from file and on through iterating that data
        and check if the withdraw ammount is equal or greater than
        the balance then upate the object.

        Returns:
        updated atmData
    """

    atmData = utils.readDataFromFile()

    withdrawAmount = utils.validateUserInput(
        0, 99999999, "Enter Amount to withdraw: ")

    for account in atmData:
        if accountNumber == account["account_number"]:
            account_balance = int(account["account_balance"])
            if withdrawAmount <= account_balance:
                account["account_balance"] = str(
                    account_balance - withdrawAmount)
                return atmData


def depositAmmount(accountNumber):
    """
        Allows a user to Deposit his/her funds.

        This function will take account number as an argument
        read data from file and on through iterating that data
        and check if the withdraw ammount is equal or greater than
        the balance then upate the object.

        Returns:
        updated atmData
    """

    atmData = utils.readDataFromFile()

    depositAmmount = utils.validateUserInput(
        0, 99999999, "Enter Amount to withdraw: ")

    for account in atmData:
        if accountNumber == account["account_number"]:
            account_balance = int(account["account_balance"])
            account["account_balance"] = str(
                account_balance + depositAmmount)
            return atmData


def loginAccount():
    """
    Allows a user to log in to their account.

    This function prompts the user to enter their account number (in the format ATM000)
    and a 4-digit password. It checks if the entered credentials match an existing account.
    If the login is successful, it presents a menu for the user to check their balance, withdraw,
    deposit, or quit. It continues to display the menu until the user chooses to quit.

    Returns:
    None
    """
    utils.loginHeader()

    while True:
        accountNumber = input("Enter your account no : i.e ATM000 : ")
        accountPassword = utils.validateUserInput(
            0, 9999, "Enter 4-digit password")

        if utils.isUserExist(accountNumber, accountPassword):
            while True:
                utils.loginMenu()
                choice = utils.validateUserInput(1, 4, "Enter Your Choice : ")

                if choice == 1:
                    balance = checkBalance(accountNumber)
                    print("Account balance is : ", balance)
                elif choice == 2:
                    atmData = withdrawAmount(accountNumber)
                    utils.updatfileData(atmData)
                    utils.withdrawAmountMsg()
                elif choice == 3:
                    atmData = depositAmount(accountNumber)
                    utils.updatfileData(atmData)
                    utils.depositAmountMsg()
                else:
                    print("Quitting")
                    return
        else:
            utils.accountNotExistMsg()


if __name__ == "__main__":

    """
        This script presents a menu-driven program for user account management.

        It repeatedly displays a menu with two options: login or register an account. The user is prompted to choose one of these options, and their choice is validated. After performing the chosen action (login or registration), the user is asked if they want to continue. The program continues to run until the user decides to exit.

        Usage:
        1. Run this script.
        2. Choose between login (1) or registration (2).
        3. After each operation, you can choose to continue or exit by entering 'yes' or 'no'.

        Note: The actual implementation of 'loginAccount' and 'registerAccount' functions is not shown in this code snippet.
    """
    
    while True:
        utils.startProgram()
        choice = utils.validateUserInput(1, 2, "Enter Your Choice : ")

        if choice == 1:
            loginAccount()
        else:
            registerAccount()

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != "yes":
            break
