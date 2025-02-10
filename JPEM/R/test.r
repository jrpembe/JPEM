library(tidyverse)
library(plotly)
str(mtcars)

mtcars %>%
  ggplot(aes(mpg, wt, color = "red", size = 5)) +
  geom_point() +
  labs(
       title = "Cars: Mileage vs Weight",
       x = "Miles Per Gallon",
       y = "Weight") +
  theme_minimal()


df <- read_csv("C:/JPEM_Git_Main/JPEM/JPEM/data/penguins.csv")
str(df)

df %>% na.omit(df) %>%
  ggplot(aes(island, fill = sex)) +
  geom_bar() +
  labs(
       title = "Penguins",
       x = "Species",
       y = "Body Mass (g)") +
  theme_minimal()

p <- df %>% na.omit(df) %>%
  ggplot(aes(bill_length_mm, flipper_length_mm, col = species, alpha=0.5)) +
  geom_point() +
  geom_smooth(method = lm, se = FALSE) +
  labs(
       title = "Penguin Data",
       x = "Bill Length (mm)", 
       y = "Flipper Length (mm)")

ggplotly(p)
