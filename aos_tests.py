import unittest
import aos_methods as methods
import aos_locators as locators

class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory

        methods.setUp()
        methods.create_new_user()
        methods.log_out()
        methods.login(locators.new_username, locators.new_password)
        methods.log_out()
        methods.teardown()
