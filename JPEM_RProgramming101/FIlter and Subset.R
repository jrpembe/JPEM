library(tidyverse)

df <- msleep

head(df)

# filter using a logical condition
df <- df %>% 
  select(name, sleep_total) %>% 
  filter(!sleep_total > 18)


# filter using "and", "or"
my_data <- msleep %>% 
  select(name, order, bodywt, sleep_total) %>% 
  filter(order == "Primates" | bodywt > 20) # you can use , instead of & - use | for "or

# filter using "in"
my_data2 <- msleep %>% 
  select(name, sleep_total) %>% 
  filter(name %in% c("Cow", "Dog", "Horse"))

# filter usnig "between"
my_data3 <- msleep %>% 
  select(name, sleep_total) %>% 
  filter(between(sleep_total, 16, 18))

# filter using "near"
my_data4 <- msleep %>% 
  select(name, sleep_total) %>% 
  filter(near(sleep_total, 17, tol=0.5)) # must be within 0.5 of 17

# filter using presence of "na"
my_data5 <- msleep %>% 
  select(name, conservation, sleep_total) %>% 
  filter(!is.na(conservation)) # rows that do not have NA for conservation 
