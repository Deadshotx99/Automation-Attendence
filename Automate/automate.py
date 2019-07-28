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
login = driver.find_element(By.XPATH,'.//*[@id="Submit"]')
time.sleep(0.75)
login.click()
element1 = driver.find_element_by_link_text('Attendance')
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

button = driver.find_element(By.XPATH,'.//*[@id="MainContent_Button4"]')
button.click()

time.sleep(0.75)

sub0 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_0"]')
bysubject.append(sub0.text)
sub1 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_1"]')
bysubject.append(sub1.text)
sub2 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_2"]')
bysubject.append(sub2.text)
sub3 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_3"]')
bysubject.append(sub3.text)
sub4 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_4"]')
bysubject.append(sub4.text)
sub5 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_5"]')
bysubject.append(sub5.text)
sub6 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_6"]')
bysubject.append(sub6.text)
sub7 = driver.find_element(By.XPATH,'.//*[@id="MainContent_GridView4_lblid_7"]')
bysubject.append(sub7.text)

data = {'SUBJECT CODE': ['EID205', 'EID201', 'ECS201', 'ECS221', 'EMA203', 'EID221', 'EID203', 'EID223'],
        'SUBJECT NAME': ['D C', 'C + +', 'P L P', 'C E W', 'P S', 'C + + _ LAB', 'C O A', 'U N I X _ LAB'],
        ' ATTENDENCE ': bysubject,

        }
dframe = DataFrame(data)

print('\n')

print('B y   S u b j e c t  D e t a i l s :  ')

print('\n')


print(dframe)


driver.close()


















