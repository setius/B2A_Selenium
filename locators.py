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
    CLIENT_LIST_TAB = (By.XPATH, '//tbody[@role="rowgroup"]')
    CLIENT_LIST_FIRST_ROW = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]')
    CLIENT_LIST_FIRST_ROW_ID = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[1]')
    CLIENT_LIST_FIRST_ROW_NAME = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[2]')
    CLIENT_LIST_FIRST_ROW_EMAIL = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[3]')
    CLIENT_LIST_FIRST_ROW_PHONE = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[4]')
    CLIENT_LIST_FIRST_ROW_GYM = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[5]/mat-form-field/div/div')
    CLIENT_LIST_FIRST_ROW_STATUS = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[8]')
    SEARCHBAR_NAME = (By.XPATH, '//input[@placeholder="Type to search"]')
    SEARCHBAR_STATUS = (By.XPATH, '//div[@class="top-form"]/mat-form-field[2]')
    SEARCHBAR_GYM = (By.XPATH, '//div[@class="top-form"]/mat-form-field[4]')
    SEARCHBAR_CLEAR = (By.XPATH, '//div[@class="top-form"]/button')



