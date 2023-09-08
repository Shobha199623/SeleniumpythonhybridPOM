from datetime import datetime

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_valid_credentials(self):
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("shobha")
        self.driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("B C")
        self.driver.find_element(By.XPATH,'//input[@name="email"]').send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.XPATH, '//input[@name="telephone"]').send_keys("12345")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@name="confirm"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH,'//input[@type="checkbox"][@name="agree"]').click()
        self.driver.find_element(By.XPATH,'// input[@type="submit"]').click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,'//div[@id="content"]/h1').text.__eq__(expected_text)

    def test_register_with_all_fields(self):
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("shobha")
        self.driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("B C")
        self.driver.find_element(By.XPATH,'//input[@name="email"]').send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.XPATH, '//input[@name="telephone"]').send_keys("12345")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@name="confirm"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="1"]').click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH,'// input[@value ="Continue"]').click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,'//div[@id="content"]/h1').text.__eq__(expected_text)

    def test_Register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("shobha")
        self.driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("B C")
        self.driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("shobhabcbc9@gmail.com")
        self.driver.find_element(By.XPATH, '//input[@name="telephone"]').send_keys("12345")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@name="confirm"]').send_keys("Login@123")
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="1"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="checkbox"][@name="agree"]').click()
        self.driver.find_element(By.XPATH,'// input[@type="submit"]').click()
        expected_warning_message="Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH,'//div[@id="account-register"]/child::div[1]').text.__contains__(expected_warning_message)

    def test_register_without_entering_any_fields(self):
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("")
        self.driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys("")
        self.driver.find_element(By.XPATH,'//input[@name="email"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@name="telephone"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@name="confirm"]').send_keys("")
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="1"]').click()
        self.driver.find_element(By.XPATH,'// input[@type="submit"]').click()
        expected_warning_message="Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH,'//div[@id="account-register"]/div[1]').text.__eq__(expected_warning_message)
        expected_warning_message = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="firstname"]/following-sibling::div[1]').text.__eq__(expected_warning_message)
        expected_warning_message = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="lastname"]/following-sibling::div[1]').text.__eq__(expected_warning_message)
        expected_warning_message = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, '//input[@placeholder="E-Mail"]/following-sibling::div[1]').text.__eq__(expected_warning_message)
        expected_warning_message = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@placeholder="Telephone"]/following-sibling::div[1]').text.__eq__(expected_warning_message)
        expected_warning_message = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]/following-sibling::div[1]').text.__eq__(expected_warning_message)

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "shobha" + time_stamp + "@gmail.com"