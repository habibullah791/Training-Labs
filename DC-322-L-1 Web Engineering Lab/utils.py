# utils.py

import os
def startProgram():
    os.system('cls')
    print("---------------------")
    print("***  ATM System  ***")
    print("---------------------")
    print("1. Login")
    print("2. Sign up")
    print("---------------------")


# register header logs
def registerHeader():
    os.system('cls')
    print("")
    print("-------------------------------")
    print("***  Account Regestration  ***")
    print("-------------------------------\n")


# login header logs
def loginHeader():
    os.system('cls')
    print("")
    print("------------------------")
    print("***  Account login  ***")
    print("------------------------")


# login menu
def loginMenu():
    print("")
    print("---------------------")
    print("***  Login Menue  ***")
    print("---------------------")
    print("1. Check Your Balance.")
    print("2. Withdraw .")
    print("3. Deposit.")
    print("4. Exit.")
    print("---------------------\n")


# Account created messages log
def accountCreatedMsg():
    print("--------------------------------------")
    print("***  Account Created Successfully  ***")
    print("--------------------------------------\n")


# Account Exist messages log
def accountExistMsg():
    print("-------------------------------------------------------------")
    print("***  Error !! Account Exist Use different 3 digit combo . ***")
    print("-----------------------------------------------------------\n")


# Account not Exist messages log
def accountNotExistMsg():
    print("------------------------------------------------------------------")
    print("***  Error !! Account Not Exist Use different 3 digit combo . ***")
    print("-----------------------------------------------------------------\n")


# Withdraw Ammount messages log
def withdrawAmountMsg():
    print("-----------------------------------------")
    print("***  You've Withdrawn the ammount  . ***")
    print("-----------------------------------------")


# Deposited Ammount messages log
def depositAmmountMsg():
    print("-----------------------------------------")
    print("***  You've Deposited the ammount  . ***")
    print("-----------------------------------------")
# validate user input


def validateUserInput(min, max, msg):

    while True:
        try:
            choice = int(input(msg + " : "))
            if min <= choice <= max:
                return choice
            else:
                print("Invalid Input: Try again")
        except ValueError:
            print("Invalid Input: Please enter a valid integer.")


# Read data from the file and return the data dictionary
def readDataFromFile():

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


# write data to the file and print success mesage
def writeDataToFile(accountDetails):

    accountData = [str(item) for item in accountDetails]
    accountData = ','.join(accountData)

    with open('atmData.txt', 'a') as file:
        file.write(accountData+"\n")

    accountCreatedMsg()


# update the file
def updatfileData(atmData):

    with open('atmData.txt', 'w') as file:

        for data in atmData:
            accountData = [str(data[key]) for key in data]
            accountData = ','.join(accountData)
            file.write(accountData+"\n")


# check if account existed
def isAccountExist(accountNumber):
    atmData = readDataFromFile()

    for account in atmData:
        if accountNumber == account["account_number"]:
            return True
        else:
            return False


# check if the user exist

def isUserExist(accountNumber, accountPassword):

    atmData = readDataFromFile()
    for account in atmData:
        if accountNumber == account["account_number"]:
            if accountPassword == int(account["account_password"]):
                return True
            else:
                return False
