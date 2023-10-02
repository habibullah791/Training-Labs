# utils.py
import os



#globalVariables
atmData = []


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
        Validate the user input.

            @param min_value: The minimum allowed value for user input.
            @param max_value: The maximum allowed value for user input.
            @param message: A custom message to prompt the user for input.

            @desc: This function repeatedly prompts the user for input until they enter a valid value
            within the specified range (inclusive of min_value and max_value). It uses the provided
            message as the input prompt.

            @return: The validated user input that falls within the specified range.
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
        Read data from a file and store it in a list of dictionaries.

        @param: None
        @desc: Read data from the file and store it in a list of dictionaries.
        @return: List of dictionaries containing account data.
    """

    try:
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
    except FileNotFoundError:
        print("The file 'atmData.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



def updatfileData():
    """
    Update data of existing user in file

    @param atmData: A list of dictionary containing account data
    @desc: This function takes a list of dictionaries representing account data
        and updates the data in an existing file.
    @return: None
    """

    try:
        with open('atmData.txt', 'w') as file:

            for data in atmData:
                # Convert each item in accountDetails to a string
                accountData = [str(data[key]) for key in data]
                # Join the string items using a comma as the separator
                accountData = ','.join(accountData)
                file.write(accountData + "\n")
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")


def isAccountExist(accountNumber):
    """
        Check if an account exists.

        @param accountNumber: Account number to check.
        @type accountNumber: str
        @return: True if the account exists, False otherwise.
        @rtype: bool
    """


    for account in atmData:
        if accountNumber == account["account_number"]:
            return True
        else:
            return False


def isUserExist(accountNumber, accountPassword):
    """
        Check if a user exists.

        @param accountNumber: The user's account number.
        @param accountPassword: The user's account password.
        @desc: This function reads data from a file, iterates through the data, 
            and checks if a user with the provided account number and password exists.
        @return: True if the user exists, False otherwise.
    """

    for account in atmData:
        if accountNumber == account["account_number"]:
            if accountPassword == int(account["account_password"]):
                return True
            else:
                return False
