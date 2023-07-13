import pytest
from src.tests.smoke_tests.base import TestToDo
from src.page.main import MainPage
from src.helpers.general import TODO_SELECTOR, TEST_TEXT


@pytest.mark.smoke
class TestNewTodo(TestToDo):
    def test_add_new_todo(self):
        page = MainPage

        assert page.count_todos(self, self.driver) == 0

        page.enterNewTodo(self, self.driver)
        assert page.count_todos(self, self.driver) == 1

        text = page.get_text_arr(self, self.driver, TODO_SELECTOR)[0]
        assert text == TEST_TEXT.strip()
