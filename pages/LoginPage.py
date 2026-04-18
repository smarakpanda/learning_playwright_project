from utils.decorators.LoggingDecorator import log_decorator


class LoginPage:
    def __init__(self, page):
        self.page = page

    @log_decorator
    def get_username(self):
        # username = self.page.get_by_test_id("username")
        username =  self.page.locator("[data-test='username']")
        username.highlight()
        return username

    @log_decorator
    def get_password(self):
        return self.page.get_by_test_id("password")

    @log_decorator
    def get_login_button(self):
        return self.page.get_by_test_id("login-button")

    @log_decorator
    def enter_username(self, username):
        username_field = self.page.locator("[data-test='username']")
        username_field.fill(username)

    @log_decorator
    def enter_password(self, password):
        password_field = self.page.locator("[data-test='password']")
        password_field.fill(password)

    @log_decorator
    def click_login_button(self):
        login_button = self.page.locator("[data-test='login-button']")
        login_button.click()

    @log_decorator
    def wait_for_shopping_cart(self):
        self.page.locator("[data-test='shopping-cart']").wait_for(state="visible")

    @log_decorator
    def perform_login(self, username, password):
        # self.get_username()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @log_decorator
    def get_menu_button(self):
        return self.page.locator("[data-test='open-menu']")
