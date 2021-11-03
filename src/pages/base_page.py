import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """Базовый класс для web-страниц"""
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url
    
    def open(self):
        """Открытие web-стрницы"""
        self.browser.get(self.url)
    
    def is_element_present(self, by_what, locator) -> bool:
        """Проверка на существование элемента на странице"""
        try:
            self.browser.find_element(by_what, locator)
        except NoSuchElementException:
            return False
        return True
    
    def find_element(self, locator, timeout=10):
        """Поиск элемента на странице"""
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator), 
                                    message=f"Can't find element by locator {locator}")
        except NoSuchElementException:
            return False
        return element
    
    def find_elements(self, locator, timeout=10):
        """Поиск элементов на странице"""
        try:
            elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator), 
                                    message=f"Can't find elements by locator {locator}")
        except NoSuchElementException:
            return False
        return elements

    # метод из курса Stepik
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(f"answer={answer}")
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
