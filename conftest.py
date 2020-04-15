import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Parameterization of the test by the browser
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: opera, chrome or firefox")
    # Parameterization of the test by the language
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ru, en, es, fr etc.")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        # Setup parameters for Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        # Launch Chrome
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # Setup parameters for FireFox
        binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        print("\nstart firefox browser for test..")
        # Launch FireFox
        browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    else:
        raise pytest.UsageError(f"--your browser {browser_name} with language {language} still not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()
