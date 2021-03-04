# B2A_Selenium

Project contains five selenium test cases which verify functionalities of B2A site. The site is used to manage clients, scheduling, workouts for B2A gym administrators and members.

![site](https://user-images.githubusercontent.com/23122115/109948674-d862cb00-7cda-11eb-83fe-be78c606d574.PNG)

### SetUp procedure executed before each test case:
1. Open welcome page and check if loaded properly.
2. Go to login page and check if loaded properly.
3. Login with user/pass and go to main page

### TestCase#1 Verification of newly created user
Steps:
1. Check if main page is loaded correctly
2. Create new user with attributes: Username, Gym, Phone, Email, Status, Calories
3. Check if newly created user has all attributes set correctly

### TestCase#2 Verification of searchbar on main page
Steps:
1. Check if main page is loaded correctly
2. Set "User" in searchbar
3. Check if User list was filtered properly according to search
4. Clear searchbar fields
5. Set "Inactive" in searchbar "Status" Field
6. Check if Users list consist only of users with "Inactive" status
7. Clear searchbar fields
8. Set "Frankfield" in searchbar "Gym" Field
9. Check if Users list consist only of users from "Frankfield" gym

### TestCase#3 Verification of Recipes page
Steps:
1. Check if main page is loaded correctly
2. Go to "Recipes" page and check if loaded correctly
3. Create new recipe with name, image file and pdf file
4. Check if Recipe was created properly with all attributes
5. Delete newly created recipe and check if was deleted

### TestCase#4 Verification of Workout Programs page
Steps:
1. Check if main page is loaded correctly
2. Go to "Workout Programs" page and check if loaded correctly
3. Create new workout program with attributes: Title, Description, Body Part, Youtube link
4. Check if Workout Program was created properly with all attributes
5. Check if Youtube clip can be previewed
6. Set searchbar "Status" field to "Published"
7. Check if filtered workout programs consists of only "Published" workouts
8. Change searchbar status field to "All"
9. Set searchbar "Body Part" field to "Shoulders"
10. Check if filtered workout programs consists of only "Shoulders" workouts

### TestCase#5 Verification of Testimonials Page
Steps:
1. Check if main page is loaded correctly
2. Go to "Testimonials" page and check if loaded correctly
3. Create new Testimonial with attributes: Name, Description, Image file
4. Check if testimonial was created properly with all attributes
5. Delete newly created testimonial
6. Check if was deleted properly
