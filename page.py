from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import locators
import element

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    # def get_row_data(self, table, column):
    #     xpath = ".//td[" + str(column) + "]"
    #     for row in table.find_elements_by_xpath(".//tr"):
    #         print(td.text for td in row.find_elements_by_xpath(xpath))

    def get_column_data(self, table, column):
        xpath = ".//td[" + str(column) + "]"
        return list(row.find_element_by_xpath(xpath).text for row in table.find_elements_by_xpath(".//tr"))
            

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
    first_user_name = element.FirstUserName()
    first_user_email = element.FirstUserEmail()
    first_user_phone = element.FirstUserPhone()
    first_user_status = element.FirstUserStatus()
    searchbar_name = element.SearchBarName()
    searchbar_status = element.SearchBarSelectStatus()
    searchbar_gym = element.SearchBarSelectGym()
    clients_rowgroup = element.ClientsRowGroup()



    def mainPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.MainPageLocators.ADD_CLIENT_BUTTON))
        return "Clients" in self.driver.title
    
    def clickAddClient(self):

        element = self.driver.find_element(*locators.MainPageLocators.ADD_CLIENT_BUTTON)
        element.click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.MainPageLocators.ADD_SAVE_CHANGES_BUTTON))

    def clickSubmit(self):
        element = self.driver.find_element(*locators.MainPageLocators.ADD_SAVE_CHANGES_BUTTON)
        element.click()

    def clickActive(self):
        element = self.driver.find_element(*locators.MainPageLocators.ADD_ACTIVE_SLIDER)
        element.click()

    def clickSearchBarClear(self):
        element = self.driver.find_element(*locators.MainPageLocators.SEARCHBAR_CLEAR)
        element.click()
  

    





