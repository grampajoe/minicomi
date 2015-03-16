import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def _get_driver():
    """Returns a Sauce Labs driver if available, otherwise Firefox."""
    username = os.environ.get('SAUCE_LABS_USERNAME')
    key = os.environ.get('SAUCE_LABS_KEY')

    if username and key:
        url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'
        driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor=url % (username, key),
        )
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(3)

    return driver


def before_all(context):
    def get_browser():
        """Only create a Selenium driver if we need it."""
        try:
            browser = context.browser
        except AttributeError:
            browser = context.browser = _get_driver()
        return browser

    context.base_url = os.environ.get(
        'MINICOMI_BASE_URL',
        'http://localhost:5000',
    )
    context.get_browser = get_browser


def after_scenario(context, scenario):
    try:
        context.browser.quit()
        del context.browser
    except AttributeError:
        pass
