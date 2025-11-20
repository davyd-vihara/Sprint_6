import pytest
import os
import sys


def run_tests():
    """
    Основная функция для запуска автоматизированных тестов.
    Returns:
        int: Код завершения (0 - успех, 1 и более - ошибки)
    """
    print("=== Запуск тестов Яндекс.Самокат ===")

    # Добавляем текущую директорию в PATH для корректных импортов
    # Это необходимо для разрешения зависимостей между модулями проекта
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # Запускаем pytest напрямую с параметрами
    exit_code = pytest.main([
        "tests/",  # Директория с тестами
        "-v",  # Подробный вывод (verbose)
        "--alluredir=allure-results",  # Директория для результатов Allure
        "-s"  # Вывод print-ов в консоль (no capture)
    ])

    # Обработка результатов выполнения тестов
    if exit_code == 0:
        print("\n Все тесты прошли успешно!")
        print("\n Для просмотра Allure отчета выполните команду:")
        print("   allure serve allure-results")
    else:
        print(f"\n Тесты завершены с ошибками (код: {exit_code})")

    return exit_code


if __name__ == "__main__":
    """
    Точка входа в программу.
    Запускает тесты и возвращает код завершения в операционную систему.
    """
    sys.exit(run_tests())
