import unittest
from selenium import webdriver
import page
import credentials
import time

class B2ATests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(credentials.WEBSITE)
        '''Welcome page'''
        welcome_page = page.WelcomePage(self.driver)
        assert welcome_page.welcomePageCheck(), "Welcome page text did not match"
        welcome_page.clickGoToApp()
        '''Login Page'''
        login_page = page.LoginPage(self.driver)
        assert login_page.loginPageCheck(), "Login page text did not match"
        login_page.email_text_element = credentials.USER
        login_page.pass_text_element = credentials.PASS 
        login_page.clickLogin()


    def tearDown(self):
        self.driver.close()

    def test1_AddUser(self):
        '''This test case verifies functionality of adding new user
            and also checks if user attributes are set properly
            Disabled because we cannot delete users in GUI'''
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        '''
        main_page.clickAddClient()
        main_page.clickActive()
        main_page.add_user_name = 'Carl Johnson'
        main_page.add_user_email = 'cj_grooveStreetFL@gmail.com'
        main_page.add_user_phone = '445676777'
        main_page.add_user_gym = 'Frankfield'
        main_page.add_user_calories = '2300'
        main_page.clickSubmit()
        '''
        main_page.first_user_select_gym

    def dis_test2_UserAttributesVerification(self):
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"


        


if __name__ == "__main__":
    unittest.main()
