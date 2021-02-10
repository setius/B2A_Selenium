"""File contains locators described as tuples divided by page class"""

from selenium.webdriver.common.by import By

class WelcomePageLocators(object):

    GO_BUTTON = (By.XPATH, '//span[normalize-space()="Go to app"]')

class LoginPageLocators(object):

    LOGIN_BUTTON = (By.XPATH, '//span[normalize-space()="Login"]')
    LOGIN_FIELD = (By.ID, 'mat-input-0')
    PASS_FIELD = (By.ID, 'mat-input-1')

class MainPageLocators(object):

    ADD_CLIENT_BUTTON = (By.XPATH, '//button[@routerlink="/admin/clients/new-client"]')
    ADD_SAVE_CHANGES_BUTTON = (By.XPATH, '//span[normalize-space()="Save Changes"]')
    ADD_ACTIVE_SLIDER = (By.CLASS_NAME, 'mat-slide-toggle-bar')
    ADD_NAME_FIELD = (By.XPATH, '//input[@formcontrolname="name"]')
    ADD_EMAIL_FIELD = (By.XPATH, '//input[@formcontrolname="email"]')
    ADD_PHONE_FIELD = (By.XPATH, '//input[@formcontrolname="phone"]')
    ADD_CALORIES_FIELD = (By.XPATH, '//input[@formcontrolname="caloriesTarget"]')
    ADD_GYM_FIELD = (By.XPATH, '//mat-select[@formcontrolname="gymCode"]')
    ADD_GYM_FIELD_FRANKFIELD = (By.XPATH, '//span[normalize-space()="Frankfield"]')



