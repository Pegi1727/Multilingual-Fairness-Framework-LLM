# SM_S9_Bootstrap_Analysis.R
# Bootstrap resampling for main effects and confidence intervals

library(readr)
library(dplyr)
library(boot)

set.seed(42)

df <- read_csv("/mnt/data/Fairness_Full_Dataset.csv", show_col_types = FALSE)

# Example statistic: difference in mean Overall_Score between FairnessAware and Baseline
stat_fun <- function(data, indices) {
  d <- data[indices, ]
  means <- d %>% group_by(Prompt) %>% summarise(m = mean(Overall_Score), .groups = "drop")
  diff <- means$m[means$Prompt == "FairnessAware"] - means$m[means$Prompt == "Baseline"]
  return(diff)
}

boot_res <- boot(data = df, statistic = stat_fun, R = 1000)
ci <- boot.ci(boot_res, type = c("perc", "bca"))

sink("/mnt/data/SM_S9_Bootstrap_Summary.txt")
print(boot_res)
print(ci)
sink()
