import pytest
from selenium import webdriver
from utilities import ReadConfigurations
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def setup_and_teardown(request):
    browser=ReadConfigurations.read_configuration("basic info","browser")
    driver=webdriver.Chrome()
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox()
    elif browser .__eq__("edge"):
        driver=webdriver.Edge()
    else:
        print("provide a valid browser name from the list chrome/firefox/edge")
    driver = webdriver.Chrome()
    app_url=ReadConfigurations.read_configuration("basic info","url")
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
