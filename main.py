import unittest
from selenium import webdriver
import page
import credentials
import time

class B2ATests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(credentials.WEBSITE)
        welcome_page = page.WelcomePage(self.driver)
        assert welcome_page.welcomePageCheck(), "Welcome page text did not match"
        welcome_page.clickGoToApp()
        login_page = page.LoginPage(self.driver)
        assert login_page.loginPageCheck(), "Login page text did not match"
        login_page.email_text_element = credentials.USER
        login_page.pass_text_element = credentials.PASS 
        login_page.clickLogin()


    def tearDown(self):
        self.driver.close()

    def dis_test1_AddUser(self):

        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        USER = 'Carl Johnson'
        EMAIL = 'cj_grooveStreetFL@gmail.com'
        PHONE = '445676777'
        GYM = 'Frankfield'
        CALORIES = '2300'
        '''
        main_page.add_client_button.click()
        main_page.active_button.click()
        main_page.add_user_name = user
        main_page.add_user_email = email
        main_page.add_user_phone = phone
        main_page.add_user_gym = gym
        main_page.add_user_calories = calories
        main_page.submit_button.click()
        '''
        assert USER in main_page.get_column_data(main_page.rowgroup, 2)[0], "User Name was not set properly"
        assert EMAIL.upper() in main_page.get_column_data(main_page.rowgroup, 3)[0].upper(), "User Email was not set properly"
        assert PHONE in main_page.get_column_data(main_page.rowgroup, 4)[0], "User Phone was not set properly"
        assert GYM in main_page.get_column_data(main_page.rowgroup, 5)[0], "User Gym was not set properly"
        assert "Active" in main_page.get_column_data(main_page.rowgroup, 8)[0], "User status was not set properly"

        
    def dis_test2_ClientsSearchBarVerification(self):

        USER = 'Carl Johnson'
        EMAIL = 'cj_grooveStreetFL@gmail.com'
        ACTIVE_STATUS = 'Active'
        INACTIVE_STATUS = 'Inactive'
        GYM = 'Frankfield'
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.searchbar_name = USER
        assert USER in main_page.get_column_data(main_page.rowgroup, 2)[0], "User did not match with searched user"
        assert EMAIL.upper() in main_page.get_column_data(main_page.rowgroup, 3)[0].upper(), "Email did not match with searched user"
        assert ACTIVE_STATUS in main_page.get_column_data(main_page.rowgroup, 8)[0], "Email did not match with searched user"
        main_page.clear_searchbar_button.click()
        main_page.searchbar_status = INACTIVE_STATUS
        active_column = main_page.get_column_data(main_page.rowgroup, 8)
        assert all(element==INACTIVE_STATUS for element in active_column), "Search did not filter status properly"
        main_page.clear_searchbar_button.click()
        main_page.searchbar_gym = GYM
        gym_column = main_page.get_column_data(main_page.rowgroup, 5)
        assert all(element==GYM for element in gym_column), "Search did not filter gym properly"

    def dis_test3_checkRecipesPage(self):

        RECIPE_NAME = "Chocolate brownie with peanutbutter"
        RECIPE_IMG_PATH = r"C:\Users\jania\Desktop\Repositories\B2A_Selenium\brownie.PNG"
        RECIPE_PDF_PATH = r"C:\Users\jania\Desktop\Repositories\B2A_Selenium\recipe.pdf"
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.panel_goto_recipes_button.click()
        recipes_page = page.RecipesPage(self.driver)
        assert recipes_page.recipesPageCheck(), "Recipes page title did not match"
        recipes_page.add_recipe_button.click()
        recipes_page.add_recipe_title = RECIPE_NAME
        recipes_page.upload_img_recipe = RECIPE_IMG_PATH
        recipes_page.upload_pdf_recipe = RECIPE_PDF_PATH
        recipes_page.submit_recipe_button.click()
        assert RECIPE_NAME in recipes_page.get_column_data(recipes_page.rowgroup, 2)[0], "Recipe was not created properly"
        recipes_page.delete_first_recipe_button.click()
        recipes_page.delete_first_recipe_confirm_button.click()
        assert RECIPE_NAME not in recipes_page.get_column_data(recipes_page.rowgroup, 2)[0], "Recipe was not deleted properly after test"

    def dis_test4_workoutProgramsCheck(self):

        WORKOUT_TITLE = 'Chest workout'
        WORKOUT_DESC = 'Basic chest workout for beginners. Mostly push-ups'
        WORKOUT_YT = "https://youtube.com/watch?v=jWc8gHlAkoM"
        WORKOUT_BODYPART = 'Chest'
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.panel_goto_workouts_button.click()
        workouts_page = page.WorkoutProgramsPage(self.driver)
        assert workouts_page.workoutProgramsPageCheck(), "Workouts Page title did not match"
        workouts_page.add_workout_button.click()
        workouts_page.add_YTlink = WORKOUT_YT
        workouts_page.add_title = WORKOUT_TITLE
        workouts_page.add_desc = WORKOUT_DESC
        workouts_page.add_bodyPart = WORKOUT_BODYPART
        workouts_page.add_workout_submit_button.click()
        assert WORKOUT_BODYPART in workouts_page.get_column_data(workouts_page.rowgroup, 2)[0], "Bodypart for created workout not set correctly"
        assert WORKOUT_TITLE in workouts_page.get_column_data(workouts_page.rowgroup, 5)[0], "Title of created workout not set correctly"
        assert WORKOUT_DESC in workouts_page.get_column_data(workouts_page.rowgroup, 4)[0], "Description of created workout not set correctly"
        assert WORKOUT_YT in workouts_page.get_column_data(workouts_page.rowgroup, 7)[0] , "Youtube link of created workout was not set correctly"
        workouts_page.preview_button.click()
        time.sleep(1)
        workouts_page.preview_cancel_button.click()
        workouts_page.delete_first_workout_button.click()
        workouts_page.searchbar_status = "Published"
        status_column = workouts_page.get_column_data(workouts_page.rowgroup, 6)
        assert all(element=="Published" for element in status_column), "Search did not filter status properly"
        workouts_page.searchbar_status = "All"
        workouts_page.searchbar = "Shoulders"
        bodypart_column = workouts_page.get_column_data(workouts_page.rowgroup, 2)
        assert all(element=="Shoulders" for element in bodypart_column), "Search did not filter body parts properly"

    def test5_testimonialsPage(self):
        
        NAME = "Johnny Bravo"
        DESC = "Johnny Bravo tranformation"
        FILE_PATH = r"C:\Users\jania\Desktop\Repositories\B2A_Selenium\johnny.PNG"
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.panel_goto_testimonials_button.click()
        test_page = page.TestimonialsPage(self.driver)
        assert test_page.testimonialsPageCheck(), "Testimonials page did not match"
        test_page.add_test.click()
        test_page.input_name = NAME
        test_page.input_desc = DESC
        test_page.input_file = FILE_PATH
        test_page.test_submit_button.click()
        assert NAME in test_page.get_column_data(test_page.rowgroup, 2)[0], "User testimonial was not created properly"
        assert DESC in test_page.get_column_data(test_page.rowgroup, 3)[0], "User description was not set properly"
        test_page.test_delete_button.click()
        assert NAME not in test_page.get_column_data(test_page.rowgroup, 2)[0], "User testimonial was not deleted properly"       



if __name__ == "__main__":
    unittest.main()
