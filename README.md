# 🚀 Evaluating Cross-Linguistic Fairness in Large Language Model-Generated Writing Feedback

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.2+-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)
[![Dataset](https://img.shields.io/badge/Dataset-24k%20Records-success.svg)](data/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21973288-blue.svg)](https://doi.org/10.5281/zenodo.21973288)
[![Open Science](https://img.shields.io/badge/Open%20Science-Reproducible%20Pipeline-blueviolet.svg)](Supplementary_Materials.zip)

---

## 🖼️ Graphical Abstract

<p align="center">
  <img src="figures/ga.png" alt="Graphical Abstract - Theoretical Framework" width="100%">
</p>

---

## 📊 Key Results at a Glance

### Cross-Linguistic Pedagogical Quality & Fairness by Model and Prompt Condition

| LLM Architecture | Prompt Condition | Actionability (1–5) | Pedagogical Tone (1–5) | Cognitive Load (1–5) | Linguistic Fairness (1–5) | FQI Score (0–1) | MFI (Cross-L1 Parity) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **GPT-4o** | Baseline | 3.912 | 4.105 | 3.824 | 3.765 | 0.781 | 0.812 |
| **GPT-4o** | Fairness-Aware | **4.328** | **4.482** | **4.210** | **4.195** | **0.864** | **0.895** |
| **Claude 4** | Baseline | 3.845 | 4.012 | 3.790 | 3.680 | 0.766 | 0.798 |
| **Claude 4** | Fairness-Aware | 4.210 | 4.390 | 4.150 | 4.085 | 0.842 | 0.871 |
| **Gemini 2.5** | Baseline | 3.650 | 3.890 | 3.610 | 3.490 | 0.732 | 0.760 |
| **Gemini 2.5** | Fairness-Aware | 4.050 | 4.230 | 3.980 | 3.920 | 0.808 | 0.835 |

> **Key Takeaway:** Fairness-aware prompting reduces cross-linguistic disparity and improves pedagogical quality across Arabic, Chinese, Persian, and Spanish L1 cohorts.

---

## 🖼️ Figures & Analytical Visualizations

| **Figure 1: Methodological Workflow** | **Figure 2: L1 vs. Model Distribution** |
| :---: | :---: |
| <img src="figures/Figure1_workflow.png" alt="Figure 1: Methodological Workflow" width="100%"> | <img src="figures/Figure2_L1_Model.png" alt="Figure 2: L1 vs. Model Distribution" width="100%"> |
| *End-to-end experimental framework & evaluation stages* | *Score distributions across L1 backgrounds and model architectures* |

| **Figure 3: Correlation & Dimension Heatmap** | **Figure 4: Prompt Intervention Effect** |
| :---: | :---: |
| <img src="figures/Figure3_heatmap.png" alt="Figure 3: Correlation Heatmap" width="100%"> | <img src="figures/Figure4_prompt_effect.png" alt="Figure 4: Prompt Intervention Effect" width="100%"> |
| *Pairwise metric correlation and dimension alignment* | *Performance shifts between Baseline and Fairness-Aware conditions* |

| **Figure 5: Prompt Intervention Distribution** | **Figure 6: L1 × CEFR Interaction** |
| :---: | :---: |
| <img src="figures/Figure5_prompt_distribution.png" alt="Figure 5: Prompt Intervention Distribution" width="100%"> | <img src="figures/Figure6_L1_CEFR.png" alt="Figure 6: L1 × CEFR Interaction" width="100%"> |
| *Score distributions under Baseline vs. Fairness-Aware interventions* | *Cross-linguistic performance variations across CEFR proficiency tiers* |

| **Figure 7: Multilingual Fairness Index (MFI)** | **Figure 8: SHAP Feature Importance** |
| :---: | :---: |
| <img src="figures/Figure7_MFI.png" alt="Figure 7: Multilingual Fairness Index" width="100%"> | <img src="figures/Figure8_SHAP_importance.png" alt="Figure 8: SHAP Feature Importance" width="100%"> |
| *Dispersion, parity gaps, and equity metrics across language cohorts* | *Global feature attributions (Error Density, CEFR, L1 background)* |

| **Figure 9: Bootstrap Distributions** | **Figure 10: Theoretical Framework (GA)** |
| :---: | :---: |
| <img src="figures/Figure9_bootstrap.png" alt="Figure 9: Bootstrap Validation" width="100%"> | <img src="figures/ga.png" alt="Figure 10: Theoretical Framework / Graphical Abstract" width="100%"> |
| *5,000-resample non-parametric bootstrap validation (95% BCa CI)* | *Integrated Multilingual Fairness Theoretical Architecture* |

---

## 📁 Repository Contents

- `Fairness_Full_Dataset.csv` — main dataset (24,000 records)
- `README.txt` — supplementary instructions
- `SM_S4_Data_Dictionary.xlsx`
- `SM_S5_FQI_MFI_Computation.R`
- `SM_S6_Mixed_Effects_Analysis.R`
- `SM_S7_XGBoost_SHAP_Analysis.py`
- `SM_S8_SBERT_Analysis.py`
- `SM_S9_Bootstrap_Analysis.R`
- `SM_S10_Figure_Data.xlsx`
- `Supplementary_Materials.zip`

---

## 🔬 Methods Overview

This study evaluates cross-linguistic fairness in LLM-generated writing feedback using:

- **Mixed-effects models**
- **FQI / MFI indices**
- **XGBoost + SHAP**
- **SBERT semantic alignment**
- **5,000-resample bootstrap validation**

---

## 📌 Reproducibility

All code, data dictionary, figure data, and analysis scripts are included in the supplementary package for full reproducibility.

Archived supplementary materials are also available via Zenodo:

**DOI:** [10.5281/zenodo.21973288](https://doi.org/10.5281/zenodo.21973288)

---

## 📄 Citation

If you use this repository, please cite the associated paper and Zenodo record where appropriate.

---

## 📬 Contact

For questions or collaboration, please contact the corresponding author.
