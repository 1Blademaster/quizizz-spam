import os
import secrets
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

init(autoreset=True)

URL = 'https://quizizz.com/join'

def spam(code, number_of_bots, headless):
	if headless:
		options = webdriver.FirefoxOptions()
		options.headless = True
		driver = webdriver.Firefox(options=options)
	else:
		driver = webdriver.Firefox()
	
	for i in range(number_of_bots):
		driver.switch_to.window(driver.window_handles[i])
		driver.get(URL)
		while True:
			try:
				code_input = driver.find_element_by_class_name('check-room-input')
				code_input.send_keys(code)
				time.sleep(0.05)
				code_input.send_keys(Keys.RETURN)
				break
			except:
				time.sleep(0.25)

		while True:
			try:
				name_input = driver.find_element_by_class_name('enter-name-field')
				name_input.clear()
				time.sleep(0.1)
				name_input.send_keys(secrets.token_hex(4))
				time.sleep(0.05)
				name_input.send_keys(Keys.RETURN)
				break
			except:
				time.sleep(0.25)

		driver.execute_script(f'''window.open("{URL}","_blank");''')

		time.sleep(0.1)

if __name__ == '__main__':

	try:
		code = input(f'Enter code: {Fore.GREEN}')
		print(Fore.RESET)
		number_of_bots = int(input(f'Enter the number of bots to join: {Fore.GREEN}'))
		print(Fore.RESET)
		number_of_threads = int(input(f'Enter the number of threads to use: {Fore.GREEN}'))
		print(Fore.RESET)

		start_time = time.perf_counter()

		threads = []
		for i in range(number_of_threads):
			t = threading.Thread(target=spam, args=(code, (number_of_bots // number_of_threads), False,))
			threads.append(t)
			t.start()

		for idx, thread in enumerate(threads):
			thread.join()

		print(f'Time taken for {number_of_bots}: {time.perf_counter() - start_time}')
	except KeyboardInterrupt:
		print(f'{Fore.RESET}Quitting')

	os.system('taskkill /F /IM firefox.exe')
	print('\nClosed all instances of firefox.exe')
