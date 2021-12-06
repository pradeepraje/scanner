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
date: //*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]
publication: //*[@id="ctl00_ContentPlaceHolder1_lblPublication"]
author: //*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]
headline: //*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]

#to create db
import sqlite3
with sqlite3.connect('cairndb') as con:
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
import requests,xlrd
from bs4 import BeautifulSoup
from datetime import datetime
from flashtext import KeywordProcessor
import sqlite3

#early definition
def get_text(url):
    #pass url and defined keyword processor
    webpage = requests.get('https'+url.lstrip('http'))
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    text=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]/div[3]/span')[0].text
    lfound = list(set(keyword_processor.extract_keywords(data)))
    return (lfound)
    
def put_db(lfound):
    # Writing to table

    datex=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text
    id_date=datetime.strftime(datetime.strptime(datex, '%d-%m-%Y'), '%Y-%m-%d')
    id_pub=dom.xpath(' //*[@id="ctl00_ContentPlaceHolder1_lblPublication"]')[0].text
    id_author= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]')[0].text
    id_headline= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text
    sql = """INSERT INTO cairn_table(date, publication,author, headline, items) VALUES(?,?,?,?,?)"""
    data = (id_date, id_pub,id_author,id_headline, lfound)
    cur.execute(sql,data)
    #con.commit()


#main block
#import pdb; pdb.set_trace()
keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)
with sqlite3.connect('cairndb') as con:
    cur=con.cursor() # dbase cursor initialised    
    ibook = xlrd.open_workbook("cairn18.xls", formatting_info=True)
    isheet = ibook.sheet_by_index(0)
    for row in range(1,11):
        link = isheet.hyperlink_map.get((row, 1))
        url = '(No URL)' if link is None else link.url_or_path
        print(url)
        lfound=get_text(url)        
        if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax')in lfound):  
            put_db(lfound)
        else:
            continue
    