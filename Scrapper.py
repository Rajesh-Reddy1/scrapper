from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class Scrapper():
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()

    def scrap(self,web,link):
        self.driver.get(web)
        self.driver.implicitly_wait(1)
        cn = self.driver.find_elements(by=By.CSS_SELECTOR, value=link)
        self.n=[i.get_attribute("href") for i in cn]
        self.names=[i.get_attribute("innerHTML") for i in cn]
        print(self.names)
        
    def mul_scarp(self,link):
        a=[]
        for i in self.n[:5]:
            self.driver.get(i)
            self.driver.implicitly_wait(1)
            kn = self.driver.find_elements(by=By.ID, value=link)
            n=[i.get_attribute("innerHTML") for i in kn]
            a.extend(n)
        res = dict(map(lambda i,j : (i,j) , self.names,a))
        print(res)

    def quit(self):
        self.driver.quit()