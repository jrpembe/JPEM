library(tidyverse)

df<- read_xlsx("./data/friends.xlsx")
head(df)

# str shows the data types in your file
str(df)

# TASKS:
# we want age to be an integer, height & weight can remain numeric (Numeric / Integer)
# chr = character, or string. We need the height data to be in order, or ordinal (factor)
# first lets create the height categories 

df <- df %>%
  mutate(height_category = case_when(
    Height < 1.78 ~ "Short",
    Height >= 1.78 & Height < 1.80 ~ "Medium",
    Height >= 1.80 ~ "Tall"
  ))


df$height_category <- as.factor(df$height_category)
df$Age <- as.integer(df$Age)

# change levels to be in order, not alphabetical
levels(df$height_category)
df$height_category <- factor(df$height_category,
                             levels = c("Short", "Medium", "Tall"))

# Logical Variables
df$old <- df$Age > 23
