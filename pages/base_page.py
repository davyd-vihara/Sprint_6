from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config


class BasePage:
    """
    Базовый класс Page Object для всех страниц.
    Содержит общие методы для работы с веб-элементами.
    """

    def __init__(self, driver):
        """Инициализация базовой страницы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
        self.base_url = Config.BASE_URL

    def go_to_site(self):
        """Переход на базовый URL сайта."""
        self.driver.get(self.base_url)

    def wait_for_element(self, locator):
        """Ожидание присутствия элемента в DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator):
        """Ожидание видимости элемента на странице."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Ожидание кликабельности элемента."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        """Клик по элементу с ожиданием кликабельности."""
        self.wait_for_clickable(locator).click()

    def click_element_js(self, locator):
        """
        Клик по элементу через JavaScript.
        Используется когда обычный клик не работает (перекрытие и т.д.)
        """
        element = self.wait_for_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element)

    def input_text(self, locator, text):
        """Ввод текста в поле с предварительной очисткой."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Получение текста элемента."""
        return self.wait_for_visible(locator).text

    def is_element_visible(self, locator):
        """
        Проверка видимости элемента.
        Возвращает True если элемент видим, False если нет.
        """
        try:
            return self.wait_for_visible(locator).is_displayed()
        except:
            return False

    def get_current_url(self):
        """Получение текущего URL страницы."""
        return self.driver.current_url

    def scroll_to_element(self, locator):
        """Прокрутка страницы к элементу."""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
