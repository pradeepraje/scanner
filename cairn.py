import io
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


module get element by xpath:
============================
#imports segment
from lxml import etree
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flashtext import KeywordProcessor

#early definition
keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)

def get_text(url,keyword_processor):
    #pass url and defined keyword processor
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    text=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text
    lfound = list(set(keyword_processor.extract_keywords(data)))
    return (lfound)
    
def do_db(lfound, cur):
    # Writing to table
    try:
        datex=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text
        id_date=datetime.strftime(datetime.strptime(datex, '%d-%m-%Y'), '%Y-%m-%d'))
        id_pub=dom.xpath(' //*[@id="ctl00_ContentPlaceHolder1_lblPublication"]')[0].text
        id_author= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]')[0].text
        id_headline= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text
        sql = """INSERT INTO cairndb(date, publication,author, headline, items) VALUES(?,?,?,?,?)"""
        data = (id_date, id_pub,id_author,id_headline, lfound)
        cur.execute(sql,data)
        #con.commit()
    else:
        sql = """INSERT INTO cairndb(date, publication,author, headline, items) VALUES(?,?,?,?,?)"""
        data = ('*****', '*****','*****','*****', '*****')
        cur.execute(sql,data)
        #con.commit()

    

with sq.connect("cairndb.db") as con:
    cur = con.cursor()    
    if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax')in lfound):  
        do_db(lfound,cur)
    