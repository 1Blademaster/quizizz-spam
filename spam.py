import secrets
import time

import pyautogui as pag
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

init(autoreset=True)

URL = 'https://quizizz.com/join'

def spam(code, number_of_bots):
	driver = webdriver.Firefox()
	
	for i in range(number_of_bots):
		driver.get(URL)
		while True:
			try:
				code_input = driver.find_element_by_class_name('check-room-input')
				code_input.send_keys(code)
				time.sleep(0.05)
				code_input.send_keys(Keys.RETURN)
				break
			except: pass

		while True:
			try:
				name_input = driver.find_element_by_class_name('enter-name-field')
				name_input.clear()
				name_input.send_keys(secrets.token_hex(4))
				time.sleep(0.05)
				name_input.send_keys(Keys.RETURN)
				break
			except: pass

		pag.hotkey('ctrl', 't')
		driver.switch_to.window(driver.window_handles[i+1])

		time.sleep(0.1)

if __name__ == '__main__':
	try:
		code = input(f'Enter code: {Fore.GREEN}')
		number_of_bots = int(input(f'Enter the number of bots to join: {Fore.GREEN}'))

		start_time = time.perf_counter()

		spam(code, number_of_bots)

		print(f'Time taken for {number_of_bots}: {time.perf_counter() - start_time}')
	except KeyboardInterrupt:
		print(f'{Fore.RESET}Quitting')
