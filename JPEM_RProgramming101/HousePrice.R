library(tidyverse)
library(ggpmisc)

df <- read.csv('./data/HousePrices.csv')
# head(df)
# tail(df)
# summary(df)
# View(df)

#plot(df$area, df$price)

ggplot(df, aes(x = area, y = price)) +
  geom_point() +
  geom_smooth(method="lm", se=FALSE, color="red") +
  stat_poly_eq(aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               formula = y ~ x, 
               parse = TRUE) +
  labs(title = "Scatterplot of Area vs Price",
       x = "Area (sq ft)",
       y = "Price ($)") +
  theme_minimal()
