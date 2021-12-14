import unittest
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from faker import Faker
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import unittest

# import AllureReports

faker_class = Faker()


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        code = requests.get("https://www.google.com").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")
        if not "Google" in driver.title:
            raise Exception("Google page has wrong Title!")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Google Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        driver = webdriver.Chrome()
        driver.get("https://qasvus.wordpress.com/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Link(href) for header message \"California Real Estate\" is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Link(src) for first home image under \"About us\" is",
              driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))

        assert "California Real Estate" in driver.title
        print('"California Real Estate" is in website title')
        print("Website title is", driver.title)

        driver.find_element(By.ID, "g2-name").click()
        driver.find_element(By.ID, "g2-name").send_keys("Ruslan")
        driver.find_element(By.ID, "g2-email").click()
        driver.find_element(By.ID, "g2-email").send_keys("stepanyuk1988@gmail.com")
        driver.find_element(By.ID, "contact-form-comment-g2-message").click()
        driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Hi there!")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(), 'go back')]").click()
        print("Attribute \"type\" for submit button is",
              driver.find_element(By.XPATH, "//button[@type=\"submit\"]").get_attribute("type"))

        driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        print("Google Url has ", requests.get("https://www.google.com").status_code, " as status Code")
        code = requests.get("https://www.google.com").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200")
        if not "Google" in driver.title:
            raise Exception("Google page has wrong Title!")

        # Check that an element is present on the DOM of a page and visible.
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "q")))
            print("First Google Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("google_page_loading_error.png")
            driver.save_screenshot('google_page_loading_error.png')

        # Checking page title for "Google" then print it
        self.assertIn("Google", driver.title)
        print("Page has", driver.title + " as Page title")

        driver = webdriver.Firefox()
        driver.get("https://qasvus.wordpress.com/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Link(href) for header message \"California Real Estate\" is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Link(src) for first home image under \"About us\" is",
              driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))

        assert "California Real Estate" in driver.title
        print('"California Real Estate" is in website title')
        print("Website title is", driver.title)

        driver.find_element(By.ID, "g2-name").click()
        driver.find_element(By.ID, "g2-name").send_keys("Ruslan")
        driver.find_element(By.ID, "g2-email").click()
        driver.find_element(By.ID, "g2-email").send_keys("stepanyuk1988@gmail.com")
        driver.find_element(By.ID, "contact-form-comment-g2-message").click()
        driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Hi there!")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(), 'go back')]").click()
        print("Attribute \"type\" for submit button is",
              driver.find_element(By.XPATH, "//button[@type=\"submit\"]").get_attribute("type"))

        driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
