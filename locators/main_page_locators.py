from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вопросы и ответы
    QUESTION_LOCATORS = [tuple([By.ID, f"accordion__heading-{i}"]) for i in range(8)]
    ANSWER_LOCATORS = [tuple([By.ID, f"accordion__panel-{i}"]) for i in range(8)]

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
