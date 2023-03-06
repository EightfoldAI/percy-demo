import pytest
from percy.snapshot import percy_snapshot
from common.constants.global_constants import Constants
from common.pcs.pcs_locators import CareerPageLocators


@pytest.mark.usefixtures('driver', 'parameters')
class TestLink:

    def getting_url(self, parameters):
        return Constants.URL_DICT["PCS_CAREER_URL"].replace("environment", parameters[0]).replace("domain_name", parameters[
            1]).replace(
            "-region", parameters[2])

    def test_career_main_page(self, driver, parameters):
        url = self.getting_url(parameters)
        driver.get(url)
        driver.implicitly_wait(10)
        percy_snapshot(driver, 'PCS Career Main Page')

    def test_career_home_page(self, driver, parameters):
        url = self.getting_url(parameters)
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(*CareerPageLocators.SKIP).click()
        driver.implicitly_wait(10)
        percy_snapshot(driver, 'PCS Career Home Page')






