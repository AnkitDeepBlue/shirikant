from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import logging


class reusableMethods:

    def __init__(self, driver):
        self.driver = driver


    def select_by_VisibleText(self, Bylocator, text):
        sel= Select(Bylocator)
        sel.select_by_visible_text(text)

