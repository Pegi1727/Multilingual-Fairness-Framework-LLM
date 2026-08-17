# SM_S6_Mixed_Effects_Analysis.R
# Mixed-effects models, MANOVA, Tukey comparisons, Holm-Bonferroni

library(readr)
library(dplyr)
library(lme4)
library(lmerTest)
library(emmeans)
library(car)
library(broom.mixed)

input_path <- "/mnt/data/Fairness_Full_Dataset.csv"
df <- read_csv(input_path, show_col_types = FALSE)

# Mixed-effects model on Overall_Score
m1 <- lmer(Overall_Score ~ L1 * Model * Prompt * CEFR + (1 | Essay_ID), data = df)
summary(m1)

# Estimated marginal means and Tukey-adjusted comparisons
emm_model <- emmeans(m1, ~ Model)
pairs_model <- pairs(emm_model, adjust = "tukey")

emm_l1 <- emmeans(m1, ~ L1)
pairs_l1 <- pairs(emm_l1, adjust = "tukey")

# MANOVA on six feedback dimensions
Y <- cbind(df$Accuracy, df$Helpfulness, df$Specificity,
           df$Actionability, df$Pedagogical_Appropriateness,
           df$Socio_Affective_Tone)
man1 <- manova(Y ~ L1 * Model * Prompt * CEFR, data = df)
summary(man1, test = "Pillai")

# Holm-Bonferroni correction example for pairwise p-values
pvals <- c(0.01, 0.04, 0.20)
p.adjust(pvals, method = "holm")

# Save key outputs
sink("/mnt/data/SM_S6_Mixed_Effects_Summary.txt")
cat("Mixed-effects model summary\n")
print(summary(m1))
cat("\nMANOVA summary\n")
print(summary(man1, test = "Pillai"))
cat("\nTukey comparisons (Model)\n")
print(pairs_model)
cat("\nTukey comparisons (L1)\n")
print(pairs_l1)
sink()
