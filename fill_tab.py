from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://vug.dosi-in.com/vug-2021-dh-thuong-mai-bai-du-thi-vong-loai-2-dance-battle-ha-noi?fbclid'
        '=IwAR0gEEgGQ4yGFwCRB9HEdAmXToMnpGOVFFGE-pu36kIgr1g8FiYViA7cSbQ')

time.sleep(2)

nameFill = "tuancong"
name = web.find_element_by_xpath('//*[@id="name-vote"]')
name.send_keys(nameFill)

phoneFill = "0968259116"
phone = web.find_element_by_xpath('//*[@id="phone"]')
phone.send_keys(phoneFill)

emailFill = "tuan.dc@urbox.vn"
email = web.find_element_by_xpath('//*[@id="email-vote"]')
email.send_keys(emailFill)