import pytest
from src.tests.smoke_tests.base import TestToDo
from src.page.main import MainPage


@pytest.mark.smoke
class TestNoTodos(TestToDo):
    def test_title(self):
        assert "React • TodoMVC" == self.driver.title

    def test_todos_form(self):
        page = MainPage

        header = page.getElement(self, self.driver, "/html/body/section/div/section")
        assert header is None

        footer = page.getElement(self, self.driver, "/html/body/section/div/footer")
        assert footer is None
