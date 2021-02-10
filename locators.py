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
    ADD_ACTIVE_SLIDER = (By.ID, 'mat-slide-toggle-4')
    ADD_NAME_FIELD = (By.ID, 'mat-input-63')
    ADD_EMAIL_FIELD = (By.ID, 'mat-input-64')
    ADD_PHONE_FIELD = (By.ID, 'mat-input-65')
    ADD_CALORIES_FIELD = (By.ID, 'mat-input-66')
    ADD_GYM_FIELD = (By.ID, 'mat-select-147')
    ADD_GYM_FIELD_FRANKFIELD = (By.ID, 'mat-option-457')



