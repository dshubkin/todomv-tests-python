import pytest
from src.tests.smoke_tests.base import TestToDo
from src.helpers.page_with_todo_opener import Opener
import src.helpers.general as helper


@pytest.mark.smoke
class TestCountTodos(TestToDo):
    def test_add_new_todo(self):
        opener = Opener
        page = opener.open(self, self.driver, 3)

        assert page.is_visible(self, self.driver, helper.TODO_CLEAR_COMPLETED_SELECTOR) is False

        page.click_on_mark_all_as_complete(self, self.driver)
        assert page.is_visible(self, self.driver, helper.TODO_CLEAR_COMPLETED_SELECTOR) is True

        page.click_on_element(self, self.driver, helper.TODO_CLEAR_COMPLETED_SELECTOR)
        assert page.is_visible(self, self.driver, helper.TODO_CLEAR_COMPLETED_SELECTOR) is False

        assert page.getElements(self, self.driver, helper.TODO_SELECTOR) == []

