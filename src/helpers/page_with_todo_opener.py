from src.page.main import MainPage
from src.tests.smoke_tests.base import TestToDo
from selenium import webdriver


class Opener:
    def open(self: TestToDo, driver: webdriver, try_number: int = 1):
        page = MainPage
        for number in range(try_number):
            page.enterNewTodo(self, driver, str(number))
        return page
