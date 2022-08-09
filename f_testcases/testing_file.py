import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("/home/zorro/pythoreborn/facebook_login/")
from f_baseclass.login_details import Facebooklogin


class TestingLogin(unittest.TestCase):
    email = "9951425962"
    password = "Mbappe@1"
    url = "https://www.facebook.com/"
    driver = webdriver.Firefox(executable_path="/home/zorro/Downloads/geckodriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)

    def testing_login(self):
        lp = Facebooklogin(self.driver)
        lp.username(self.email)
        lp.password(self.password)
        lp.login_button()
        self.assertEqual("Facebook", self.driver.title, "not the same match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/zorro/pythoreborn/facebook_login/f_reports"))
