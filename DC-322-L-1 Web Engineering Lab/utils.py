# utils.py

import os


def startProgram():
    """Display initial program header."""

    os.system('cls')
    print("---------------------")
    print("***  ATM System  ***")
    print("---------------------")
    print("1. Login")
    print("2. Sign up")
    print("---------------------")


def registerHeader():
    """Display registration header."""

    os.system('cls')
    print("")
    print("-------------------------------")
    print("***  Account Regestration  ***")
    print("-------------------------------\n")


# login header logs
def loginHeader():
    """Display login header."""

    os.system('cls')
    print("")
    print("------------------------")
    print("***  Account login  ***")
    print("------------------------")


# login menu
def loginMenu():
    """Display login menu options."""

    print("")
    print("---------------------")
    print("***  Login Menue  ***")
    print("---------------------")
    print("1. Check Your Balance.")
    print("2. Withdraw .")
    print("3. Deposit.")
    print("4. Exit.")
    print("---------------------\n")


def accountCreatedMsg():
    """Display account creation success message."""

    print("--------------------------------------")
    print("***  Account Created Successfully  ***")
    print("--------------------------------------\n")


def accountExistMsg():
    """Display account existence error message."""

    print("-------------------------------------------------------------")
    print("***  Error !! Account Exist Use different 3 digit combo . ***")
    print("-----------------------------------------------------------\n")


def accountNotExistMsg():
    """Display account non-existence error message."""

    print("------------------------------------------------------------------")
    print("***  Error !! Account Not Exist Use different 3 digit combo . ***")
    print("-----------------------------------------------------------------\n")


def withdrawAmountMsg():
    """Display withdrawal confirmation message."""

    print("-----------------------------------------")
    print("***  You've Withdrawn the ammount  . ***")
    print("-----------------------------------------")


def depositAmmountMsg():
    """Display withdrawal confirmation message."""

    print("-----------------------------------------")
    print("***  You've Deposited the ammount  . ***")
    print("-----------------------------------------")


def validateUserInput(min, max, msg):
    """
        Validate the user input

        This function will take the min, maz and xustom message
        and check if the user enter the right value until its
        right and then retuen the correct value

        Returns:
        user input
    """

    while True:
        try:

            choice = int(input(msg + " : "))
            if min <= choice <= max:
                return choice
            else:
                print("Invalid Input: Try again")
        except ValueError:
            print("Invalid Input: Please enter a valid integer.")


def readDataFromFile():
    """
        Read Data from the file and store in a variable

        This function will read data from file and store the 
        data in a list of dictionary and then return it 

        Return:
        atmData
    """
    atmData = []

    with open('atmData.txt', 'r') as file:

        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 3:
                accountNumber, accountPassword, balance = parts
                atmData.append({
                    "account_number": accountNumber,
                    "account_password": accountPassword,
                    "account_balance": balance
                })

    return atmData


def writeDataToFile(accountDetails):
    """
        Write data to the file 

        This function will get the list of dictionary 
        and then convert each dictionary in list and then 
        in string and overite the existing file it will be 
        account detail of one new user

        Return:
        none
    """

    accountData = [str(item) for item in accountDetails]
    accountData = ','.join(accountData)

    with open('atmData.txt', 'a') as file:
        file.write(accountData+"\n")

    accountCreatedMsg()


def updatfileData(atmData):
    """
        Upate data of existing user in file

        This function will get the list of dictionary 
        and then convert each dictionary in list and then 
        in string and overite the existing file

        Return:
        none
    """

    with open('atmData.txt', 'w') as file:

        for data in atmData:
            accountData = [str(data[key]) for key in data]
            accountData = ','.join(accountData)
            file.write(accountData+"\n")


def isAccountExist(accountNumber):
    """
        check If account Exist

        This function have a accountnumber as an argument
        and will read data from file and then iterate the data 
        and check if the user exist or not 

        Returns:
        True or False
    """

    atmData = readDataFromFile()

    for account in atmData:
        if accountNumber == account["account_number"]:
            return True
        else:
            return False


# check if the user exist

def isUserExist(accountNumber, accountPassword):
    """
        check If user Exist

        This function have a accountnumber, and password as an argument
        and will read data from file and then iterate the data 
        and check if the user exist or not 

        Returns:
        True or False
    """

    atmData = readDataFromFile()
    for account in atmData:
        if accountNumber == account["account_number"]:
            if accountPassword == int(account["account_password"]):
                return True
            else:
                return False
