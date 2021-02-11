from selenium.webdriver.support.ui import WebDriverWait
import locators


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text field to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element

class BaseDropDownBarElement(object):
    '''Base element to handle drop down bars'''
    def __set__(self, obj, value):
        """Sets the text field to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).click()
        self.xpath = "//span[@class='" + self.classname + "' and text()='" + value +"']" 
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath(self.xpath))
        driver.find_element_by_xpath(self.xpath).click()


    def __get__(self, obj, value, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).click()
        self.xpath = "//span[@class='" + self.classname + "' and text()='" + value +"']" 
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath(self.xpath))
        element = driver.find_element_by_xpath(self.xpath)
        return element

class LoginEmailElement(BasePageElement):

    locator = locators.LoginPageLocators.LOGIN_FIELD

class LoginPassElement(BasePageElement):

    locator = locators.LoginPageLocators.PASS_FIELD

class AddUserName(BasePageElement):

    locator = locators.MainPageLocators.ADD_NAME_FIELD

class AddUserEmail(BasePageElement):

    locator = locators.MainPageLocators.ADD_EMAIL_FIELD

class AddUserPhone(BasePageElement):

    locator = locators.MainPageLocators.ADD_PHONE_FIELD

class AddUserCalories(BasePageElement):

    locator = locators.MainPageLocators.ADD_CALORIES_FIELD

class AddUserSelectGym(BaseDropDownBarElement):

    locator = locators.MainPageLocators.ADD_GYM_FIELD
    classname = 'mat-option-text'

class AddUserSelectGym(BaseDropDownBarElement):

    locator = locators.MainPageLocators.ADD_GYM_FIELD
    classname = 'mat-option-text'

class FirstUserSelectGym(BaseDropDownBarElement):

    locator = locators.MainPageLocators.CLIENT_LIST_FIRST_ROW_GYM
    classname = 'mat-option-text'


