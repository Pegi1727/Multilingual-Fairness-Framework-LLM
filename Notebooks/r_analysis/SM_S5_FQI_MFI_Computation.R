# SM_S5_FQI_MFI_Computation.R
# Feedback Quality Index (FQI) and Multilingual Fairness Index (MFI)

library(readr)
library(dplyr)
library(writexl)

input_path <- "/mnt/data/Fairness_Full_Dataset.csv"
df <- read_csv(input_path, show_col_types = FALSE)

dims <- c("Accuracy", "Helpfulness", "Specificity", "Actionability",
          "Pedagogical_Appropriateness", "Socio_Affective_Tone")

# FQI: simple mean of the six feedback quality dimensions
# This is consistent with the manuscript's composite quality interpretation.
df <- df %>%
  mutate(FQI = rowMeans(across(all_of(dims)), na.rm = FALSE))

# MFI: fairness across L1 groups, computed from group-mean FQI dispersion
# Higher MFI = lower between-group variability
l1_summary <- df %>%
  group_by(L1) %>%
  summarise(mean_FQI = mean(FQI), n = n(), .groups = "drop")

cv_between <- sd(l1_summary$mean_FQI) / mean(l1_summary$mean_FQI)
MFI <- 1 - cv_between

# Optional model/prompt summaries
model_prompt_summary <- df %>%
  group_by(Model, Prompt, L1) %>%
  summarise(mean_FQI = mean(FQI), sd_FQI = sd(FQI), n = n(), .groups = "drop")

# Output tables
write_xlsx(
  list(
    full_data_with_FQI = df,
    l1_summary = l1_summary,
    model_prompt_summary = model_prompt_summary,
    fairness_index = data.frame(MFI = MFI, CV_between = cv_between)
  ),
  path = "/mnt/data/SM_S5_FQI_MFI_Output.xlsx"
)

cat(sprintf("MFI = %.6f\n", MFI))
cat(sprintf("CV_between = %.6f\n", cv_between))
