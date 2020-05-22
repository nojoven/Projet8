from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MySeleniumTests(StaticLiveServerTestCase):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(24000)

    def test_browser(self):
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/foodfacts/")
        self.assertIn("GRAS", self.driver.find_element_by_id("main_title").text)
        self.driver.get("http://localhost:8000/roles/signin/")

        signin_email = self.driver.find_element_by_name("signin_email")
        signin_email.send_keys('pujadas@gmail.com')
        signin_password = self.driver.find_element_by_name("signin_password")
        signin_password.send_keys('pujadas')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()

        search_navbar_input = self.driver.find_element_by_name("nav_search")
        search_navbar_input.send_keys("Coleslaw")
        search_navbar_input.send_keys(u'\ue007')

        self.driver.find_element_by_id(f"details{1}").click()
        self.driver.find_element_by_name("offacts_link").click()
        self. driver.execute_script("window.history.go(-2)")

        self.driver.find_elements_by_class_name('add_to_fav')[0].submit()

        self.driver.get("http://localhost:8000/roles/favourites")
        self.driver.find_elements_by_class_name('unlike_form')[0].submit()
        self.driver.execute_script("window.history.go(-2)")

        self.driver.refresh()
        self.driver.get("http://localhost:8000/roles/signin/")
        #submit
        self.driver.find_elements_by_class_name('logout_form')[0].submit()




"""
    def test_register(self):
        self.driver.get("http://localhost:8000/foodfacts/")
        self.assertIn("GRAS", self.driver.find_element_by_id("main_title").text)
        self.driver.get("http://localhost:8000/roles/signin/")
        self.driver.find_element_by_name("register_link").click()
        signup_first_name = self.driver.find_element_by_name("Prenom")
        signup_first_name.send_keys('David')
        signup_last_name = self.driver.find_element_by_name("Nom")
        signup_last_name.send_keys('Pujadas')
        signup_password = self.driver.find_element_by_name("Mot_De_Passe")
        signup_password.send_keys('pujadas')
        signup_confirm_pwd = self.driver.find_element_by_name("Repeter_Mot_De_Passe")
        signup_confirm_pwd.send_keys('pujadas')
        signup_email = self.driver.find_element_by_name("Mail")
        signup_email.send_keys('pujadas@gmail.com')
        signup_telephone = self.driver.find_element_by_name("Telephone")
        signup_telephone.send_keys("0602030405")
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        self.driver.implicitly_wait(15)

    def test_update(self):
        update_first_name = self.driver.find_element_by_name("update_first_name")
        update_first_name.send_keys('Jules')
        update_last_name = self.driver.find_element_by_name("update_last_name")
        update_last_name.send_keys('Julien')
        update_email = self.driver.find_element_by_name("update_email")
        update_email.send_keys('rugby@gmail.com')
        confirm_email = self.driver.find_element_by_name("confirm_email")
        confirm_email.send_keys('pujadas@gmail.com')
        confirm_password = self.driver.find_element_by_name("confirm_password")
        confirm_password.send_keys('pujadas')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        self.driver.implicitly_wait(15)
"""