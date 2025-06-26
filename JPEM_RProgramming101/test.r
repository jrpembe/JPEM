library(tidyverse)
library(gtExtras)

iris %>%
  tab_out %>% sub_missing(Mean:SD)
  gt_plt_summary()
