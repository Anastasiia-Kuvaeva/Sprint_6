import allure
import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import (Paths, OrderInformation)


class TestOrder:

    @allure.title("Тестирование перехода при клике по логотипу Яндекс")
    @allure.description('''Алгоритм тестирования: 
        1. Кликаем по кнопке "Заказать", 
        2. Кликаем по логотипу Яндекса, 
        3. Переходим на новую вкладку, 
        4. Сверяем URL''')
    def test_go_logo_yandex(self, driver):
        order_page = OrderPage(driver)
        # кликаем по логотипу Яндекс и и дожидаемся загрузки страницы Дзен
        order_page.click_yandex_dzen_logo()
        order_page.switch_to_new_tab()
        order_page.wait_url(Paths.YANDEX_DZEN_URL)
        # Проверка URL
        assert order_page.get_current_url() == Paths.YANDEX_DZEN_URL

    @allure.title("Тестирование перехода при клике по логотипу Яндекс Самокат")
    @allure.description('''Алгоритм тестирования: 
            1. Кликаем по кнопке "Заказать",
            2. Кликаем по логотипу Самокат,           
            4. Сверяем URL''')
    def test_go_logo_scooter(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        # кликаем по кнопке "Заказать" и дожидаемся загрузки страницы заказа (находясь на главной странице)
        home_page.accept_cookie()
        home_page.click_order_button_header()
        home_page.wait_url(Paths.ORDER_URL)
        # кликаем по логотипу Самокат и и дожидаемся загрузки главной страницы
        order_page.click_scooter_logo()
        order_page.wait_url(Paths.YANDEX_SCOOTER_URL)
        # Проверка URL
        assert home_page.get_current_url() == Paths.YANDEX_SCOOTER_URL

    @pytest.mark.parametrize("method, order_data", [
        ("click_order_button_header", OrderInformation.order_1),
        ("click_order_button", OrderInformation.order_2)
    ])
    @allure.title("Тестирование создание заказа по кноаке 'Заказать'")
    @allure.description('''Алгоритм тестирования: 
                1. Принимаем cookie,
                2. Кликаем по кнопке "заказать",   
                3. Заполняем форму заказа №1,           
                4. Кликаем по кнопке "Далее",    
                3. Заполняем форму заказа №2,           
                4. Кликаем по кнопке "Да",           
                4. Проверка отображения формы "Заказ оформлен"''')
    def test_create_order_from_header_button(self, driver, method, order_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        # принимаем cookie
        home_page.accept_cookie()
        # клик по кнопке "Заказать" в шапке сайта / в центре страницы
        getattr(home_page, method)()
        # заполнение формы №1
        order_page.input_form_1(order_data)
        # клик по кнопке "Далее"
        order_page.click_next_button()
        # заполнение формы №2
        order_page.input_form_2(order_data)
        # клик по кнопке "Заказать"
        order_page.click_order_button()
        # клик по кнопке "Да"
        order_page.click_confirm_button()
        # проверка отображения формы с заголовком "Заказ оформлен"
        assert order_page.check_order_complete()
