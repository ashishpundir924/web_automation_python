from selenium import webdriver
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        time.sleep(3)
        driver.implicitly_wait(10)  # seconds
        driver.get("https://web.whatsapp.com")
        time.sleep(120)
        s = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
        s.send_keys(pankaj)
        time.sleep(5)
        pankaj = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]')
        time.sleep(1)
        pankaj.click()
        time.sleep(2)
        chat_bar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        chat_bar.send_keys("or bhai kya hal")
        time.sleep(1)
        send = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        time.sleep(1)
        send.click()
        time.sleep(1)









    def tearDown(self):
        self.driver.implicitly_wait(100000)


if __name__ == "__main__":
    unittest.main()
