import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.XPATH,"// button[contains( @class ,'btn btn-default btn-lg')]").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.XPATH,"//input[(@placeholder='Search' and contains(@class, 'input-lg')) or @name='search']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "// button[contains( @class ,'btn btn-default btn-lg')]").click()
        expected_text="Products meeting the search criteria"
        assert self.driver.find_element(By.XPATH,"//h2 [text()='Products meeting the search criteria']").text.__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        self.driver.find_element(By.XPATH,'//input[@placeholder="Search"]').click()
        self.driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys("")
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-lg"]').click()
        expected_text="Products meeting the search criteria"
        assert self.driver.find_element(By.XPATH,"//h2 [text()='Products meeting the search criteria']").text.__eq__(expected_text)
