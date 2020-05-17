import selenium
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import authenticate
import pytest


driver = webdriver.Chrome()
driver.get("http://localhost:8000/foodfacts/")


class MySeleniumTests(StaticLiveServerTestCase):
 #   fixtures = ['user-data.json']

    @classmethod
    def test_setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome().get("http://localhost:8000/foodfacts/")
        cls.selenium.implicitly_wait(10)

    @classmethod
    def test_tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, 'signin/'))
        signin_email = self.selenium.find_element_by_name("signin_email")
        signin_email.send_keys('dubosc@gmail.com')
        signin_password = self.selenium.find_element_by_name("Franck")
        signin_password.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()
