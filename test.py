ssh -i <private key path> azureuser@52.182.129.185

sVQUQJYgZ.w%idGnHpw7haPJ&Pc)9U9*


import selenium as se
from selenium import webdriver
import time

options = se.webdriver.ChromeOptions()
options.add_argument('headless')
driver = se.webdriver.Chrome(options=options)
start = time.localtime()

driver.get('http://mtrack.merryspiders.com/NewsDetailsPublished.aspx?NewsId=e3E6Ggaq2uAX9SosCfBB7Q==&MediaType=')
time.sleep(5)
page= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]').text
text = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]').text
date= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]').text
publication= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublication"]').text
author= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblJournalist"]').text
headline= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]').text
print(date,'\n',publication,'\n',author,'\n',headline)
end = time.localtime()
print("Total execution time in seconds," '\n')
print(end.tm_sec - start.tm_sec)