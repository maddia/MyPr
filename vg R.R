# read data from dataset
vg = read.csv('C:/Users/Magda/Desktop/Data An/PfBD/Project/video_clean_data.csv')
# see summary of dataset
summary(dat)
# simple plot of Genre by Year
plot(vg$Year,vg$Genre, col='magenta', main="Rank over Years", xlab="Years", ylab="Rank" )
#ANOVA
anova <- aov(Global_Sales~Platform, data=vg)
summary(anova)

#regression
subvg <- subset(vg, select = c("JP_Sales", "Global_Sales"))
summary(subvg)
cor(subvg) 
plot(subvg, col='magenta')
# use a library (tidyr together with ggplots)
library(tidyr)
# gg plots showwing Genre of most selling games
ggplot(data = vg) + 
  geom_bar(mapping = aes(x = Genre, colour = Genre))
#gg plots showing Platform on which games were sold
ggplot(data = vg) + 
  geom_bar(mapping = aes(x = Platform, fill = Platform))
# by Genre in Nothern America
ggplot(data=vg, aes(x=Genre, y=NA_Sales, colour = Genre)) + 
  stat_summary(fun.y=sum, geom="bar", position="stack") +
  coord_flip() +
  ggtitle("Sales in North America by Genre")
# by Genre in Europe
ggplot(data=vg, aes(x=Genre, y=EU_Sales, colour = Genre)) + 
  stat_summary(fun.y=sum, geom="bar", position="stack") +
  coord_flip() +
  ggtitle("Sales in Europe by Genre")
# by Genre in Japan
ggplot(data=vg, aes(x=Genre, y=JP_Sales, colour = Genre)) + 
  stat_summary(fun.y=sum, geom="bar", position="stack") +
  coord_flip() +
  ggtitle("Sales in Japan by Genre")
# by Genre in Other Countries
ggplot(data=vg, aes(x=Genre, y=Other_Sales, colour = Genre)) + 
  stat_summary(fun.y=sum, geom="bar", position="stack") +
  coord_flip() +
  ggtitle("Sales ies by Genre")
# by Genre Global Sales
ggplot(data=vg, aes(x=Genre, y=Global_Sales, colour = Genre)) + 
  stat_summary(fun.y=sum, geom="bar", position="stack") +
  coord_flip() +
  ggtitle("Sales by Genre")




