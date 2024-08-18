# **********************************************************************************
# file: Baseball Analysis.R
# Author: Jason Pemberton
# Date: August 1, 2024

# Purpose: This script runs the analysis to validate the 538 ELO MLB model and other
# models for predicting who will win individual baseball games.
# **********************************************************************************

library(tidyverse)
library(lubridate)


# We will add filters to screen out games that had not been played as of the date of creation of this file
game_data <- read_csv(file="C:/JPEM_Git_Main/JPEM/JPEM_Riffomonas/mlb-elo/mlb_elo.csv",
                      col_types = cols(date=col_date(),
                                       season=col_integer(),
                                       rating_prob1=col_double(),
                                       rating_prob2=col_double(),
                                       score1=col_integer(),
                                       score2=col_integer())
) %>% 
  filter(date < "2023-06-21")
                                    
 
favourite_win_prob <- game_data %>% 
  mutate(fav_538_won=ifelse(rating_prob1 > rating_prob2, score1 > score2, score2 > score1),
         fav_538_prob=ifelse(rating_prob1 > rating_prob2, rating_prob1, rating_prob2)) %>% 
  select(season, date, team1, team2, fav_538_won, fav_538_prob)
