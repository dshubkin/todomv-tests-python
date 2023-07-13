import pytest
from src.tests.smoke_tests.base import TestToDo
from src.helpers.page_with_todo_opener import Opener


@pytest.mark.smoke
class TestMarkAsComplete(TestToDo):
    def test_add_new_todo(self):
        opener = Opener
        page = opener.open(self, self.driver, 3)

        page.set_todo_as_complete(self, self.driver, 1)
        page.click_on_mark_all_as_complete(self, self.driver)

        is_all_complete = page.check_all_as_complete(self, self.driver)
        assert is_all_complete is True
