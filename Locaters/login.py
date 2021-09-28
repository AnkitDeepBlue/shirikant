from selenium import webdriver
from selenium.webdriver.common.by import By

class addToCart:
    def __init__(self, driver):
        self.driver = driver

    # Login Locators
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    loginbtn = (By.XPATH, "//input[@id='login-button']")
    menu = (By.XPATH, "//button[contains(text(),'Open Menu')]")
    logout = (By.XPATH, "//a[@id='logout_sidebar_link']"
              )