import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import creds


class Testing(unittest.TestCase):
    flag = True
    driver = webdriver.Chrome("D:\Download\chromedriver_win32 (4)\chromedriver.exe")
    def test_string(self,):
        self.assertTrue(Testing.flag)

    def test_selenium(self):
        driver  = Testing.driver
        driver.get("https://www.linkedin.com/")
        email = driver.find_element(By.XPATH,"//*[@id=\"session_key\"]")
        driver.maximize_window()
        email.send_keys(creds.user_id)
        password = driver.find_element(By.XPATH,"//*[@id=\"session_password\"]")
        password.send_keys(creds.password)
        driver.find_element(By.XPATH,"//*[@id=\"main-content\"]/section[1]/div/div/form/button").click()
        time.sleep(10)
        self.assertEqual(driver.title,'Feed | LinkedIn')
        driver.close()
    
    def tearDown(self) -> None:
        Testing.driver.quit()
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()