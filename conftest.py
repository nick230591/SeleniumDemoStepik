import pytest
from selenium import webdriver

# путь до log файла, который создает Firefox 
GECKO_LOG_PATH_FIREFOX = 'test_demo/geckodriver.log'

# 
def pytest_addoption(parser):
    """
    Добавляем дополнительные параметры из командной строки
    parser - вcтроенная fixture
    """
    # возможность выбора браузера (Chrome, Firefox)
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # возможность выбора локализации
    parser.addoption('--language', action='store', default="en",
                     help="Choose user language")


# фикстура инициализирующая браузер
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name") # тип браузера
    user_language = request.config.getoption("language")    # язык локализации
    browser = None
    if browser_name == "chrome":    # для Chrome
        # настраиваем локализацию
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # options.add_experimental_option('excludeSwitches', ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        print("\nstart chrome browser for test..")
        print(f"Language: {user_language}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox": # для Firefox
        # настраиваем локализацию
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        print(f"Language: {user_language}")
        browser = webdriver.Firefox(firefox_profile=fp, log_path=GECKO_LOG_PATH_FIREFOX)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()