library(tidyverse)
data <- starwars

sw <- data %>% 
  select(name, height, mass, gender) %>% 
  rename(weight = mass) %>% 
  na.omit() %>% 
  mutate(height = height/100) %>% 
  filter(gender == "masculine" | gender == "feminine") %>%  # gender %in% c("masculine", "feminine")
  mutate(gender = recode(gender,
                        masculine = "m",
                        feminine = "f")) %>% 
  mutate(size = height > 1 & weight > 75,
         size = if_else(size == TRUE, "big", "small"))

