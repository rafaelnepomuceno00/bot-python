from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path='/home/rafael/Documentos/geckodriver-v0.28.0-linux64/geckodriver')

    def login(self):
        driver = self.driver
        driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(4)
        userfield = driver.find_element_by_xpath('//input[@name="username"]')
        userfield.click()
        userfield.clear()
        userfield.send_keys(self.userName)
        pswdfield = driver.find_element_by_xpath("//input[@name='password']")
        pswdfield.click()
        pswdfield.clear()
        pswdfield.send_keys(self.password)
        pswdfield.send_keys(Keys.RETURN)
        time.sleep(5)

    @staticmethod
    def typing(phrase, wheretype):
        for letters in phrase:
            wheretype.send_keys(letters)
            time.sleep(random.randint(1, 5)/30)

    def coment(self):
        driver = self.driver
        driver.get("link do post")
        time.sleep(4)
        driver.execute_script('window.scrollTo(0,300);')

        for i in range(0, 1000):
            try:
                coments = ['Quero ganhar!', 'Contando com a sorte', 'Qualquer Coisa', 'Comentando','Vou ganhar', 'Já ganhei!', 'Quero', 'Espero muito ganhar', 'Tentando', 'Não custa nada tentar',
                           'Quero muito!', 'Espero ganhar!', '$$$', '$','$$','$$$', '$$$$$', '$$$$', '$$$$$$$$$$$$$' '$$$$$$' '$$$$$$$']
                driver.find_element_by_class_name("Ypffh").click()
                comentfield = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(4, 10))
                self.typing(random.choice(coments), comentfield)
                time.sleep(random.randint(15, 40))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Post')]").click()
                time.sleep(random.randint(4, 10))
                driver.get("link do post")
                time.sleep(random.randint(4, 10))
                driver.execute_script('window.scrollTo(0,300);')

                print(i)
            except Exception as e:
                print('erro: ')
                print(i)
                print(e)
                time.sleep(2)


bot = InstagramBot('user', 'senha')
bot.login()
time.sleep(5)
bot.coment()
