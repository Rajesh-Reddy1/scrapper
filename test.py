import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class test():
    # service = FirefoxService(executable_path=GeckoDriverManager().install())
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

        self.driver.get("https://www.youtube.com")

        title = self.driver.title
        self.driver.implicitly_wait(1)
        
        cn = self.driver.find_elements(by=By.CSS_SELECTOR, value=".yt-simple-endpoint.style-scope.yt-formatted-string")
        n=[i.get_attribute("innerHTML") for i in cn]
        print(n)       
        print(title)
        
        self.driver.quit()


test()

