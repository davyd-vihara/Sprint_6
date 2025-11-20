import pytest
import allure
from pages.main_page import MainPage
from data.test_data import QUESTIONS_AND_ANSWERS


class TestQuestions:
    """Тесты раздела 'Вопросы о важном' на главной странице."""

    @allure.title("Проверка ответа на вопрос: {question_text}")
    @pytest.mark.parametrize("question_index,question_text,expected_answer", QUESTIONS_AND_ANSWERS)
    def test_question_answer(self, driver, question_index, question_text, expected_answer):
        """
        Параметризованный тест проверки корректности ответов на вопросы.
        Проверяет что при клике на каждый вопрос отображается правильный ответ.
        Тест запускается для всех 8 вопросов из тестовых данных.
        Args:
            question_index (int): Индекс вопроса (0-7)
            question_text (str): Текст вопроса для отображения в Allure
            expected_answer (str): Ожидаемый текст ответа
        """
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.go_to_site()

        with allure.step(f"Нажать на вопрос №{question_index + 1}"):
            main_page.click_question(question_index)

        with allure.step("Проверить текст ответа"):
            actual_answer = main_page.get_answer_text(question_index)
            assert actual_answer == expected_answer, f"Для вопроса '{question_text}' ожидалось: {expected_answer}, получено: {actual_answer}"
