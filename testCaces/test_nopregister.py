import time

import pytest

from SuperClasses.baseClass import baseclass
from SuperClasses.xls import myexel
from pageClasses.nopRegisterPageClass import doRegister
from utilities.noteBook import myNotebook


class TestLogin(baseclass):

    def test_doRegister(self):
        doRegister.access_url(self)
        doRegister.enter_firstName(self, myNotebook.firstname)
        doRegister.enter_lasttName(self, myNotebook.lastName)
        doRegister.enter_email(self, myNotebook.email)
        doRegister.enter_confirmEmail(self, myNotebook.email)
        doRegister.enter_username(self, myNotebook.username)

        doRegister.select_Country(self, myNotebook.country)
        doRegister.select_TimeZone(self, myNotebook.timeZone)
        doRegister.verifyCheckBoxSelection(self)
        doRegister.delecting_checkBox(self)

        doRegister.enterPassword(self, myNotebook.password)
        doRegister.enterConfirmPassword(self, myNotebook.password)
        doRegister.select_Mycompany(self, myNotebook.companyDetails)
        doRegister.select_Activity(self, myNotebook.activity)
        doRegister.select_pplWork(self, myNotebook.pplAtWork)
        doRegister.clickRegister(self)

        time.sleep(10)