import selenium
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import authenticate
# import pytest


class MySeleniumTests(StaticLiveServerTestCase):
 #   fixtures = ['user-data.json']

    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/foodfacts/")

    def test_login(self):
        self.driver.get("http://localhost:8000/roles/signin/")
        signin_email = self.driver.find_element_by_name("signin_email")
        signin_email.send_keys('ezzou@gmail.com')
        signin_password = self.driver.find_element_by_name("signin_password")
        signin_password.send_keys('ezzou')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        self.driver.implicitly_wait(10)
