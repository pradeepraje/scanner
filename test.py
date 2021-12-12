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

import sqlite3
con3 = sqlite3.connect("combine.db")

con3.execute("ATTACH 'results_a.db' as dba")

con3.execute("BEGIN")
for row in con3.execute("SELECT * FROM dba.sqlite_master WHERE type='table'"):
    combine = "INSERT INTO "+ row[1] + " SELECT * FROM dba." + row[1]
    print(combine)
    con3.execute(combine)
con3.commit()
con3.execute("detach database dba")


attach 'c:\test\b.db3' as toMerge;           
BEGIN; 
insert into AuditRecords select * from toMerge.AuditRecords; 
COMMIT; 
detach toMerge;