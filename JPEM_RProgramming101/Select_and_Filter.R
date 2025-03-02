library(tidyverse)
# Working with R built-in datasets

# Body Mass Index (BMI) mass(kg) / height (m2)
# Working with the height and mass of various Star Wars characters (humans)
# Identify differences between male and female characters

df <- starwars

head(df)

df %>%
  select(gender, mass, height, species) %>% 
  filter(species == "Human") %>% 
  na.omit() %>% 
  mutate(height = height/100) %>% 
  mutate(BMI = mass / height ^2) %>% 
  group_by(gender) %>% 
  summarise(Average_BMI = mean(BMI))

