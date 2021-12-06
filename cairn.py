'''import io
from flashtext import KeywordProcessor
import sqlite3 as sq

keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)


#file open routine
with io.open("cairn1.txt", mode="r", encoding="utf-8") as fin:
    data=fin.read()


keywords_found = set(keyword_processor.extract_keywords(data))
print(keywords_found)


xpath for text: //*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]/div[3]/span
date: .xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text)
publication: .xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublication"]')[0].text
author: .xpath('//*[@id="ctl00_ContentPlaceHolder1_lblJournalist"]')[0].text)headline: .xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text

#to create db
import sqlite3
with sqlite3.connect('cairndb.db') as con:
    cur=con.cursor()
    table="""CREATE TABLE "cairn_table" (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT, -- rowid
                "date" TEXT,
                "publication" TEXT,
                "author" TEXT,
                "headline" TEXT,
                "items" TEXT                
            )
            """
    cur.execute(table)
    print ("created Cairn_table") 


'''
#module get element by xpath:
#============================
#imports segment
#from lxml import etree
import time,xlrd,sqlite3
#from bs4 import BeautifulSoup
from datetime import datetime
from flashtext import KeywordProcessor
import sqlite3
import selenium as se
from selenium import webdriver

#early definition
options = se.webdriver.ChromeOptions()
options.add_argument('headless')





def get_keywords(driver):
    #pass url and defined keyword processor
    data = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]').text
    lfound = list(set(keyword_processor.extract_keywords(data)))
    return (lfound)
    
def put_db(driver,lfound):
    # Writing to table
    try:
        datex= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]').text
        id_date=datetime.strftime(datetime.strptime(datex, '%d-%m-%Y'), '%Y-%m-%d')
        id_pub= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublication"]').text
        id_author= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblJournalist"]').text
        id_headline= driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]').text
        xfound=', '.join(lfound)
        sql = """INSERT INTO cairn_table(date, publication,author, headline, items) VALUES(?,?,?,?,?)"""
    except:
        data = ('*****', '*****','*****','*****','*****')
    else:
        data = (id_date, id_pub,id_author,id_headline, xfound)
    finally:
        cur.execute(sql,data)
    

#main block
#import pdb; pdb.set_trace()
keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)
with sqlite3.connect('cairndb.db') as con:
    driver=se.webdriver.Chrome(options=options) 
    cur=con.cursor() # dbase cursor initialised    
    ibook = xlrd.open_workbook("cairn18.xls", formatting_info=True)
    isheet = ibook.sheet_by_index(0)
    for row in range(5,11):
        link = isheet.hyperlink_map.get((row, 1))
        url = '(No URL)' if link is None else link.url_or_path        
        driver.get(url)
        time.sleep(5)

        lfound=get_keywords(driver)        
        if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax')in lfound):  
            put_db(driver,lfound)
        else:
            continue;
 
driver.close()
driver.quit() 
con.close() 

 