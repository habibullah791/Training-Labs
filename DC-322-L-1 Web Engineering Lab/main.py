import utils

# Create a new user
def registerAccount():

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


# checking balance
def checkBalance(accountNumber):
    atmData = utils.readDataFromFile()

    for account in atmData:
        if accountNumber == account["account_number"]:
            return account["account_balance"]


# withdraw amount from account
def withdrawAmount(accountNumber):

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


# Deposit amount in the account
def depositAmmount(accountNumber):
    atmData = utils.readDataFromFile()

    depositAmmount = utils.validateUserInput(
        0, 99999999, "Enter Amount to withdraw: ")

    for account in atmData:
        if accountNumber == account["account_number"]:
            account_balance = int(account["account_balance"])
            account["account_balance"] = str(
                account_balance + depositAmmount)
            return atmData


# login account
def loginAccount():
    utils.loginHeader()

    while True:
        accountNumber = input("Enter your account no : i.e ATM000 : ")
        accountPassword = utils.validateUserInput(
            0, 9999, "Enter 4 digit password")

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
                    atmData = depositAmmount(accountNumber)
                    utils.updatfileData(atmData)
                    utils.depositAmmountMsg()
                else:
                    print("Quitting")
                    return
        else:
            utils.accountNotExistMsg()


# main function
if __name__ == "__main__":
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
