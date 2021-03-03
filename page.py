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
    searchbar_name = element.SearchBarName()
    searchbar_status = element.SearchBarSelectStatus()
    searchbar_gym = element.SearchBarSelectGym()
    add_client_button = element.AddClientButton()
    submit_button = element.AddClientSubmitButton()
    active_button = element.AddClientActiveButton()
    clear_searchbar_button = element.ClearSearchBarButton()
    panel_goto_recipes_button = element.GoToRecipesButton()
    panel_goto_workouts_button = element.GoToWorkoutsButton()
    panel_goto_testimonials_button = element.GoToTestimonialsButton()


    def mainPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.MainPageLocators.ADD_CLIENT_BUTTON))
        return "Clients" in self.driver.title
         

class RecipesPage(BasePage):

    add_recipe_title = element.InputRecipeName()
    upload_img_recipe = element.UploadRecipeIMG()
    upload_pdf_recipe = element.UploadRecipePDF()
    add_recipe_button = element.AddRecipeButton()
    submit_recipe_button = element.SubmitRecipeButton()
    delete_first_recipe_button = element.DeleteFirstRecipeButton()
    delete_first_recipe_confirm_button = element.DeleteFirstRecipeConfirmButton()

    def recipesPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.RecipesPageLocators.ADD_RECIPE_BUTTON))
        return "Recipes" in self.driver.title


class WorkoutProgramsPage(BasePage):

    add_title = element.InputWorkoutTitle()
    add_desc = element.InputWorkoutDescription()
    add_bodyPart = element.InputWorkoutBodyPart()
    add_YTlink = element.InputWorkoutYoutubeLink()
    searchbar_status = element.SearchbarWorkoutStatus()
    searchbar = element.SearchbarWorkout()
    add_workout_button = element.AddWorkoutButton()
    add_workout_submit_button = element.AddWorkoutSubmitButton()
    preview_button = element.FirstWorkoutPreviewButton()
    delete_first_workout_button = element.DeleteFirstWorkoutButton()
    preview_cancel_button = element.CancelPreviewButton()

    def workoutProgramsPageCheck(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locators.WorkoutProgramsPageLocators.PAGE_HEADER))
        return "Workout programs" in self.driver.title



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
   


    





