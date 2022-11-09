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
        driver.get("https://www.youtube.com")
        time.sleep(6)
        active = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        active.click()
        time.sleep(3)


        s_bur = driver.find_element(By.XPATH, '//*[@id="button"]/yt-icon')
        s_bur.click()

        s_bar = driver.find_element(By.XPATH, '//*[@id="search"]')
        s_bar.send_keys("ashish")
        s_2 = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
        



        c_bar = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
        c_barsend_keys("vinod")

        time.sleep(5)
        sned_c = driver.find_element(By.XPATH, '//*[@id="submit-button"]/yt-button-shape/button')

        time.sleep(1)
        sned_c.click()
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
