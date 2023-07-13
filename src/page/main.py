from selenium.common.exceptions import NoSuchElementException
from src.tests.smoke_tests.base import TestToDo
from selenium import webdriver
import string
import src.helpers.general as helper


class MainPage:
    def getElement(self: TestToDo, driver: webdriver, selector: string):
        element = None
        try:
            element = driver.find_element_by_xpath(selector)
        except NoSuchElementException:
            pass
        return element

    def getElements(self: TestToDo, driver: webdriver, selector: string):
        elements = None
        try:
            elements = driver.find_elements_by_xpath(selector)
        except NoSuchElementException:
            pass
        return elements

    def enterNewTodo(self: TestToDo, driver: webdriver, text=''):
        driver.find_element_by_xpath(helper.INPUT_SELECTOR).send_keys(helper.TEST_TEXT + text)
        driver.find_element_by_xpath(helper.INPUT_SELECTOR).send_keys(u'\ue007')

    def count_todos(self: TestToDo, driver: webdriver):
        elements = []
        try:
            elements = driver.find_elements_by_xpath(helper.TODO_SELECTOR)
        except NoSuchElementException:
            pass
        return len(elements)

    def get_text_arr(self: TestToDo, driver: webdriver, selector: string):
        text = []
        elements = driver.find_elements_by_xpath(selector)
        for element in elements:
            text.append(element.text)
        return text

    def set_todo_as_complete(self: TestToDo, driver: webdriver, index: int):
        elements_check = driver.find_elements_by_xpath(helper.TODO_CHECK_SELECTOR)
        elements_check[index].click()
        elements = driver.find_elements_by_xpath(helper.TODO_SELECTOR)
        status = elements[index].get_attribute('class')
        if status:
            return status
        else:
            raise ValueError('У туду с индексом' + str(int) + 'не найден атрибут class с значением <<complete>>')

    def click_on_mark_all_as_complete(self: TestToDo, driver: webdriver):
        driver.find_element_by_xpath(helper.MARK_ALL_AS_COMPLETE_SELECTOR).click()

    def check_all_as_complete(self: TestToDo, driver: webdriver):
        flag = True
        elements = driver.find_elements_by_xpath(helper.TODO_SELECTOR)
        for element in elements:
            if element.get_attribute('class') != 'completed':
                flag = False
        return flag

    def get_count_todos(self: TestToDo, driver: webdriver):
        return driver.find_element_by_xpath(helper.TODO_COUNT_SELECTOR).text

    def is_visible(self: TestToDo, driver: webdriver, selector: string):
        element = None
        try:
            element = driver.find_element_by_xpath(selector)
        except NoSuchElementException:
            pass
        if element is None:
            return False
        else:
            if element.is_displayed() is True:
                return True

    def click_on_element(self:TestToDo, driver: webdriver, selector: string):
        driver.find_element_by_xpath(selector).click()
