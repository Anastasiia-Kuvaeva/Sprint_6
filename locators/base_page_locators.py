from selenium.webdriver.common.by import By


class LocatorBase:
    # Локаторы общих элементов страниц
    YANDEX_SCOOTER_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    YANDEX_DZEN_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")