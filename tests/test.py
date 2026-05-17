import pytest
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.usefixtures('test_setup')
class TestLink:

    def test_1(self):
        el1 = self.driver.find_element(AppiumBy.ID, "com.lambdatest.proverbial:id/color")
        el1.click()
        
    def test_2(self):
        el2 = self.driver.find_element(AppiumBy.ID, "com.lambdatest.proverbial:id/color")
        el2.click()
    



