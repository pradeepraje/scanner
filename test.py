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




library(RSQLite)
library(DBI)
dba <- read.csv("tempa.csv")


df_1 %>%
  group_by(Year, Month) %>%
  summarise(count= n()) 
  
   barplot(by_year$n, axes=FALSE, col=rainbow(10))
   
jpeg('d:/raje/bert/by_year.jpg',width = 6, height = 4, unit="in", res=300)  
xx=barplot(by_year$n, axes=FALSE, ylim= c(0,max(by_year$n+200)),xlab="Year-wise count", col=rainbow(10), names.arg=c("2015","2016","2017","2018","2019","2020","2021"))
text(x = xx, y = by_year$n+10, label = by_year$n, pos = 3, cex = 1.0, col = "black")
dev.off()

library(dplyr)
by_month<-temp %>% count(MY)

#jpeg('d:/raje/bert/by_month.jpg',width = 6, height = 4, unit="in", res=300)  
xx=barplot(by_month$n,  ylim= c(0,max(by_month$n+10)),xlab="Month-wise distribution", col="#2E9FDF", names.arg=c("2015",rep('',11),"2016",rep('',35),"2017",rep('',11),"2018",rep('',11),"2019",rep('',11),"2020",rep('',11),"2021"))
text(x = xx, y = by_year$n+10, label = by_year$n, pos = 3, cex = 1.0, col = "black")
dev.off()


barplot(by_month$n,ylim= c(0,max(by_month$n+10)),xlab="Month-wise distribution", col=rainbow(20))

x<-barplot(by_month$n,beside=TRUE,col=rep(c("red","blue","green","yellow","magenta","pink","maroon"),each=12))
axis(1, at=x, label=c("2015",rep('',12),"2016",rep('',12),"2017",rep('',12),"2018",rep('',12),"2019",rep('',12),"2020",rep('',12),"2021",rep("",2)),cex.axis=0.8)

x<-barplot(by_month$n,beside=TRUE,col=rep(c("red","blue","green","yellow","magenta","pink","maroon"),each=12),xaxt='n')
axis(1, at=x, label=c("2015",rep('',12),"2016",rep('',12),"2017",rep('',12),"2018",rep('',12),"2019",rep('',12),"2020",rep('',12),"2021",rep("",2)),cex.axis=0.8,las=1)


> 
> axis(1, at=x, label=c("2015",rep('',12),"2016",rep('',12),"2017",rep('',12),"2018",rep('',12),"2019",rep('',12),"2020",rep('',12),"2021",rep("",2)),cex.axis=0.8,las=2)
> axis(1, at=x, label=c("2015",rep('',12),"2016",rep('',12),"2017",rep('',12),"2018",rep('',12),"2019",rep('',12),"2020",rep('',12),"2021",rep("",2)),cex.axis=0.8,las=2,tck=0.1)
> axis(1, at=x, label=c("2015",rep('',12),"2016",rep('',12),"2017",rep('',12),"2018",rep('',12),"2019",rep('',12),"2020",rep('',12),"2021",rep("",2)),cex.axis=0.8,las=2)
> 


x<-barplot(by_month$n,beside=TRUE,col=rep(c("red","blue","green","yellow","magenta","pink","maroon"),each=12),xaxt='n')
axis(1, at=x, label=c("2015",rep('',51),"2019",rep('',51),"2021",rep("",2)),tick=FALSE,cex.axis=0.8, las=2)

&lt;-c(6,9,11,13,15)
#create dataframe
data=data.frame(x=LETTERS[1:5], y=y)
#set up labels



yat<-c("","50","100","150","200","250","300")

p2 <- ggplot(by_pub10, aes(x = reorder(Category, -Count), y = Count),label=y) +
    geom_segment( aes(x=x, xend=x, y=0, yend=y), color="magenta",size=4) +
    theme_bw()+ scale_x_reverse()+
      coord_flip()+ 
      #geom_text(aes(x = reorder(Category, -Count), y = Count,label=y))+
       annotate("text", x = 1.225:10.225, y =3.01, label = xat, size=4,hjust=0.05,family="serif",fontface =2)+ 
       theme(
     panel.grid.minor.x = element_blank(),
     panel.grid.minor.y = element_blank(),
     panel.border = element_blank(),
     axis.line=element_blank(),
     axis.title.x=element_blank(),
     axis.title.y=element_blank(), 
       axis.text.y=element_blank(),
     axis.ticks.y=element_blank())+
     theme(axis.line.x = element_line(color = "black"), axis.line.y = element_line(color = "black")
     )
     
    jpeg('by_publi.jpg',res=300,width=6, height=4, unit='in')
    plot(p2)
    dev.off()
    
    