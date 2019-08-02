from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
from pandas import DataFrame
import pyttsx3

audio1 = pyttsx3.init()
audio2 = pyttsx3.init()
audio3 = pyttsx3.init()
audio4 = pyttsx3.init()
audio5 = pyttsx3.init()
name   = pyttsx3.init()


BANNER = r'''

     _        _   _     _____      ___      __  __        _        _____     ___      ___      _   _     _ 
    / \      | | | |   |_   _|    / _ \    |  \/  |      / \      |_   _|   |_ _|    / _ \    | \ | |   | |
   / _ \     | | | |     | |     | | | |   | |\/| |     / _ \       | |      | |    | | | |   |  \| |   | |  
  / ___ \    | |_| |     | |     | |_| |   | |  | |    / ___ \      | |      | |    | |_| |   | |\  |   |_|  
 /_/   \_\    \___/      |_|      \___/    |_|  |_|   /_/   \_\     |_|     |___|    \___/    |_| \_|   (_) '''


print(BANNER)

#login_details

print('\n')

file = open('logindetails.txt','r+')
content = file.readlines()

if(content == []):
    print('E N T E R  Y O U R  L O G I N  D E T A I L S : ')

    print('\n')

    detail1 = input('R E G I S T R A T I O N  I D :')
    print('\n')
    detail2 = input('P A S S W O R D :')
    file.write(detail1+"\n"+detail2)
    file = open('logindetails.txt','r+')
    temp = file.readlines()
    file.close()


else:

    file = open('logindetails.txt','r+')
    temp = file.readlines()


    file.close()





driver = webdriver.Chrome()
driver.get('https://login.gitam.edu/Login.aspx')



#login_procedure
email = driver.find_element(By.XPATH,'.//*[@id="txtusername"]')
email.send_keys(temp[0])
password = driver.find_element(By.XPATH,'.//*[@id="password"]')
password.send_keys(temp[1])

print('\n')

print('F e t c h i n g  T o T a l  A t t e n d e n c e ...')


time.sleep(0.5)
submit = driver.find_element_by_xpath('.//*[@id="Submit"]')
submit.click()

Name = driver.find_element_by_xpath('.//*[@id="lblinf"]')
name.say('Hello'+ Name.text)
#Attendance_link
element1 = driver.find_element_by_xpath('.//*[@id="MainContent_ad"]/a/h5')

element1.click()

time.sleep(0.5)
element2 = driver.find_element(By.XPATH,'.//*[@id="MainContent_lbltotal"]')

print("\n")

aud = element2.text

print("Y o u r  T o T a l  A t t e n d e n c e  is : ",element2.text)


audio1.say("Your Total Attendence is  "+ aud)
audio1.runAndWait()

audio2.say("Fetching your Attendence of Each subject")
audio2.runAndWait()

audio3.say('it will take just a moment ')
audio3.runAndWait()




bysubject = []



subjectcode = []

subjects = []

button = driver.find_element(By.XPATH,'.//*[@id="MainContent_Button4"]')
button.click()

print("\n")

print('F e t c h i n g  B y  S u b j e c t   A t t e n d e n c e ...')




count = driver.find_elements_by_xpath('.//*[@id="MainContent_GridView4"]/tbody/tr/td[2]')
count = len(count)


# subjectcode
temp = driver
temp1 = './/*[@id="MainContent_GridView4"]/tbody/tr['
for x in range(2, (count + 2)):
    sub1 = temp1 + str(x) + ']/td[1]'
    k = driver.find_element_by_xpath(sub1)
    subjectcode.append(k.text)

# subjectname
temp2 = './/*[@id="MainContent_GridView4"]/tbody/tr['
for x in range(2, (count + 2)):
    sub2 = temp2 + str(x) + ']/td[2]'
    j = driver.find_element_by_xpath(sub2)
    subjects.append(j.text)

#by_subject_attendence
temp3 = './/*[@id="MainContent_GridView4_lblid_'
for x in range(0,count):
    sub3 = temp3 + str(x)+'"]'
    l = driver.find_element_by_xpath(sub3)
    bysubject.append(l.text)


print('\n')

print('B y   S u b j e c t  D e t a i l s :  ')

audio4.say('Your Attendence by Each Subject is Displayed below ')
audio4.runAndWait()
audio5.say('Thank you')
audio5.runAndWait()

print('\n')

data = {'S U B J E C T C O D E': subjectcode,
        'S U B J E C T  N A M E ': subjects,
        ' A T T E N D E N C E ': bysubject,
        }

dframe = DataFrame(data)

print(dframe)

driver.close()






























