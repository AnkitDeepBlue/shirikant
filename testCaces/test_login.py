import pytest

from SuperClasses.baseClass import baseclass
from SuperClasses.xls import myexel
from pageClasses.loginPageClass import *


class TestLogin(baseclass):
    @pytest.mark.parametrize("userid, password",[("standard_user","secret_sauce"),("standard_user","secret_sauce")])
    def test_loginFun(self, userid, password):
        loginPage.access_url(self)
        loginPage.enter_userName(self, userid)
        loginPage.enter_password(self, password)
        loginPage.clickLogin(self)
        loginPage.clickLogout(self)
        loginPage.verifyTittle(self, "Swag Labs")

    @pytest.mark.skip
    def test_loginFromXLS(self):
        path = "D:\Pycharm\Myexcel\details.xlsx"
        max_row = myexel.maxrow(self, path, "Sheet1")
        max_col = myexel.maxcol(self, path, "Sheet1")
        for r in range(2, max_row + 1):
            for c in range(2, max_col + 1):
                data_u = myexel.getCellValue(self, path, r, 1)
                data_p = myexel.getCellValue(self, path, c, 2)
                loginPage.enter_userName(self, data_u)
                loginPage.enter_password(self, data_p)
                loginPage.clickLogin(self)
                loginPage.clickLogout(self)
                loginPage.verifyTittle(self, "Swag Labs")

    @pytest.mark.skip
    def test_printFormData(self):
        path = "D:\Pycharm\Myexcel\details_new.xlsx"
        max_row = myexel.maxrow(self, path, "Sheet1")
        max_col = myexel.maxcol(self, path, "Sheet1")
        for r in range(2, max_row + 1):
            for c in range(2, max_col + 1):
                data_u = myexel.getCellValue(self, path, r, 1)
                data_p = myexel.getCellValue(self, path, r, 2)
                data_p2 = myexel.getCellValue(self, path, r, 3)
                print(data_u, data_p, data_p2)

    def test_verifyLog(self):
        loginPage.accessLog(self, "Title")

