import unittest
from selenium import webdriver
import page
import credentials

class B2ATests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\chromedriver.exe')
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

    def test1_AddDeleteUser(self):
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.clickAddClient()
        main_page.add_user_name = 'Tomili Jones'
        main_page.add_user_email = 'tomilijones@gmail.com'
        main_page.add_user_phone = '445666777'
        main_page.add_user_calories = '2300'
        main_page.clickSubmit()


if __name__ == "__main__":
    unittest.main()
