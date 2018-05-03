# read data
bitcoin = read.csv('C:/Users/Magda/Desktop/Data An/PfBD/Project/bitcoin_clean_data.csv', header = TRUE)
# see summary
summary(bitcoin)
str(bitcoin)
#install.packages("tidyverse")
#library(tidyverse) 
library(tidyr)

#regression
subbi <- subset(bitcoin, select = c("Volume", "Ask"))
summary(subbi)
cor(subbi) 


#gg plots - Asking to Volume
ggplot(data=bitcoin) + 
  geom_point(mapping = aes(x = Volume, y = Ask, colour = Volume)) +
  coord_flip() +
  ggtitle("Volume to Asking Price Correlation")

#high price to bidding price
ggplot(data=bitcoin, aes(High, Bid)) + 
    geom_line(colour = "darkblue") +
    ylab("Bidding Price") + xlab("High Price")

# high price to low and bid price
ggplot(data=bitcoin, aes(High, Bid)) + 
  geom_line(colour = "darkblue") +
  geom_line(colour = " red", aes(Low)) +
  xlab("High Price")
