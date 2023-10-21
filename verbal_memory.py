import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from web_driver import WebDriverUtils

class VerbalMemory:

	def __init__(self):
		self.browser = webdriver.Firefox()
		self.utils = WebDriverUtils(self.browser)
		self.seen_words = set()

	def run(self):
		
		self.utils.open_url("https://humanbenchmark.com/dashboard")
		self.utils.start_challenge('Verbal Memory')

		game_running = True
		while game_running:
			word = self.get_word()
			seen_button = self.utils.find_element(By.XPATH, "//button[text()='SEEN']")
			new_button = self.utils.find_element(By.XPATH, "//button[text()='NEW']")
			
			if word in self.seen_words:
				seen_button.click()
			else:
				self.seen_words.add(word)
				new_button.click()

			time.sleep(0.1)

	def get_word(self):
		word_link = self.utils.find_element(By.CLASS_NAME, "word")
		return word_link.text

if __name__ == '__main__':
	vm = VerbalMemory()
	vm.run()