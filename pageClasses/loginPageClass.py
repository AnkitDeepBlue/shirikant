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
from SuperClasses.Logs import loggingClass
from SuperClasses.Reusable_methods import reusableMethods

logger = loggingClass.logGen()


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    def access_url(self):

        self.driver.get("https://www.saucedemo.com/")

    def enter_userName(self, username):
        logger.info("Entering user name as >>"+ username)
        self.driver.find_element(*addToCart.username).send_keys(username)

    def enter_password(self, password):
        logger.info("Entering password as >>"+ password)
        self.driver.find_element(*addToCart.password).send_keys(password)

    def clickLogin(self):
        logger.info("Clicking login button")
        self.driver.find_element(*addToCart.loginbtn).click()

    def verifyTittle(self, title):
        logger.info("Verifing title with " + title)
        gettitle=self.driver.title

        if gettitle != title:
            logger.info("Title not matched")
            assert False
        else:
            logger.info("Title matched")

    def clickLogout(self):
        logger.info("Clicking Menu button >> clicking logout")
        time.sleep(2)
        self.driver.find_element(*addToCart.menu).click()
        self.driver.find_element(*addToCart.logout).click()

    def accessLog(self, text):
        with open('C:/Users/ovonel/PycharmProjects/pythonProject9/testCaces/GenratedFile.log', 'r') as reader:
            for line in reader:
                if text in line:
                    print("text found in log file")
                    break
                else:
                    print("Text not found in log file")