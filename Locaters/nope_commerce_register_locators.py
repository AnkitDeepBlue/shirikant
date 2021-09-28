from selenium import webdriver
from selenium.webdriver.common.by import By

class register:
    def __init__(self, driver):
        self.driver = driver


    #Register locatores

    firstName= (By.XPATH, "//input[@id='FirstName']")
    lastName= (By.XPATH, "//input[@id='LastName']")
    email = (By.XPATH, "//input[@id='Email']")
    confirmEmail = (By.XPATH, "//input[@id='ConfirmEmail']")

    userName = (By.XPATH, "//input[@id='Username']")
    dw_country = (By.XPATH, "//select[@id='CountryId']")
    dw_timeZone = (By.XPATH, "//select[@id='TimeZoneId']")

    checkBox= (By.XPATH, "//label[contains(text(),'I would like to receive newsletters:')]")

    password = (By.XPATH, "//input[@id='Password']")
    confirmPassword = (By.XPATH, "//input[@id='ConfirmPassword']")

    dw_Mycompeny = (By.XPATH, "//select[@id='Details_CompanyIndustryId']")
    dw_mainActivity = (By.XPATH, "//select[@id='Details_CompanyRoleId']")
    dw_pplWork = (By.XPATH, "//select[@id='Details_CompanySizeId']")

    click_Register = (By.XPATH, "//input[@id='register-button']")