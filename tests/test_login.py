from pages.LoginPage import LoginPage
from utils.configReader import ConfigReader

config = ConfigReader()

print(f"config sections {config.config.sections()}")
print(f"config sections {config.config.items()}")

username = config.get_value_from_config("username")
password = config.get_value_from_config("password")


def test_login_functionality(my_page):
    print(f"Page Title: {my_page.title()}")
    login_page = LoginPage(my_page)
    print(f"UserName : {username}, Password: {password}")
    login_page.perform_login(username, password)
    print(f"Page title : {my_page.title()}")
    my_page.wait_for_load_state("load")
    login_page.get_menu_button().wait_for(state="visible")
    assert login_page.get_menu_button().is_visible()


def test_incorrect_login_test(my_page):
    print(f"Page Title: {my_page.title()}")
    login_page = LoginPage(my_page)
    login_page.perform_login("locked_out_user", password)






