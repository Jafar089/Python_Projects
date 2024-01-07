#Facobook login using python program

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
email_id=input("Enter your email id! ")
password=input("Enter your password! ")
server=webdriver.Chrome(ChromeDriverManager().install())
server.get('https://www.facebook.com/syed.sherazi.79462')
username=server.find_element_by_id('pass')
passw.send_keys(password)
login=server.find_element_by_id('loginbutton')
login.click()
server.quit()