import pytest
from src.tests.smoke_tests.base import TestToDo
from src.helpers.page_with_todo_opener import Opener
import src.helpers.general as helper


@pytest.mark.smoke
class TestMarkAsComplete(TestToDo):
    def test_add_new_todo(self):
        opener = Opener
        page = opener.open(self, self.driver)

        todo_class = page.getElement(self, self.driver, helper.TODO_SELECTOR).get_attribute('class')
        assert todo_class == ''

        is_completed = page.set_todo_as_complete(self, self.driver, 0)
        assert is_completed == 'completed'
