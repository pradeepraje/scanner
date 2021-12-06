import requests
from lxml import etree
from bs4 import BeautifulSoup



url='https://mtrack.merryspiders.com/NewsDetailsPublished.aspx?NewsId=LL4TnLrpK34t5Zo2DiVMpA==&MediaType='
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
text=(dom.xpath('//*[@id="ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews"]/div[3]/span')[0].text)
print(text)

url='https://mtrack.merryspiders.com/NewsDetailsPublished.aspx?NewsId=e3E6Ggaq2uAX9SosCfBB7Q==&MediaType='
webpage=requests.get(url)
soup=BeautifulSoup(webpage.content,'html.parser')
dom=lxml.etree.HTML(str(soup))
print(dom.xtree.get_element_by_id("ctl00_ContentPlaceHolder1_TabContainer1_TabPanel2_lblNews").text_content())