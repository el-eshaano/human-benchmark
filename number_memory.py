from selenium import webdriver
from selenium.webdriver.common.by import By

from web_driver import WebDriverUtils


class NumberMemory:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.utils = WebDriverUtils(self.browser)

    def run(self):

        self.utils.open_url("https://humanbenchmark.com/dashboard")
        self.utils.start_challenge('Number Memory')

        game_running = True
        while(game_running):
            num = self.get_number()
            print(num)
            self.enter_number(num)
            self.go_next()

    def get_number(self) -> str:
        number_div = self.utils.find_element(By.CLASS_NAME, "big-number")
        return number_div.text

    def enter_number(self, num: str):
        text_box = self.utils.find_element(By.XPATH, "//input[@pattern='[0-9]*']")
        text_box.clear()
        text_box.send_keys(num)

        submit_button = self.utils.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        return

    def go_next(self):
        next_button = self.utils.find_element(By.XPATH, "//button[text()='NEXT']")
        next_button.click()
        return


if __name__ == '__main__':
    nm = NumberMemory()
    nm.run()
