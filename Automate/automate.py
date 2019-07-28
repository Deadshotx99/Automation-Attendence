from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
from pandas import DataFrame

BANNER = r'''

     _        _   _     _____      ___      __  __        _        _____     ___      ___      _   _     _ 
    / \      | | | |   |_   _|    / _ \    |  \/  |      / \      |_   _|   |_ _|    / _ \    | \ | |   | |
   / _ \     | | | |     | |     | | | |   | |\/| |     / _ \       | |      | |    | | | |   |  \| |   | |  
  / ___ \    | |_| |     | |     | |_| |   | |  | |    / ___ \      | |      | |    | |_| |   | |\  |   |_|  
 /_/   \_\    \___/      |_|      \___/    |_|  |_|   /_/   \_\     |_|     |___|    \___/    |_| \_|   (_) '''


print(BANNER)

driver = webdriver.Chrome()
driver.get('https://login.gitam.edu/Login.aspx')

#login_details
file = open('logindetails.txt','r+')
content = file.readlines()
file.close()

#login_procedure
email = driver.find_element(By.XPATH,'.//*[@id="txtusername"]')
email.send_keys(content[0])
password = driver.find_element(By.XPATH,'.//*[@id="password"]')
password.send_keys(content[1])



element1 = driver.find_element_by_xpath('.//*[@id="MainContent_ad"]/a/h5')

element1.click()

time.sleep(3)
element2 = driver.find_element(By.XPATH,'.//*[@id="MainContent_lbltotal"]')

print('\n')

print('F e t c h i n g  T o T a l  A t t e n d e n c e ...')

print("\n")

print("Y o u r  T o T a l  A t t e n d e n c e  is : ",element2.text)

print("\n")

print('F e t c h i n g  B y  S u b j e c t   A t t e n d e n c e ...')

bysubject = []
subjectcode = []
subjects = []

button = driver.find_element(By.XPATH,'.//*[@id="MainContent_Button4"]')
button.click()

time.sleep(0.75)

#subjectcode
temp1 = './/*[@id="MainContent_GridView4"]/tbody/tr['
for x in range(2,10):
    sub1 = temp1 + str(x)+']/td[1]'
    k = driver.find_element_by_xpath(sub1)
    subjectcode.append(k.text)


#subjectname
temp2 = './/*[@id="MainContent_GridView4"]/tbody/tr['
for x in range(2,10):
    sub2 = temp2 + str(x)+']/td[2]'
    j = driver.find_element_by_xpath(sub2)
    subjects.append(j.text)

#by_subject_attendence
temp3 = './/*[@id="MainContent_GridView4_lblid_'
for x in range(0,8):
    sub3 = temp3 + str(x)+'"]'
    l = driver.find_element_by_xpath(sub3)
    bysubject.append(l.text)






print('\n')

print('B y   S u b j e c t  D e t a i l s :  ')

print('\n')

data = {'SUBJECT CODE': subjectcode,
        'SUBJECT NAME': subjects,
        ' ATTENDENCE ': bysubject,

        }

dframe = DataFrame(data)

print(dframe)

























