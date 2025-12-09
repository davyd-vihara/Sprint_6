from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class OrderPage(BasePage):
    """
    Page Object класс для страницы заказа самоката.
    Содержит методы для заполнения формы заказа и подтверждения.
    """

    def __init__(self, driver):
        """Инициализация страницы заказа."""
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_first_step(self, name, last_name, address, metro_station, phone):
        """
        Заполнение первой части формы заказа.
        Args:
            name (str): Имя заказчика
            last_name (str): Фамилия заказчика
            address (str): Адрес доставки
            metro_station (str): Станция метро
            phone (str): Номер телефона
        """
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)
        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    def select_metro_station(self, station_name):
        """
        Выбор станции метро из выпадающего списка.
        Args:
            station_name (str): Название станции метро
        """
        self.click_element(self.locators.METRO_INPUT)
        self.input_text(self.locators.METRO_INPUT, station_name)
        # Используем более точный локатор для выбора станции
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click_element(station_locator)

    def fill_second_step(self, date, rental_period, color, comment):
        """
        Заполнение второй части формы заказа.
        Args:
            date (str): Дата доставки в формате дд.мм.гггг
            rental_period (str): Период аренды (например, 'сутки', 'двое суток')
            color (str): Цвет самоката ('black' или 'grey')
            comment (str): Комментарий для курьера (опционально)
        """
        self.set_delivery_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        if comment:
            self.input_text(self.locators.COMMENT_INPUT, comment)

    def set_delivery_date(self, date):
        """
        Установка даты доставки самоката.
        Args:
            date (str): Дата в формате дд.мм.гггг
        Процесс:
        1. Ожидание загрузки страницы
        2. Клик в поле даты
        3. Очистка поля
        4. Ввод даты
        5. Подтверждение клавишей Enter
        """
        # Ждем пока вторая страница загрузится
        time.sleep(2)

        # Находим поле даты
        date_input = self.wait_for_element(self.locators.DATE_INPUT)

        # Кликаем в поле даты
        date_input.click()

        # Очищаем поле (на всякий случай)
        date_input.clear()

        # Вводим дату
        date_input.send_keys(date)

        # Нажимаем Enter для подтверждения
        date_input.send_keys(Keys.ENTER)

        # Ждем немного чтобы дата применилась
        time.sleep(1)

    def select_rental_period(self, period):
        """
        Выбор периода аренды из выпадающего списка.
        Args:
            period (str): Период аренды ('сутки', 'двое суток' и т.д.)
        """
        # Находим dropdown периода аренды
        dropdown = self.wait_for_element(self.locators.RENTAL_PERIOD_DROPDOWN)

        # Кликаем, чтобы открыть список
        dropdown.click()

        # Ждем появления опций
        time.sleep(1)

        # Выбираем нужный период
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        period_element = self.wait_for_element(period_locator)
        period_element.click()

    def select_color(self, color):
        """
        Выбор цвета самоката.
        Args:
            color (str): Цвет самоката - 'black' (черный) или 'grey' (серый)
        """
        if color == "black":
            self.click_element(self.locators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(self.locators.COLOR_GREY)

    def confirm_order(self):
        """
        Подтверждение заказа.
        Процесс: клик по кнопке 'Заказать' → клик по кнопке 'Да' в модальном окне.
        """
        self.click_element(self.locators.ORDER_BUTTON)
        self.click_element(self.locators.CONFIRM_BUTTON)

    def is_success_message_displayed(self):
        """
        Проверка отображения сообщения об успешном заказе.
        Returns:
            bool: True если сообщение отображается, False если нет
        """
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)

    def get_success_message(self):
        """
        Получение текста сообщения об успешном заказе.
        Returns:
            str: Текст сообщения о успешном оформлении заказа
        """
        return self.get_text(self.locators.SUCCESS_MESSAGE)
