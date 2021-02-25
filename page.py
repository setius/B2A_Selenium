from selenium.webdriver.support.ui import WebDriverWait
import time
import locators
import element

class BasePage(object):

    rowgroup = element.RowgroupElement()

    def __init__(self,driver):
        self.driver = driver

    def get_column_data(self, table, column):
        xpath = ".//td[" + str(column) + "]"
        time.sleep(0.5)
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
    #first_user_select_gym = element.FirstUserSelectGym()
    #first_user_name = element.FirstUserName()
    #first_user_email = element.FirstUserEmail()
    #first_user_phone = element.FirstUserPhone()
    #first_user_status = element.FirstUserStatus()
    searchbar_name = element.SearchBarName()
    searchbar_status = element.SearchBarSelectStatus()
    searchbar_gym = element.SearchBarSelectGym()
    #clients_rowgroup = element.RowgroupElement()



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

    def clickRecipesPage(self):
        
        element = self.driver.find_element(*locators.MainPageLocators.GO_TO_RECIPES)
        element.click()    

    def clickWorkoutsPage(self):
        
        element = self.driver.find_element(*locators.MainPageLocators.GO_TO_WORKOUTS)
        element.click()  

    def clickTestimonialsPage(self):
        
        element = self.driver.find_element(*locators.MainPageLocators.GO_TO_TESTIMONIALS)
        element.click()     

class RecipesPage(BasePage):

    add_recipe_title = element.InputRecipeName()
    upload_img_recipe = element.UploadRecipeIMG()
    upload_pdf_recipe = element.UploadRecipePDF()
    #first_recipe_name = element.FirstRecipeName()

    def recipesPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.RecipesPageLocators.ADD_RECIPE_BUTTON))
        return "Recipes" in self.driver.title

    def clickAddRecipe(self):

        element = self.driver.find_element(*locators.RecipesPageLocators.ADD_RECIPE_BUTTON)
        element.click()  

    def clickSubmitRecipe(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.RecipesPageLocators.RECIPE_SUBMIT_BUTTON))
        element = self.driver.find_element(*locators.RecipesPageLocators.RECIPE_SUBMIT_BUTTON)
        element.click() 

    def deleteRecentRecipe(self):

        element = self.driver.find_element(*locators.RecipesPageLocators.RECIPES_FIRST_ROW_DELETE)
        element.click()
        self.driver.find_element(*locators.RecipesPageLocators.RECIPES_CONFIRM_DELETE).click()


class WorkoutProgramsPage(BasePage):

    add_title = element.InputWorkoutTitle()
    add_desc = element.InputWorkoutDescription()
    add_bodyPart = element.InputWorkoutBodyPart()
    add_YTlink = element.InputWorkoutYoutubeLink()
    #first_row_title = element.FirstWorkoutTitle()
    #first_row_desc = element.FirstWorkoutDesc()
    #first_row_yt = element.FirstWorkoutYoutube()
    #first_row_bodypart = element.FirstWorkoutBodyPart()
    searchbar_status = element.SearchbarWorkoutStatus()
    searchbar = element.SearchbarWorkout()
    #workouts_rowgroup =  element.RowgroupElement()

    def workoutProgramsPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.PAGE_HEADER))
        return "Workout programs" in self.driver.title

    def clickAddWorkout(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.ADD_WORKOUT_BUTTON))
        element = self.driver.find_element(*locators.WorkoutProgramsPageLocators.ADD_WORKOUT_BUTTON)
        element.click() 

    def clickSubmit(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.ADD_WORKOUT_SUBMIT))
        element = self.driver.find_element(*locators.WorkoutProgramsPageLocators.ADD_WORKOUT_SUBMIT)
        element.click() 

    def clickFirstPreview(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_PREVIEW_BUTTON))
        element = self.driver.find_element(*locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_PREVIEW_BUTTON)
        element.click() 

    def clickFirstDelete(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_DELETE_BUTTON))
        element = self.driver.find_element(*locators.WorkoutProgramsPageLocators.WORKOUT_FIRST_ROW_DELETE_BUTTON)
        element.click() 

    def clickCancelPreview(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.PREVIEW_CANCEL_BUTTON))
        element = self.driver.find_element(*locators.WorkoutProgramsPageLocators.PREVIEW_CANCEL_BUTTON)
        element.click() 

class TestimonialsPage(BasePage):
    
    input_name = element.CreateTestimonialNameInput()
    input_desc = element.CreateTestimonialDescInput()
    input_file = element.CreateTestimonialFileInplut()
    add_test = element.CreateTestimonialButton()
    test_submit_button = element.CreateTestimonialSubmitButton()
    test_delete_button = element.TestimonialFirstRowDeleteButton()


    def testimonialsPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.TestimonialsPageLocators.PAGE_HEADER))
        return "Testimonials" in self.driver.title


    def deleteFirstTestimonial(self):

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.TestimonialsPageLocators.FIRST_ROW_DELETE_BUTTON))
        element = self.driver.find_element(*locators.TestimonialsPageLocators.FIRST_ROW_DELETE_BUTTON)
        element.click()       


    





