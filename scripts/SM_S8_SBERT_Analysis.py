# SM_S8_SBERT_Analysis.py
# Sentence-BERT semantic evaluation

import pandas as pd
from sentence_transformers import SentenceTransformer, util

# This script assumes there is a text column containing feedback strings.
# If the manuscript data export stores feedback text under a different name,
# replace FEEDBACK_TEXT_COLUMN below.

path = "/mnt/data/Fairness_Full_Dataset.csv"
df = pd.read_csv(path)

FEEDBACK_TEXT_COLUMN = "Feedback_Text"  # adjust if needed
if FEEDBACK_TEXT_COLUMN not in df.columns:
    raise ValueError(
        f"Column '{FEEDBACK_TEXT_COLUMN}' not found. Add the feedback text column before running SBERT analysis."
    )

model = SentenceTransformer("all-MiniLM-L6-v2")
emb = model.encode(df[FEEDBACK_TEXT_COLUMN].astype(str).tolist(), convert_to_tensor=True, show_progress_bar=True)

# Example: mean semantic similarity within same Essay_ID across the six generated feedbacks
results = []
for essay_id, grp in df.groupby("Essay_ID"):
    idx = grp.index.tolist()
    if len(idx) < 2:
        continue
    vectors = emb[idx]
    sim_matrix = util.cos_sim(vectors, vectors).cpu().numpy()
    # upper triangle without diagonal
    tri = sim_matrix[np.triu_indices_from(sim_matrix, k=1)]
    results.append({"Essay_ID": essay_id, "mean_pairwise_similarity": float(tri.mean())})

out = pd.DataFrame(results)
out.to_csv("/mnt/data/SM_S8_SBERT_Similarity.csv", index=False)
print(out.head())
