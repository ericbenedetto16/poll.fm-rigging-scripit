from selenium import webdriver
from time import sleep

while(1==1):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    #Replace POLL_URL with https://poll.fm/POLL_NUMBER
    driver.get('POLL_URL')

    #Replace POLL_ANSWER_ID with Radio Id Attribute: PDI_answerXXXXXX
    name = driver.find_element_by_id('POLL_ANSWER_ID')
    name.click()

    #l-link is the Div Which Holds the Vote Button
    submit = driver.find_element_by_class_name('l-link')
    submit.click()

    driver.close();
