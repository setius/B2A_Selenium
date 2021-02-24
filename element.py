from selenium.webdriver.support.ui import WebDriverWait
import locators


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text field to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Returns specified element"""
        driver = obj.driver
        WebDriverWait(driver, 5).until(
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
        self.xpath = "//span[@class='" + self.classname + "' and normalize-space()='" + value +"']" 
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath(self.xpath))
        driver.find_element_by_xpath(self.xpath).click()


    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator)) 
        element = driver.find_element(*self.locator)
        return element


class BaseUploadFileElement(object):
    """Base class used to handle file upload input."""

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(value)



# Generic Page Elements

class RowgroupElement(BasePageElement):

    locator = locators.GenericLocators.ROWGROUP



# Login Page elements
class LoginEmailElement(BasePageElement):

    locator = locators.LoginPageLocators.LOGIN_FIELD

class LoginPassElement(BasePageElement):

    locator = locators.LoginPageLocators.PASS_FIELD



# Main Page elements

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

class FirstUserName(BasePageElement):

    locator = locators.MainPageLocators.CLIENT_LIST_FIRST_ROW_NAME

class FirstUserEmail(BasePageElement):

    locator = locators.MainPageLocators.CLIENT_LIST_FIRST_ROW_EMAIL

class FirstUserPhone(BasePageElement):

    locator = locators.MainPageLocators.CLIENT_LIST_FIRST_ROW_PHONE

class FirstUserStatus(BasePageElement):

    locator = locators.MainPageLocators.CLIENT_LIST_FIRST_ROW_STATUS

class SearchBarName(BasePageElement):
    
    locator = locators.MainPageLocators.SEARCHBAR_NAME

class SearchBarSelectStatus(BaseDropDownBarElement):

    locator = locators.MainPageLocators.SEARCHBAR_STATUS
    classname = 'mat-option-text'

class SearchBarSelectGym(BaseDropDownBarElement):

    locator = locators.MainPageLocators.SEARCHBAR_GYM
    classname = 'mat-option-text'

class ClientsRowGroup(BasePageElement):

    locator = locators.GenericLocators.ROWGROUP



# Recipes Page elements

class InputRecipeName(BasePageElement):

    locator = locators.RecipesPageLocators.ADD_RECIPE_TITLE

class UploadRecipeIMG(BaseUploadFileElement):

    locator = locators.RecipesPageLocators.ADD_RECIPE_IMG_INPUT

class UploadRecipePDF(BaseUploadFileElement):

    locator = locators.RecipesPageLocators.ADD_RECIPE_PDF_INPUT

class FirstRecipeName(BasePageElement):

    locator = locators.RecipesPageLocators.RECIPES_FIRST_ROW_TITLE



# Workouts Page elements

class InputWorkoutYoutubeLink(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.ADD_WORKOUT_YT

class InputWorkoutDescription(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.ADD_WORKOUT_DESC

class InputWorkoutTitle(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.ADD_WORKOUT_TITLE

class InputWorkoutBodyPart(BaseDropDownBarElement):

    locator = locators.WorkoutProgramsPageLocators.ADD_WORKOUT_BODYPART
    classname = 'mat-option-text'

class FirstWorkoutTitle(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_TITLE

class FirstWorkoutDesc(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_DESC

class FirstWorkoutBodyPart(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_BODYPART

class FirstWorkoutYoutube(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_YT

class SearchbarWorkoutStatus(BaseDropDownBarElement):

    locator = locators.WorkoutProgramsPageLocators.SEARCH_STATUS
    classname = 'mat-option-text'

class SearchbarWorkout(BasePageElement):

    locator = locators.WorkoutProgramsPageLocators.SEARCH_FIELD

class WorkoutsRowGroup(BasePageElement):

    locator = locators.GenericLocators.ROWGROUP




# Testimonials Page elements

class CreateTestimonialButton(BasePageElement):

    locator = locators.TestimonialsPageLocators.ADD_TESTIMONIAL_BUTTON

class CreateTestimonialNameInput(BasePageElement):

    locator = locators.TestimonialsPageLocators.ADD_TEST_NAME

class CreateTestimonialDescInput(BasePageElement):

    locator = locators.TestimonialsPageLocators.ADD_TEST_DESC

class CreateTestimonialFileInplut(BaseUploadFileElement):

    locator = locators.TestimonialsPageLocators.ADD_TEST_IMG

class CreateTestimonialSubmitButton(BasePageElement):

    locator = locators.TestimonialsPageLocators.ADD_TEST_SUBMIT_BUTTON

class TestimonialFirstRowDeleteButton(BasePageElement):

    locator = locators.TestimonialsPageLocators.FIRST_ROW_DELETE_BUTTON











