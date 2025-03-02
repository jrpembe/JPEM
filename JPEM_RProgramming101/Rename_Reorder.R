library(tidyverse)
data <- starwars
head(data)

data <- data %>% 
  select(name, gender, mass, height, hair_color) %>% 
  filter(mass < 400) %>% 
  rename(weight = mass) %>% 
  mutate(gender = recode(gender, "masculine" = "male", "feminine" = "female"))

head(data)


plot(data$height, data$weight)

