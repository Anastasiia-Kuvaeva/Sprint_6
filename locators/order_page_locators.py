from selenium.webdriver.common.by import By


# поля первой формы заказа
class OrderLocatorsForm1:
    NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Имя')]")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    METRO_STATION_FIELD = (By.XPATH, ".//div[text() = 'Красносельская']")
    TELEPHONE_FIELD = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    BUTTON = (By.XPATH, ".//button[contains(text(),'Далее')]")


# поля второй формы заказа
class OrderLocatorsForm2:
    DELIVERY_DATE_FIELD = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENT_PERIOD_CHOICE_FIELD = (By.XPATH, ".//div[contains(text(),'сутки')]")
    COLOR_FIELD = (By.XPATH, ".//label[@for = 'black']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[contains(text(), 'Заказать')]")


# поля формы подтверждения заказа
class OrderLocatorsConfirmForm:
    BUTTON = (By.XPATH, ".//button[contains(text(),'Да')]")


# поля последней формы заказа
class OrderLocatorsLastForm:
    ORDER_COMPLETED_FIELD = (By.XPATH, ".//div[text() = 'Заказ оформлен']")
