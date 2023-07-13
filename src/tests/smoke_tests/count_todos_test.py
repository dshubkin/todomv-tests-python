import pytest
from src.tests.smoke_tests.base import TestToDo
from src.helpers.page_with_todo_opener import Opener


@pytest.mark.smoke
class TestCountTodos(TestToDo):
    def test_add_new_todo(self):
        opener = Opener
        page = opener.open(self, self.driver)

        count_before = page.get_count_todos(self, self.driver)
        assert count_before == "1 item left"

        page.set_todo_as_complete(self, self.driver, 0)

        count_after = page.get_count_todos(self, self.driver)
        assert count_after == "0 items left"
