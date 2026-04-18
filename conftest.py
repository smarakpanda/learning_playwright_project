import pytest
from playwright.sync_api import sync_playwright
from browserFactory import launch_browser
from utils.configReader import ConfigReader
from utils.decorators.LoggingDecorator import log_decorator

config = ConfigReader()

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    print("Browser fixture started")
    browser_name = config.get_value_from_config("browser")
    headless = config.get_value_from_config("headless").lower() == "true"
    browser = launch_browser(playwright, browser_name, headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, request):
    print("Context fixture started")
    context = browser.new_context(
        record_video_dir="videos/",
        viewport={"width": 1920, "height": 1080}
    )
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
    context.close()

@pytest.fixture(scope="function")
def my_page(context):
    print("Page fixture started")
    page = context.new_page()
    url = config.get_value_from_config("prod_url")
    print("Launching URL:", url)
    page.goto(url)
    yield page
    page.close()