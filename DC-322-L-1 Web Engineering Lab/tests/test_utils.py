import unittest
from unittest.mock import mock_open, patch
import utils  # Import your 'utils' module here


# in these classes the unittest.mock.patch method modify the behaviour of the
# input tmethod for its use for the test just temporarly and replce the input
# with the mock object that return return value  when ever its called and the
# side_effect will provde the sequence of values that wiill be returned

class Test_ValidateUserInput(unittest.TestCase):

    def test_positive_input(self):
        with patch("builtins.input", return_value="5"):
            result = utils.validateUserInput(
                1, 10, "Enter a number between 1 and 10")
            self.assertEqual(result, 5)

    def test_negative_input(self):
        with patch("builtins.input", side_effect=["-5", "15", "abc", "6"]):
            result = utils.validateUserInput(
                1, 10, "Enter a number between 1 and 10")
            self.assertNotEqual(result, 7)

    def test_random_input(self):
        with patch("builtins.input", side_effect=["8", "9"]):
            result = utils.validateUserInput(
                1, 10, "Enter a number between 1 and 10")
            self.assertEqual(result, 8)


# Tests to check if the account exist
class Test_IsAccountExist(unittest.TestCase):

    def test_positive(self):
        result = utils.isAccountExist("ATM001")
        self.assertTrue(result)

    def test_negative(self):
        result = utils.isAccountExist("NonExistentAccount")
        self.assertFalse(result)

    def test_random(self):
        result = utils.isAccountExist("RandomAccountNumber")
        self.assertFalse(result)


# Tests to check if the User exist
class Test_IsUserExist(unittest.TestCase):

    def test_positive(self):
        result = utils.isUserExist("ATM001", 1234)
        self.assertTrue(result)

    def test_negative(self):
        result = utils.isUserExist("ABC111", 1234)
        self.assertFalse(result)

    def test_random(self):
        result = utils.isUserExist("Ran344", 0000)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
