from os import environ
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from requests import request

@pytest.fixture(scope='function')
def test_setup(request):
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    
    options = UiAutomator2Options()
    options.set_capability("deviceName", "Galaxy S21 Ultra 5G")
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "11")
    options.set_capability("app", "lt://APP10160301691747362768822447")
    options.set_capability("isRealMobile", True)
    options.set_capability("build", build)
    options.set_capability("name", test_name)
    
    driver = webdriver.Remote("https://<Username>:<AccessKey>@mobile-hub.lambdatest.com/wd/hub", options=options)
    request.cls.driver = driver
    
    yield driver
    
    def fin():
        #browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else "failed").lower()))
        if request.node.rep_call.failed:
            driver.execute_script("lambda-status=failed")
        else:
            driver.execute_script("lambda-status=passed")
            driver.quit()
    request.addfinalizer(fin)
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

