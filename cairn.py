import io
from flashtext import KeywordProcessor
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

from lxml import etree
import requests,
from bs4 import BeautifulSoup
from datetime import datetime


#pass url
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
text=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text

lfound = list(set(keyword_processor.extract_keywords(data)))

if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax')in lfound):
    datex=dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text
    id_date=datetime.strftime(datetime.strptime(datex, '%d-%m-%Y'), '%Y-%m-%d'))
    id_pub=date: dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblNewsDate"]')[0].text
    id_publication=dom.xpath(' //*[@id="ctl00_ContentPlaceHolder1_lblPublication"]')[0].text
    id_author= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblAuthor"]')[0].text
    id_headline= dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_lblHeadline"]')[0].text

