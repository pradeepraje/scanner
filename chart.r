

by_author<-temp %>% count(author)
Category=by_author$authorCount=by_author$n
p3 <- ggplot(by_pub10, aes(x = reorder(Category, -Count), y = Count),label=y) +
     geom_segment( aes(x=x, xend=x, y=0, yend=y), color="limegreen",size=4) +
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
    
     plot(p3)
     

Category=by_auth10$author
Count=by_auth10$n

p4 <- ggplot(by_auth10, aes(x = reorder(Category, -Count), y = Count),label=y) + ylim(0,40)+ ylab("No. of stories")+
     geom_segment( aes(x=x, xend=x, y=0, yend=Count), color="lawngreen",size=4) + xlab("")+
     theme_bw()+ scale_x_reverse()+
       coord_flip()+ 
        annotate("text", x = 1.225:10.225, y =1.01, label = xat, size=4,hjust=0.05,family="sans",fontface =2)+ 
        theme(
      panel.grid.minor.x = element_blank(),
      panel.grid.minor.y = element_blank(),
      panel.border = element_blank(),
      axis.line=element_blank(),
      #axis.title.x=element_blank(),
      #axis.title.y=element_blank(), 
        axis.text.y=element_blank(),
      axis.ticks.y=element_blank())+
      theme(axis.line.x = element_line(color = "black"), axis.line.y = element_line(color = "black")
      )
    
     plot(p4)
     
	 
	 jpeg("by_author.jpg",res=300, height=4, width=6, units="in")
	 plot(pr)
	 dev.off()
	 
