class FirstScreen:

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_next_page(self):
        enter = self.driver.find_element_by_id("enter")
        enter.click()


class SecondScreen:

    def __init__(self, driver):
        self.driver = driver

    def check_checkbox(self):
        elem = self.driver.find_element_by_id("checkbox")
        if not elem.is_selected():
            elem.click()

    def enter_secret_password(self):
        elem = self.driver.find_element_by_name("input")
        pw = self.driver.find_element_by_id("secret_code").get_attribute('value')

        elem.clear()
        elem.send_keys(pw)

    def click_submit(self):
        elem = self.driver.find_element_by_id("submit")
        elem.click()


class ThirdScreen:

    def __init__(self, driver):
        self.driver = driver

    def check_successful_result(self):
        elem = self.driver.find_element_by_id("result")
        assert elem.text == "SUCCESS"
