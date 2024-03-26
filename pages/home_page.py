import allure
from locators.home_page_locators import CookieLocators
from locators.home_page_locators import OrderLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Принятие cookie')
    def accept_cookie(self):
        self.click_on_element(CookieLocators.COOKIE_BUTTON)

    @allure.step('Клик на кнопку "Заказать" в шапке сайта')
    def click_order_button_header(self):
        self.click_on_element(OrderLocators.ORDER_HEADER_BUTTON)

    @allure.step('Клик на кнопку "Заказать" в центре страницы')
    def click_order_button(self):
        self.click_on_element(OrderLocators.ORDER_BUTTON)

    @allure.step("Клик на вопрос, получение атрибутов видимости вопроса и ответа, получение текста ответа")
    def get_question_answer(self, question_locator, answer_locator):
        # кликаем по вопросу и получаем атрибут его активности
        question_expanded = self.find_and_click_element(question_locator).get_attribute("aria-expanded")
        # полкчение признака видимости ответа
        answer_hidden = self.find_element(answer_locator).is_displayed()
        # получение текста ответа
        answer_text = self.get_text_element(answer_locator)
        return question_expanded, answer_hidden, answer_text
