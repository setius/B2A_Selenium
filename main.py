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
        '''Welcome page'''
        welcome_page = page.WelcomePage(self.driver)
        assert welcome_page.welcomePageCheck(), "Welcome page text did not match"
        welcome_page.clickGoToApp()
        '''Login Page'''
        login_page = page.LoginPage(self.driver)
        assert login_page.loginPageCheck(), "Login page text did not match"
        login_page.email_text_element = credentials.USER
        login_page.pass_text_element = credentials.PASS 
        login_page.clickLogin()


    def tearDown(self):
        self.driver.close()

    def test1_AddUser(self):
        '''This test case verifies functionality of adding new user
            and also checks if user attributes are set properly
            Disabled because we cannot delete users in GUI'''
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        user = 'Carl Johnson'
        email = 'cj_grooveStreetFL@gmail.com'
        phone = '445676777'
        gym = 'Frankfield'
        calories = '2300'
        '''
        main_page.clickAddClient()
        main_page.clickActive()
        main_page.add_user_name = user
        main_page.add_user_email = email
        main_page.add_user_phone = phone
        main_page.add_user_gym = gym
        main_page.add_user_calories = calories
        main_page.clickSubmit()
        '''
        assert user in main_page.first_user_name.text, "User Name was not set properly"
        assert email.upper() in main_page.first_user_email.text.upper(), "User Email was not set properly"
        assert phone in main_page.first_user_phone.text, "User Phone was not set properly"
        assert gym in main_page.first_user_select_gym.text, "User Gym was not set properly"
        assert "Active" in main_page.first_user_status.text, "User status was not set properly"

        time.sleep(2)

        

    def test2_ClientsSearchBarVerification(self):
        user = 'Carl Johnson'
        email = 'cj_grooveStreetFL@gmail.com'
        active_status = 'Active'
        inactive_status = 'Inactive'
        gym = 'Frankfield'
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.searchbar_name = user
        assert main_page.first_user_name.text in user, "User did not match with searched user"
        assert main_page.first_user_email.text.upper() in email.upper(), "Email did not match with searched user"
        assert main_page.first_user_status.text in active_status, "Email did not match with searched user"
        main_page.clickSearchBarClear()
        main_page.searchbar_status = inactive_status
        active_column = main_page.get_column_data(main_page.clients_rowgroup, 8)
        assert all(element==inactive_status for element in active_column), "Search did not filter status properly"
        main_page.clickSearchBarClear()
        main_page.searchbar_gym = gym
        gym_column = main_page.get_column_data(main_page.clients_rowgroup, 5)
        assert all(element==gym for element in gym_column), "Search did not filter gym properly"

    def test3_checkRecipesPage(self):

        RECIPE_NAME = "Chocolate brownie with peanutbutter"
        RECIPE_IMG_PATH = r"C:\Users\jania\Desktop\Repositories\B2A_Selenium\brownie.PNG"
        RECIPE_PDF_PATH = r"C:\Users\jania\Desktop\Repositories\B2A_Selenium\recipe.pdf"
        main_page = page.MainPage(self.driver)
        assert main_page.mainPageCheck(), "Main Page title did not match"
        main_page.clickRecipesPage()
        recipes_page = page.RecipesPage(self.driver)
        assert recipes_page.recipesPageCheck(), "Recipes page title did not match"
        recipes_page.clickAddRecipe()
        recipes_page.add_recipe_title = RECIPE_NAME
        recipes_page.upload_img_recipe = RECIPE_IMG_PATH
        recipes_page.upload_pdf_recipe = RECIPE_PDF_PATH
        recipes_page.clickSubmitRecipe()
        time.sleep(1)
        assert recipes_page.first_recipe_name.text in RECIPE_NAME, "Recipe was not created properly"
        recipes_page.deleteRecentRecipe()
        time.sleep(1)
        assert recipes_page.first_recipe_name.text not in RECIPE_NAME, "Recipe was not deleted properly after test"
        


if __name__ == "__main__":
    unittest.main()
