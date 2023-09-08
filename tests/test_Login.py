from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from conftest import setup_and_teardown


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_valid_credentials(self):
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        self.driver.find_element(By.XPATH,'//input[@id="input-email"]').send_keys("shobhabc9@gmail.com")
        self.driver.find_element(By.XPATH,'//input[@id="input-password"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()

    def test_login_valid_Email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        self.driver.find_element(By.XPATH, '//input[@id="input-email"]').send_keys("shobhabc9@gmail.com")
        self.driver.find_element(By.XPATH, '//input[@id="input-password"]').send_keys("wrg@123")
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        expected_condition = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text.__eq__(expected_condition)

    def test_login_invalid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        self.driver.find_element(By.XPATH, '//input[@id="input-email"]').send_keys("shobhabcbc29@gmail.com")
        self.driver.find_element(By.XPATH, '//input[@id="input-password"]').send_keys("wrg@123")
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        expected_condition = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text.__eq__(expected_condition)

    def test_login_empty_credentials(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        self.driver.find_element(By.XPATH, '//input[@id="input-email"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@id="input-password"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        expected_condition = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text.__eq__(expected_condition)

    def generate_email_with_timestamp(self):
        time_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "shobha"+time_stamp+"@gmail.com"



