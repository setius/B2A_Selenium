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
    GO_TO_RECIPES = (By.XPATH, '//a[@href="/admin/recipes"]')
    GO_TO_WORKOUTS = (By.XPATH, '//a[@href="/admin/workout-programs"]')
    GO_TO_RECIPES = (By.XPATH, '//a[@href="/admin/testimonials"]')

class RecipesPageLocators(object):

    ADD_RECIPE_BUTTON = (By.XPATH, '//mat-icon[normalize-space()="add"]')
    ADD_RECIPE_TITLE = (By.XPATH, '//input[@placeholder="Title"]')
    ADD_RECIPE_IMG_INPUT = (By.XPATH, '//div[@class="form-control-attachments"]/div[1]//input[@type="file"]')
    ADD_RECIPE_PDF_INPUT = (By.XPATH, '//div[@class="form-control-attachments"]/div[2]//input[@type="file"]')
    RECIPE_SUBMIT_BUTTON = (By.XPATH, '//button[not(@disabled)]/span[normalize-space()="Submit"]')
    REMOVE_IMG_BUTTON = (By.XPATH, '//span[normalize-space()="Remove image"]')
    REMOVE_PDF_BUTTON = (By.XPATH, '//span[normalize-space()="Remove recipe file"]')
    RECIPES_FIRST_ROW_TITLE = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[2]')
    RECIPES_FIRST_ROW_DELETE = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[5]/div/button[2]')
    RECIPES_CONFIRM_DELETE = (By.XPATH, '//span[normalize-space()="OK"]')


class WorkoutProgramsPageLocators(object):

    PAGE_HEADER = (By.XPATH, '//h2[normalize-space()="Workout programs"]')
    ADD_WORKOUT_BUTTON = (By.XPATH, '//mat-icon[normalize-space()="add"]')
    ADD_WORKOUT_YT = (By.XPATH, '//input[@formcontrolname="youtubeVideoId"]')
    ADD_WORKOUT_DESC = (By.XPATH, '//input[@formcontrolname="description"]')
    ADD_WORKOUT_TITLE = (By.XPATH, '//input[@formcontrolname="title"]')
    ADD_WORKOUT_BODYPART = (By.XPATH, '//mat-select[@formcontrolname="bodyPart"]')
    ADD_WORKOUT_SUBMIT = (By.XPATH, '//div[@class="modal-actions"]/button[2]')
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type to search"]')
    SEARCH_STATUS = (By.XPATH, '//div[@class="top-form"]/mat-form-field[2]')
    WORKOUT_FIRST_ROW = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]')
    WORKOUT_FIRST_ROW_BODYPART = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[2]')
    WORKOUT_FIRST_ROW_DESC = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[4]')
    WORKOUT_FIRST_ROW_TITLE = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[5]')
    WORKOUT_FIRST_ROW_YT = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[7]/a')
    WORKOUT_FIRST_ROW_STATUS = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[6]/mat-form-field/div/div')
    WORKOUT_FIRST_ROW_PREVIEW_BUTTON = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[8]/div/button[1]')
    WORKOUT_FIRST_ROW_DELETE_BUTTON = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[8]/div/button[3]')
    WORKOUT_LIST_TAB = (By.XPATH, '//tbody[@role="rowgroup"]')
    PREVIEW_CANCEL_BUTTON = (By.XPATH, '//span[normalize-space()="Cancel"]')
    

class TestimonialsPageLocators(object):

    PAGE_HEADER = (By.XPATH, '//h2[normalize-space()="Testimonials"]')
    ADD_TESTIMONIAL_BUTTON = (By.XPATH, '//mat-icon[normalize-space()="add"]')

