import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import webelement


class Class:

    def __init__(self):
        self.browser = webdriver.Firefox()

    def open_url(self, url):
        self.browser.get(url)

    def find_element(self, method: str, params: str = None, delay: int = 100) -> webelement:
        return WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((method, params)))

    def run(self):

        self.open_url("https://humanbenchmark.com/dashboard")

        number_memory_icon = self.find_element(By.XPATH, "//div[@title='Number Memory']")
        number_memory_icon.click()

        play_text = self.find_element(By.XPATH, "//a[@href='/tests/number-memory']")
        play_text.click()

        start_button = self.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()

        game_running = True
        while(game_running):
            num = self.get_number()
            print(num)
            self.enter_number(num)
            self.go_next()

    def get_number(self) -> str:
        number_div = self.find_element(By.CLASS_NAME, "big-number")
        return number_div.text

    def enter_number(self, num: str):
        text_box = self.find_element(By.XPATH, "//input[@pattern='[0-9]*']")
        text_box.clear()
        text_box.send_keys(num)

        submit_button = self.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        return

    def go_next(self):
        next_button = self.find_element(By.XPATH, "//button[text()='NEXT']")
        next_button.click()
        return


if __name__ == '__main__':
    c = Class()
    c.run()
