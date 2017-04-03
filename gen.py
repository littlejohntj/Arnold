import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def verifyPhone():
    phoneField = browser.find_element_by_id('id_phone_number')
    for number in phone:
        phoneField.send_keys(number)
        time.sleep(random.choice(nums))
    time.sleep(random.choice(nums2))
    browser.find_element_by_class_name('button-green').click()

email='7assdfs8dygu3@gmail.com'
fullName='The Kid'
userName='cdsidg89sm832u'
password='Password123!'
phone='+19542801018'

nums = [0.4,1.1,1.8,2.4,3.2]
nums2 = [6,8,9,10,12]

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

time.sleep(random.choice(nums))

#Get sign up form fields
form = browser.find_element_by_class_name('_3bqd5')
formFields = browser.find_elements_by_class_name('_qy55y')

emailField = formFields[0]
for letter in email:
	emailField.send_keys(letter)
	time.sleep(random.choice(nums))
time.sleep(random.choice(nums))

nameField = formFields[1]
for letter in fullName:
	nameField.send_keys(letter)
	time.sleep(random.choice(nums))
time.sleep(random.choice(nums))

userNameField = formFields[2]
formFields[2].clear()
for letter in userName:
	userNameField.send_keys(letter)
	time.sleep(random.choice(nums))
time.sleep(random.choice(nums))

passwordField = formFields[3]
for letter in password:
	passwordField.send_keys(letter)
	time.sleep(random.choice(nums))
time.sleep(random.choice(nums2))

browser.find_elements_by_class_name('_1on88')[1].click()
time.sleep(10)

try:
    verifyPhone()
except NoSuchElementException:
    time.sleep(10)
    browser.quit()

    


