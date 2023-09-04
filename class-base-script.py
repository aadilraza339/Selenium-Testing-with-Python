from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class WebAutomation:

    def __init__(self):

        self.driver =  webdriver.Chrome()

    #Add implicit wait for element to be found

    def apply_wait(self):

        self.driver.implicitly_wait(10)

    # Navigate to Signup Page

    def open_signup_page(self):

        self.driver.get("https://bstackdemo.com/")

        signin_btn = self.driver.find_element(by=By.CSS_SELECTOR,value="#signin")

        signin_btn.click()

    #Select demouser as Username

    def fill_username(self):

      username=self.driver.find_element(by=By.ID,value="username")

      username.click()

      username_input= self.driver.find_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0")

      username_input.click()

    #Select testingisfun99 as Password

    def fill_password(self):

      password =self.driver.find_element(by=By.ID,value="password")

      password.click()

      password_input =self.driver.find_element(by=By.CSS_SELECTOR,value="#react-select-3-option-0-0")

      password_input.click()

   

    # Submit the form

    def submit_form(self):

      login_btn= self.driver.find_element(by=By.ID,value="login-btn")

      login_btn.click()

    #Assert User is successfully Logged In

    def login_success(self):

        logout_btn= self.driver.find_element(by=By.CSS_SELECTOR,value="#logout")

        assert logout_btn.is_displayed()

        self.driver.close()

automation = WebAutomation()

automation.open_signup_page()

automation.apply_wait()

automation.fill_username()

automation.fill_password()

automation.submit_form()

automation.apply_wait()

automation.login_success()