import unittest
from selenium import webdriver

import PageObjects


class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://alteryx-automation.herokuapp.com/")

    def happy_case_scenario(self):
        first_page = PageObjects.FirstScreen
        second_page = PageObjects.SecondScreen
        third_page = PageObjects.ThirdScreen

        first_page.proceed_to_next_page(self)
        second_page.check_checkbox(self)
        second_page.enter_secret_password(self)
        second_page.click_submit(self)
        third_page.check_successful_result(self)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
