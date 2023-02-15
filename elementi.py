import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class test():
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

    def scrap(self,web,link):
        self.driver.get(web)
        self.driver.implicitly_wait(1)
        cn = self.driver.find_elements(by=By.CSS_SELECTOR, value=link)
        n=[i.get_attribute("href") for i in cn]
        print(n)
    def quit(self):
        self.driver.quit()


