from selenium import webdriver
from src.helpers.general import BASE_URL, INPUT_SELECTOR
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestToDo:
    def setup(self):
        capabilities = {
            "browserName": "chrome",
            "version": "80.0",
            "enableVNC": True,
            "enableVideo": False
        }

        self.driver = webdriver.Remote(
            command_executor='http://172.20.10.2:4444/wd/hub',
            desired_capabilities=capabilities)

        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,INPUT_SELECTOR)))

    def teardown(self):
        self.driver.close()
        print("basic teardown into class")

