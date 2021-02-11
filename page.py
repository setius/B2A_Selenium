from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import locators
import element

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

class WelcomePage(BasePage):

    def welcomePageCheck(self):
        WebDriverWait(self.driver, 2).until(
            lambda driver: driver.find_element(*locators.WelcomePageLocators.GO_BUTTON))
        return "Welcome to B2A" in self.driver.page_source

    def clickGoToApp(self):

        element = self.driver.find_element(*locators.WelcomePageLocators.GO_BUTTON)
        element.click()

class LoginPage(BasePage):

    email_text_element = element.LoginEmailElement()
    pass_text_element = element.LoginPassElement()

    def loginPageCheck(self):
        WebDriverWait(self.driver, 2).until(
            lambda driver: driver.find_element(*locators.LoginPageLocators.LOGIN_BUTTON))
        return "Login" in self.driver.page_source

    def clickLogin(self):
        element = self.driver.find_element(*locators.LoginPageLocators.LOGIN_BUTTON)
        element.click()

class MainPage(BasePage):

    add_user_name = element.AddUserName()
    add_user_email = element.AddUserEmail()
    add_user_phone = element.AddUserPhone()
    add_user_calories = element.AddUserCalories()
    add_user_gym = element.AddUserSelectGym()
    first_user_select_gym = element.FirstUserSelectGym()


    def mainPageCheck(self):
        WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(*locators.MainPageLocators.ADD_CLIENT_BUTTON))
        return "Clients" in self.driver.title
    
    def clickAddClient(self):

        element = self.driver.find_element(*locators.MainPageLocators.ADD_CLIENT_BUTTON)
        element.click()
        WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(*locators.MainPageLocators.ADD_SAVE_CHANGES_BUTTON))

    def clickSubmit(self):
        element = self.driver.find_element(*locators.MainPageLocators.ADD_SAVE_CHANGES_BUTTON)
        element.click()

    def clickActive(self):
        element = self.driver.find_element(*locators.MainPageLocators.ADD_ACTIVE_SLIDER)
        element.click()

    def verifyNewUser(self, name, email, phone, gym, active):
        element = self.driver.find_element()   

    





