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
from lxml import etree
import time,xlrd,sqlite3, pickle,requests
from bs4 import BeautifulSoup
from datetime import datetime
from flashtext import KeywordProcessor
import pandas as pd
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
    
def put_db(driver, dom,lfound, out_frame):
    # Writing to table
    datex= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text
    id_date=datetime.strftime(datetime.strptime(datex, '%d-%m-%Y'), '%Y-%m-%d')
    id_pub= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublication"]')[0].text
    id_headline= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text
    xfound=', '.join(lfound)
    #for author field check
    if dom.xpath( '//*[@id="ctl00_ContentPlaceHolder1_lblJournalist"]'):
        id_author=dom.xpath( '//*[@id="ctl00_ContentPlaceHolder1_lblJournalist"]')[0].text
    elif  dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAgency"]'):
        id_author=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAgency"]')[0].text
    elif dom.xpath( '//*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]'):
        id_author=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]')[0].text
    else:
        id_author="*******"
    sql = """INSERT INTO cairn_table(date, publication,author, headline, items) VALUES(?,?,?,?,?)"""
    data = (id_date, id_pub,id_author,id_headline, xfound)
    out_frame.append(list(data))
    cur.execute(sql,data)
#Ends

#main block
start = time.localtime()
print(start.tm_sec)
keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)
with sqlite3.connect('cairndb.db') as con:
    out_frame=[]
    driver=se.webdriver.Chrome(options=options) 
    cur=con.cursor() # dbase cursor initialised    
    ibook = xlrd.open_workbook("cairn17.xls", formatting_info=True)
    isheet = ibook.sheet_by_index(0)
    for row in range(21):
        if (isheet.cell_value(row,5).lower()=='english'):
            link = isheet.hyperlink_map.get((row, 1))
            url = '(No URL)' if link is None else link.url_or_path        
            driver.get(url)
            webpage=requests.get(url)
            soup=BeautifulSoup(webpage.content, 'html.parser')
            dom=etree.HTML(str(soup))
            print(row)
            time.sleep(3)
            lfound=get_keywords(driver)        
            if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax' or 'tax demand' or 'tax notice')in lfound):  
                put_db(driver,dom,lfound,out_frame)
            else:
                continue
        else:
            continue
driver.close()
driver.quit() 
con.close() 
df = pd.DataFrame(out_frame, columns=['Date', 'publication','Author', 'Headline', 'Items'])
df.to_pickle('cairn.pkl')
end = time.localtime()
print("Total execution time in seconds," '\n')
print(end.tm_sec - start.tm_sec)
