import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """Базовый класс для web-страниц"""
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url
    
    def open(self):
        """Открытие web-стрницы"""
        self.browser.get(self.url)
    
    def is_element_present(self, locator, timeout=10) -> bool:
        """Проверка на существование элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator), 
                                    message=f"Can't find element by locator {locator}")
        except TimeoutException:
            return False
        return True
    
    def find_element(self, locator, timeout=10):
        """Поиск элемента на странице"""
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator), 
                                    message=f"Can't find element by locator {locator}")
        except TimeoutException:
            return False
        return element
    
    def find_elements(self, locator, timeout=10):
        """Поиск элементов на странице"""
        try:
            elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator), 
                                    message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            return False
        return elements

    def is_not_element_present(self, locator, timeout=5):
        """Проверка что элемент НЕ появится на странице в течении timeout"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False 
    
    def is_dissapeared(self, locator, timeout=5):
        """Проверка что элемент сейчас есть, НО исчезнет"""
        try:
            # WebDriverWait(self.browser, poll_frequency=1, ignored_exceptions=TimeoutException)
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False, "Element is not Dissapeared!"
        return True, ""
        

    # метод из курса Stepik для решения примера из alert
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
    
