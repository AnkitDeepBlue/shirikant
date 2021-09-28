import time

from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from Locaters.login import *
from Locaters.nope_commerce_register_locators import register
from SuperClasses.Logs import loggingClass
from SuperClasses.Reusable_methods import reusableMethods

logger = loggingClass.logGen()


class doRegister:
    def __init__(self, driver):
        self.driver = driver

    def access_url(self):
        logger.info("Opening the Registration Page")
        self.driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen%2Fget-started")

    def enter_firstName(self, firstName):
        logger.info("Entering first name >> "+ firstName)
        self.driver.find_element(*register.firstName).send_keys(firstName)

    def enter_lasttName(self, lasttName):
        logger.info("Entering last name >> " + lasttName)
        self.driver.find_element(*register.lastName).send_keys(lasttName)

    def enter_email(self, email):
        logger.info("Entering email >> " + email)
        self.driver.find_element(*register.email).send_keys(email)

    def enter_confirmEmail(self, email):
        logger.info("Entering Confirm email >> " + email)
        self.driver.find_element(*register.confirmEmail).send_keys(email)

    def enter_username(self, username):
        logger.info("Entering username >> " + username)
        self.driver.find_element(*register.userName).send_keys(username)

    def select_Country(self, text):
        logger.info("Selecting 'Cointry' from the dropdown >> " + text)
        reusableMethods.select_by_VisibleText(self, self.driver.find_element(*register.dw_country), text)

    def select_TimeZone(self, text):
        logger.info("Selecting 'TimeZone' from the dropdown >> " + text)
        reusableMethods.select_by_VisibleText(self, self.driver.find_element(*register.dw_timeZone), text)

    def verifyCheckBoxSelection(self):
        if self.driver.find_element(*register.checkBox).is_selected() == True:
            logger.info("News-CheckBox is selected")

        else:
            logger.info("News - CheckBox is selected")
            assert True

    def delecting_checkBox(self):
        logger.info("News check box desleting")
        self.driver.find_element(*register.checkBox).click()

        if self.driver.find_element(*register.checkBox).is_selected() == False:
            logger.info("check box deslected successfuly")

        else:
            logger.info("unable to deselect the checkbox")

    def enterPassword(self, text):
        logger.info("Entering password >> " )
        self.driver.find_element(*register.password).send_keys(text)

    def enterConfirmPassword(self, text):
        logger.info("Entering confirm password >>")
        self.driver.find_element(*register.confirmPassword).send_keys(text)

    def select_Mycompany(self, text):
        logger.info("Selecting company details >> " + text)
        reusableMethods.select_by_VisibleText(self, self.driver.find_element(*register.dw_Mycompeny), text)

    def select_Activity(self, text):
        logger.info("Selecting main activity details >> " + text)
        reusableMethods.select_by_VisibleText(self, self.driver.find_element(*register.dw_mainActivity), text)

    def select_pplWork(self, text):
        logger.info("Selecting how many ppl work >> " + text)
        reusableMethods.select_by_VisibleText(self, self.driver.find_element(*register.dw_pplWork), text)

    def clickRegister(self):
        logger.info("Clicking register button")
        self.driver.find_element(*register.click_Register).click()




