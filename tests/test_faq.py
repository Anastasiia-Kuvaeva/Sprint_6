import allure
import pytest

from data import FAQAnswers
from locators.home_page_locators import FAQLocators
from pages.home_page import HomePage


class TestQuestionOpen:
    @pytest.mark.parametrize("question_locator, answer_locator, answer_text", [
        (FAQLocators.QUESTION_1, FAQLocators.ANSWER_1, FAQAnswers.TEXT_1),
        (FAQLocators.QUESTION_2, FAQLocators.ANSWER_2, FAQAnswers.TEXT_2),
        (FAQLocators.QUESTION_3, FAQLocators.ANSWER_3, FAQAnswers.TEXT_3),
        (FAQLocators.QUESTION_4, FAQLocators.ANSWER_4, FAQAnswers.TEXT_4),
        (FAQLocators.QUESTION_5, FAQLocators.ANSWER_5, FAQAnswers.TEXT_5),
        (FAQLocators.QUESTION_6, FAQLocators.ANSWER_6, FAQAnswers.TEXT_6),
        (FAQLocators.QUESTION_7, FAQLocators.ANSWER_7, FAQAnswers.TEXT_7),
        (FAQLocators.QUESTION_8, FAQLocators.ANSWER_8, FAQAnswers.TEXT_8)
    ])
    @allure.title("Тестирование раздела 'Вопросы о важном'")
    @allure.description('''Алгоритм тестирования: 
    1. Принимаем cookie, 
    2. Кликаем по вопросу и получаем необходимые атрибуты, 
    3. Сверяем полученные и эталонные данные''')
    def test_question_open(self, driver, question_locator, answer_locator, answer_text):
        home_page = HomePage(driver)
        home_page.accept_cookie()
        question_expanded, answer_hidden, answer_text_actual = home_page.get_question_answer(question_locator,
                                                                                             answer_locator)
        # проверки
        assert question_expanded == 'true', f'Ожидалось значение атрибута вопроса "aria-expanded": "true", получено "{question_expanded}"'
        assert answer_hidden == True, f'Ожидалось наличие атрибута вопроса "hidden", но не найдено'
        assert answer_text_actual == answer_text, f'Ожидалось значение текста вопроса: "{answer_text}", получено "{answer_text_actual}"'
