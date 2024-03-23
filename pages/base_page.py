from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # найти и вернуть элемент
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    # кликнуть по элементу
    def click_on_element(self, locator):
        self.find_element(locator).click()

    # найти элемент, кликнуть по нему и вернуть
    def find_and_click_element(self, locator):
        element = self.find_element(locator)
        element.click()
        return element

    # получить текст элемента
    def get_text_element(self, locator):
        return self.find_element(locator).text

    # ввести текст в элемент
    def input_keys_in_element(self, locator, value):
        self.find_element(locator).send_keys(value)

    # получить url текущей страницы
    def get_current_url(self):
        return self.driver.current_url

    # переход на новую вкладку браузера
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    # ожидание загрузки страницы
    def wait_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))