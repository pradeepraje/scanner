
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
from timeit import default_timer as timer
from datetime import timedelta
from selenium.webdriver.common.by import By



#early definition
options = se.webdriver.ChromeOptions()
options.add_argument('headless')





def get_keywords(driver):
    #pass url and defined keyword processor
    data = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]').text
    lfound = list(set(keyword_processor.extract_keywords(data)))
    return (lfound)
    
def put_db(driver, dom,lfound):
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
    cur.execute(sql,data)

#Ends

#main block
#start = timer()
start=time.time()
keyword_processor = KeywordProcessor()
for item in ['Cairn Energy','Cairn plc','arbitration','retrospective tax','retro tax']:
	keyword_processor.add_keyword(item)
with sqlite3.connect('cairndb.db') as con:
    
    driver=se.webdriver.Chrome(options=options) 
    cur=con.cursor() # dbase cursor initialised    
    ibook = xlrd.open_workbook("cairn18.xls", formatting_info=True)
    for ix in [2,3]:
        isheet = ibook.sheet_by_index(ix)
        print(isheet.name, '\t', isheet.nrows)
        try:
            for row in range(isheet.nrows+1):
                
                if (isheet.cell_value(row,5).lower()=='english'):
                    link = isheet.hyperlink_map.get((row, 1))
                    url = '(No URL)' if link is None else link.url_or_path        
                    driver.get(url)
                    webpage=requests.get(url)
                    soup=BeautifulSoup(webpage.content, 'html.parser')
                    dom=etree.HTML(str(soup))
                    time.sleep(5)
                    lfound=get_keywords(driver)        
                    if (("Cairn Energy" or "Cairn plc" in lfound)) and (('arbitration' or 'retrospective tax' or 'retro tax' or 'tax demand' or 'tax notice')in lfound):  
                        put_db(driver,dom,lfound)                    
                if row%100==0:
                    print(row)
                    con.commit()
                    '''else:
                        continue
                else:
                    continue'''
            
        except:
            print("error at "+ isheet.name+'\t'+ str(row) + '\t'+isheet.cell_value(row,1))
        else:
            #print("For "+ str(row) +'\t'+ str(timedelta(seconds=timer()-start)))
            print("For "+ str(row) +'\t'+ str(time.time()-start))
        finally:
            con.commit()
            print("processing done")


    driver.quit() 
con.close()
print(timedelta(seconds=time.time()-start))
