import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


email, passwd = sys.argv[1:]
#1.open browser
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1000, 720)
driver.get("https://game.maj-soul.net/1/")
print('Loading...')
sleep(10)

#2.input email
screen = driver.find_element(By.ID, 'layaCanvas')
ActionChains(driver)\
    .move_to_element_with_offset(screen, 250, -100)\
    .click()\
    .perform()
driver.find_element(By.NAME, 'input').send_keys(email)
print('Input email successfully')

#3.input password
ActionChains(driver)\
    .move_to_element_with_offset(screen, 250, -50)\
    .click()\
    .perform()
driver.find_element(By.NAME, 'input_password').send_keys(passwd)
print('Input password successfully')

#4.login
ActionChains(driver)\
    .move_to_element_with_offset(screen, 250, 50)\
    .click()\
    .perform()
print('Entering game...')
sleep(20) #loading...
print('Login success')
driver.quit()
