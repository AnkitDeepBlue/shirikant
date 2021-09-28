import pytest
import time
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
from selenium import webdriver
from datetime import datetime
import geckodriver_autoinstaller
import allure
from utilities.noteBook import myNotebook


@pytest.fixture(scope="class")
@allure.feature("Sample feature")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url =myNotebook.Base_url
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    time.sleep(5)
    driver.close()

@pytest.fixture()
def takeScreenShot():
    allure.attach(driver.get_screenshot_as_png(), name="Sc_starting", attachment_type= AttachmentType.JPG)
    yield
    allure.attach(driver.get_screenshot_as_png(), name="SC_Ending", attachment_type= AttachmentType.JPG)

# def pytest_addoption(parser):
#     parser.addoption(
#         "-", action="store", default="chrome"
#     )




# @pytest.fixture
# def htmlRepo_screeshot(self):
#     attach(data=self.driver.get_screenshot_as_png())


