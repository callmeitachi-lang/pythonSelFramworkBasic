import pytest

from TestData.testdatautil import Testdatautil
from pageobjects.Registration import Registration
from utily.BaseClass import BaseClass


class TestReg(BaseClass):

    def test_reg(self, getdata):

        log = self.getlogger()
        registration = Registration(self.driver)
        log.info("firstname added in test "+getdata["firstname"])
        registration.set_name().send_keys(getdata["firstname"])
        log.info("email id added in the test "+getdata["email"])
        registration.set_email().send_keys(getdata["email"])
        log.info("password added :"+getdata["password"])
        registration.set_password().send_keys(getdata["password"])
        registration.click_checkbox().click()
        registration.submit_button()

    @pytest.fixture(params=Testdatautil.getTestData("testcase1"))
    def getdata(self, request):
        return request.param


   # @pytest.fixture(params=[{"firstname": "kanwar", "email": "xyz@gmail.com", "password": "Kanwar@77"}])







