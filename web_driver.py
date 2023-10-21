
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import webelement


class WebDriverUtils:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        self.browser.get(url)

    def find_element(self, method: str, params: str, delay: int = 100):
        return WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((method, params)))

    def start_challenge(self, challenge: str):
        challenge_icon = self.find_element(By.XPATH, f"//div[@title='{challenge}']")
        challenge_icon.click()

        play_str = ''.join([x.lower() + '-' for x in challenge.split()])[:-1]
        play_text = self.find_element(By.XPATH, f"//a[@href='/tests/{play_str}']")
        play_text.click()

        start_button = self.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()


    def __str__(self):
    	return "I am a webdrive object"