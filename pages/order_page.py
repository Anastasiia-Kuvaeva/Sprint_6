import time

import allure
from pages.base_page import BasePage
from locators.base_page_locators import LocatorBase
from locators.order_page_locators import (OrderLocatorsForm1, OrderLocatorsForm2, OrderLocatorsConfirmForm,
                                          OrderLocatorsLastForm)


class OrderPage(BasePage):

    @allure.step('Клик по логотипу Яндекс Dzen')
    def click_yandex_dzen_logo(self):
        self.click_on_element(LocatorBase.YANDEX_DZEN_LOGO)

    @allure.step('Клик по логотипу Самокат')
    def click_scooter_logo(self):
        self.click_on_element(LocatorBase.YANDEX_SCOOTER_LOGO)

    @allure.step('Заполнение данных формы №1')
    def input_form_1(self, data):
        self.input_keys_in_element(OrderLocatorsForm1.NAME_FIELD, data['name'])
        self.input_keys_in_element(OrderLocatorsForm1.SURNAME_FIELD, data['surname'])
        self.input_keys_in_element(OrderLocatorsForm1.ADDRESS_FIELD, data['address'])
        self.click_on_element(OrderLocatorsForm1.METRO_FIELD)
        self.click_on_element(OrderLocatorsForm1.METRO_STATION_FIELD)
        self.input_keys_in_element(OrderLocatorsForm1.TELEPHONE_FIELD, data['phone'])

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderLocatorsForm1.BUTTON)

    @allure.step('Заполнение данных формы №2')
    def input_form_2(self, data):
        self.input_keys_in_element(OrderLocatorsForm2.DELIVERY_DATE_FIELD, data['delivery_date']),
        self.click_on_element(OrderLocatorsForm2.RENT_PERIOD_FIELD)
        self.click_on_element(OrderLocatorsForm2.RENT_PERIOD_CHOICE_FIELD)
        self.click_on_element(OrderLocatorsForm2.COLOR_FIELD)
        self.input_keys_in_element(OrderLocatorsForm2.COMMENT_FIELD, data['comment'])

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderLocatorsForm2.BUTTON)

    @allure.step('Клик на кнопку "Да"')
    def click_confirm_button(self):
        self.click_on_element(OrderLocatorsConfirmForm.BUTTON)

    @allure.step('Проверка отображения формы с заголовком "Заказ оформлен"')
    def check_order_complete(self):
        return self.find_element(OrderLocatorsLastForm.ORDER_COMPLETED_FIELD).is_displayed()