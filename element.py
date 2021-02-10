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
        return element.get_attribute("value")

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

