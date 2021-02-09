import unittest
from selenium import webdriver
import page

class B2ATests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\chromedriver.exe')
        self.driver.get('https://stag.portal.b2a.ie/')
        '''Welcome page'''
        welcome_page = page.WelcomePage(self.driver)
        assert welcome_page.welcomePageCheck(), "Welcome page text did not match"
        welcome_page.clickGoToApp()
        '''Login Page'''
        login_page = page.LoginPage(self.driver)
        assert login_page.loginPageCheck(), "Login page text did not match"
        login_page.email_text_element = 'jania.k94@gmail.com'
        login_page.pass_text_element = 'Cypis1313' 
        login_page.clickLogin()


    def tearDown(self):
        self.driver.close()

    def test_firstTest(self):

        assert True

if __name__ == "__main__":
    unittest.main()
