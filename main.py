from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_options = Options()
arguments = [
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    '--start-maximized',
    '--disable-blink-features=AutomationControlled',
]

experimental_options = {
    'excludeSwitches': ['enable-automation', 'enable-logging'],
    'prefs': {'profile.default_content_setting_values.notifications': 2}
}

for argument in arguments:
    driver_options.add_argument(argument)

for key, value in experimental_options.items():
    driver_options.add_experimental_option(key, value)

s = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s, options = driver_options)

browse = driver.get('')

driver.find_element_by_name('').send_keys()
driver.find_element_by_css_selector("[type=submit]").click()
sleep(3)
driver.find_element_by_id("checkbox").click()