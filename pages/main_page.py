from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """
    Page Object класс для главной страницы Яндекс.Самокат.
    Содержит методы для взаимодействия с элементами главной страницы.
    """

    def __init__(self, driver):
        """Инициализация главной страницы."""
        super().__init__(driver)
        self.locators = MainPageLocators()

    def click_question(self, question_index):
        """
        Клик по вопросу в разделе 'Вопросы о важном'.
        Args:
            question_index (int): Индекс вопроса (0-7)
        """
        self.click_element_js(self.locators.QUESTION_LOCATORS[question_index])

    def get_answer_text(self, answer_index):
        """
        Получение текста ответа на вопрос.
        Args:
            answer_index (int): Индекс ответа (0-7)
        Returns:
            str: Текст ответа
        """
        return self.get_text(self.locators.ANSWER_LOCATORS[answer_index])

    def click_order_button_top(self):
        """Клик по верхней кнопке 'Заказать' в шапке страницы."""
        self.click_element_js(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """
        Клик по нижней кнопке 'Заказать' в подвале страницы.
        Перед кликом прокручивает страницу к кнопке.
        """
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element_js(self.locators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        """Клик по логотипу Самоката для перехода на главную страницу."""
        self.click_element_js(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекс для перехода на главную страницу Дзен."""
        self.click_element_js(self.locators.YANDEX_LOGO)
