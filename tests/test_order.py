import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import ORDER_TEST_DATA
from config import Config


class TestOrder:
    """Тесты функциональности заказа самоката и навигации."""

    @allure.title("Позитивный сценарий заказа через {entry_point} кнопку")
    @pytest.mark.parametrize(
        "entry_point,name,last_name,address,metro,phone,date,period,color,comment", ORDER_TEST_DATA
    )
    def test_successful_order(self, driver, entry_point, name, last_name, address, metro, phone, date, period, color, comment):
        """
        Позитивный тест полного цикла заказа самоката.
        Проверяет заказ через обе кнопки (верхнюю и нижнюю) с разными данными.
        """
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step(f"Нажать кнопку 'Заказа' ({entry_point})"):
            if entry_point == "верхняя":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Заполнить первую часть формы заказа"):
            order_page = OrderPage(driver)
            order_page.fill_first_step(name, last_name, address, metro, phone)

        with allure.step("Заполнить вторую часть формы заказа"):
            order_page.fill_second_step(date, period, color, comment)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить сообщение об успешном заказе"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, f"Неверное сообщение: {success_message}"

    @allure.title("Проверка перехода на главную через логотип Самокат")
    def test_scooter_logo_redirect(self, driver):
        """Тест навигации: переход на главную страницу через логотип Самоката."""
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step("Перейти на страницу заказа и вернуться через логотип"):
            main_page.click_order_button_top()
            main_page.click_scooter_logo()

        with allure.step("Проверить URL главной страницы"):
            assert main_page.get_current_url() == Config.BASE_URL

    @allure.title("Проверка перехода на Дзен через логотип Яндекс")
    def test_yandex_logo_redirect(self, driver):
        """
        Тест навигации: переход на Дзен через логотип Яндекс.
        Проверяет открытие новой вкладки и корректный URL.
        """
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step("Сохранить текущее окно"):
            original_window = main_page.get_current_window_handle()

        with allure.step("Нажать на логотип Яндекс"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия нового окна и переключиться"):
            main_page.wait_for_new_window_and_switch()

        with allure.step("Проверить что открылась страница Дзен"):
            main_page.wait_for_url_contains("dzen.ru")
            assert main_page.is_dzen_opened()

        with allure.step("Закрыть новое окно и вернуться к исходному"):
            main_page.close_current_window()
            main_page.switch_to_window(original_window)
