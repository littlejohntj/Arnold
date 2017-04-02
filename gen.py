import time
from selenium import webdriver

#email=raw_input('Email: ')
#fullName=raw_input('Full Name: ')
#userName=raw_input('Username: ')
#password=raw_input('Password: ')

email='o1367179@mvrht.com'
fullName='Alice Bulb'
userName='bearupdown123b'
password='Password123!'

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

time.sleep(5)

#Get sign up form fields
form = browser.find_element_by_class_name('_3bqd5')
formFields = browser.find_elements_by_class_name('_qy55y')

emailField = formFields[0]
emailField.send_keys(email)
time.sleep(2)

nameField = formFields[1]
nameField.send_keys(fullName)

userNameField = formFields[2]
userNameField.send_keys(userName)
time.sleep(3)

passwordField = formFields[3]
passwordField.send_keys(password)
time.sleep(4)

browser.find_elements_by_class_name("_1on88")[1].click()

#search_box = browser.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()


#time.sleep(3) #sleep for 3 seconds


time.sleep(5)
#browser.quit()



