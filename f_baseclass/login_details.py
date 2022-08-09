class Facebooklogin:
    email_id_address = "//input[@name='email']"
    password_id_address = "//input[@type='password']"
    login_button_address = "//button[@name='login']"

    def __init__(self, webdriver):
        self.driver = webdriver

    def username(self, username):
        self.driver.find_element_by_xpath(self.email_id_address).send_keys(username)

    def password(self,password):
        self.driver.find_element_by_xpath(self.password_id_address).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_xpath(self.login_button_address).click()

