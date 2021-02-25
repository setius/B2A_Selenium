"""File contains locators described as tuples divided by page class"""

from selenium.webdriver.common.by import By

class GenericLocators(object):

    ROWGROUP = (By.XPATH, '//tbody[@role="rowgroup"]')


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
    SEARCHBAR_NAME = (By.XPATH, '//input[@placeholder="Type to search"]')
    SEARCHBAR_STATUS = (By.XPATH, '//div[@class="top-form"]/mat-form-field[2]')
    SEARCHBAR_GYM = (By.XPATH, '//div[@class="top-form"]/mat-form-field[4]')
    SEARCHBAR_CLEAR = (By.XPATH, '//div[@class="top-form"]/button')
    GO_TO_RECIPES = (By.XPATH, '//a[@href="/admin/recipes"]')
    GO_TO_WORKOUTS = (By.XPATH, '//a[@href="/admin/workout-programs"]')
    GO_TO_TESTIMONIALS = (By.XPATH, '//a[@href="/admin/testimonials"]')

class RecipesPageLocators(object):

    ADD_RECIPE_BUTTON = (By.XPATH, '//mat-icon[normalize-space()="add"]')
    ADD_RECIPE_TITLE = (By.XPATH, '//input[@placeholder="Title"]')
    ADD_RECIPE_IMG_INPUT = (By.XPATH, '//div[@class="form-control-attachments"]/div[1]//input[@type="file"]')
    ADD_RECIPE_PDF_INPUT = (By.XPATH, '//div[@class="form-control-attachments"]/div[2]//input[@type="file"]')
    RECIPE_SUBMIT_BUTTON = (By.XPATH, '//button[not(@disabled)]/span[normalize-space()="Submit"]')
    REMOVE_IMG_BUTTON = (By.XPATH, '//span[normalize-space()="Remove image"]')
    REMOVE_PDF_BUTTON = (By.XPATH, '//span[normalize-space()="Remove recipe file"]')
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
    WORKOUT_FIRST_ROW_PREVIEW_BUTTON = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[8]/div/button[1]')
    WORKOUT_FIRST_ROW_DELETE_BUTTON = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[8]/div/button[3]')
    PREVIEW_CANCEL_BUTTON = (By.XPATH, '//span[normalize-space()="Cancel"]')
    

class TestimonialsPageLocators(object):

    PAGE_HEADER = (By.XPATH, '//h2[normalize-space()="Testimonials"]')
    ADD_TESTIMONIAL_BUTTON = (By.XPATH, '//mat-icon[normalize-space()="add"]')
    FIRST_ROW_DELETE_BUTTON = (By.XPATH, '//tbody[@role="rowgroup"]/tr[1]/td[6]/div/button[2]')
    ADD_TEST_NAME = (By.XPATH, '//input[@formcontrolname="clientName"]')
    ADD_TEST_DESC = (By.XPATH, '//input[@formcontrolname="description"]')
    ADD_TEST_IMG = (By.XPATH, '//input[@type="file"]')
    ADD_TEST_SUBMIT_BUTTON = (By.XPATH, '//button[not(@disabled)]/span[normalize-space()="Submit"]')


