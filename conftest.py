import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для инициализации и управления веб-драйвером.
    Scope:
        function - создает новый драйвер для каждого теста
    Process:
        1. Инициализация Firefox драйвера
        2. Максимизация окна браузера
        3. Передача драйвера в тест
        4. Закрытие драйвера после завершения теста
    Returns:
        WebDriver: Экземпляр Firefox WebDriver
    """
    # Инициализация сервиса Firefox
    service = Service()

    # Создание экземпляра Firefox драйвера
    driver = webdriver.Firefox(service=service)

    # Максимизация окна браузера для стабильности тестов
    driver.maximize_window()

    # Передача драйвера тестовой функции
    yield driver

    # Закрытие браузера после завершения теста
    driver.quit()


@pytest.fixture(autouse=True)
def log_test_info(request):
    """
    Автоматическая фикстура для логирования начала и окончания тестов.
    Args:
        request: Объект pytest request с информацией о тесте
    Features:
        - autouse=True: автоматически применяется ко всем тестам
        - Логирует имя теста перед его запуском
        - Логирует завершение теста после его выполнения
    """
    # Логирование начала теста
    print(f"\n=== Starting test: {request.node.name} ===")

    # Выполнение теста
    yield

    # Логирование завершения теста
    print(f"=== Finished test: {request.node.name} ===\n")
