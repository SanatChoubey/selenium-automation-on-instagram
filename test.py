import bs4
import requests
import lxml
from time import sleep
from selenium import webdriver
##https://en.wikipedia.org/wiki/Machine_learning/'/usr/local/bin/chromedriver'
##response=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
driver=webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)


select= driver.find_element_by_name('username')
select.send_keys('sanat_choubey')
sleep(3)
select2= driver.find_element_by_name('password')
select2.send_keys('sanatc12345')
sleep(3)
select2.submit()
sleep(5)
driver.get('https://www.instagram.com/music.love.quotes/')
sleep(5)
soup= bs4.BeautifulSoup(driver.page_source,'lxml')
tittle=soup.select('h1')




print(tittle[0].getText())




select3= driver.find_element_by_xpath('//ul[@class="k9GMp "]/li[3]/a')
select3.click()


sleep(3)

#//li[@class="wo9IH"][1]/div/div[2]/button
driver.get('https://www.instagram.com/music.love.quotes/following/')

sleep(3)

select4= driver.find_element_by_xpath('//li[@class="wo9IH"][1]/div/div[2]/button')
select4.click()
