class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigateTo(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.page.fill('input[data-test="username"]', username)

    def enter_password(self, password):
        self.page.fill('input[data-test="password"]', password)

    def click_login(self):
        self.page.click('input[data-test="login-button"]')