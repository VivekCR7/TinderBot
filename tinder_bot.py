from selenium import webdriver
from time import sleep

from secrets import username, password

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome()

	def login(self):
		self.driver.get("https://tinder.com")

		sleep(2)


		fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
		fb_btn.click()

		#switch to login popup
		base_window = self.driver.window_handles[0]
		self.driver.switch_to_window(self.driver.window_handles[1]) 

		email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
		email_in.send_keys(username)

		pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
		pw_in.send_keys(password)

		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()

		self.driver.switch_to_window(base_window)

		popup_1 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
		popup_1.click()

		popup_2 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
		popup_2.click()

	def like(self):
		like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
		like_btn.click()

	def dislike(self):
		dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
		dislike_btn.click()

	def auto_like(self):
		while True:
			sleep(0.5)
			self.like()

bot = TinderBot()
bot.login()