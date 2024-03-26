from selenium.webdriver.common.by import By


# локаторы блока "Вопросы о важном"
class FAQLocators:
    # локаторы вопросов
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    # локаторы ответов
    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")


# локаторы, связанные с Cookie
class CookieLocators:
    COOKIE_BUTTON = (By.XPATH, ".//button[@id = 'rcc-confirm-button']")


# локаторы, связанные с заказами
class OrderLocators:
    # кнопка 'Заказать' в шапке сайта
    ORDER_HEADER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(), 'Заказать')]")
    # кнопка 'Заказать' на странице
    ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[contains(text(), 'Заказать')]")
