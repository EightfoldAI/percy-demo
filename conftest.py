import pytest
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def driver():
    chrome_options = ChromeOptions()
    # if self.config.getoption('--headless'):
    #     chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)

    yield browser

    try:
        browser.close()
    except:
        print("Browser instance did not close!")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption("--environment", action="store")
    parser.addoption("--domain_name", action="store")
    parser.addoption("--region", action="store")

@pytest.fixture(scope='session')
def parameters(request):
    environment = request.config.option.environment
    domain = request.config.option.domain_name
    region = request.config.option.region
    return [environment, domain, region]