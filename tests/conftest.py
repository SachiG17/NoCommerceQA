import pytest
import time
from selenium import webdriver
from utilities.readProperties import ReadConfig
driver = None
url=ReadConfig.getUrl()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
# This will help for cross browser for specifying the browser namer in which we need to open

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox")
    elif  browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer")
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)






