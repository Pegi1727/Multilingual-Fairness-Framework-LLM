# 🚀 Integrated Multilingual Fairness Framework for AI-Powered Feedback

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.2+-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)
[![Dataset](https://img.shields.io/badge/Dataset-24k%20Records-success.svg)](data/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Science](https://img.shields.io/badge/Open%20Science-Reproducible%20Pipeline-blueviolet.svg)](Supplementary_Materials.zip)

---

## 🖼️ Graphical Abstract

<p align="center">
  <img src="ga.png" alt="Graphical Abstract - Integrated Multilingual Fairness Framework" width="100%">
</p>

---

## 📊 Key Results at a Glance

### Table: Cross-Linguistic Pedagogical Quality & Fairness by Model and Prompt Condition ($N = 24,000$)

| LLM Architecture | Prompt Condition | Actionability (1–5) | Pedagogical Tone (1–5) | Cognitive Load (1–5) | Linguistic Fairness (1–5) | FQI Score (0–1) | MFI (Cross-L1 Parity) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **GPT-4o** | Baseline | 3.912 | 4.105 | 3.824 | 3.765 | 0.781 | 0.812 |
| **GPT-4o** | Fairness-Aware | **4.328** | **4.482** | **4.210** | **4.195** | **0.864** | **0.895** |
| **Claude 4** | Baseline | 3.845 | 4.012 | 3.790 | 3.680 | 0.766 | 0.798 |
| **Claude 4** | Fairness-Aware | 4.210 | 4.390 | 4.150 | 4.085 | 0.842 | 0.871 |
| **Gemini 2.5** | Baseline | 3.650 | 3.890 | 3.610 | 3.490 | 0.732 | 0.760 |
| **Gemini 2.5** | Fairness-Aware | 4.050 | 4.230 | 3.980 | 3.920 | 0.808 | 0.835 |

> **Summary Takeaway:** The Fairness-Aware prompting condition yielded statistically significant improvements across all dimensions ($p < .001$), narrowing the cross-linguistic evaluation gap across Arabic, Chinese, Persian, and Spanish L1 cohorts.

---

## 🖼️ Visualizations & Figures Gallery

All high-resolution figures generated across the analytical pipeline are embedded below:

| **Figure 1: End-to-End Workflow** | **Figure 2: L1 Cohort Distributions** |
| :---: | :---: |
| <img src="results/Fig1_Workflow.png" alt="Figure 1" width="100%"> | <img src="results/Fig2_L1_Distributions.png" alt="Figure 2" width="100%"> |
| *Methodological pipeline: prompt engineering to metric scoring* | *CEFR score and essay distribution across L1 backgrounds* |

| **Figure 3: Metric Distributions (Baseline vs. FA)** | **Figure 4: Model Dimension Comparisons** |
| :---: | :---: |
| <img src="results/Fig3_Metric_Distributions.png" alt="Figure 3" width="100%"> | <img src="results/Fig4_Model_Comparisons.png" alt="Figure 4" width="100%"> |
| *Empirical score density across 6 evaluation dimensions* | *Comparative breakdown across GPT-4o, Claude 4, and Gemini 2.5* |

| **Figure 5: Prompt Intervention Gains ($\Delta$)** | **Figure 6: Multilingual Fairness Index (MFI)** |
| :---: | :---: |
| <img src="results/Fig5_Prompt_Intervention.png" alt="Figure 5" width="100%"> | <img src="results/Fig6_MFI_Analysis.png" alt="Figure 6" width="100%"> |
| *Pairwise performance gain under Fairness-Aware prompt* | *Cross-L1 parity quantification across models* |

| **Figure 7: SBERT Semantic Alignment** | **Figure 8: XGBoost Feature Importance & SHAP** |
| :---: | :---: |
| <img src="results/Fig7_SBERT_Alignment.png" alt="Figure 7" width="100%"> | <img src="results/Fig8_SHAP_Summary.png" alt="Figure 8" width="100%"> |
| *Semantic cosine similarity of feedback to learner error types* | *Global feature attributions: Error Density, CEFR, L1 background* |

| **Figure 9: 5,000-Resample Bootstrap Distributions** | **Figure 10: Theoretical Evaluation Architecture** |
| :---: | :---: |
| <img src="results/Fig9_Bootstrap_Distributions.png" alt="Figure 9" width="100%"> | <img src="results/Fig10_Theoretical_Framework.png" alt="Figure 10" width="100%"> |
| *95% BCa confidence intervals confirming parameter stability* | *Integrated Multilingual Fairness Theoretical Architecture* |

---

## 📌 Project Overview

Automated feedback systems powered by Large Language Models (LLMs) often exhibit implicit sociolinguistic and cross-linguistic disparities. This repository provides the complete analytical suite and dataset for evaluating feedback equity across non-native English writing cohorts.

### Core Metrics:
1. **Feedback Quality Index (FQI):** Multi-criteria synthesis evaluating pedagogical utility, cognitive load balance, actionability, and tone appropriateness.
2. **Multilingual Fairness Index (MFI):** Invariance measure quantifying variance in feedback efficacy across distinct L1 speaker groups.

---


├── requirements.txt                  # Python dependencies
└── README.md                         # Repository documentation
