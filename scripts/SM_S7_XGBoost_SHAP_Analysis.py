# SM_S7_XGBoost_SHAP_Analysis.py
# XGBoost predictive modeling and SHAP analysis

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import shap

# Load data
path = "/mnt/data/Fairness_Full_Dataset.csv"
df = pd.read_csv(path)

# Target and predictors
# Predict Overall_Score from context and experimental factors
features = ["L1", "CEFR", "Model", "Prompt", "Error_Density", "Lexical_Sophistication"]
X = df[features].copy()
y = df["Overall_Score"].copy()

cat_cols = ["L1", "CEFR", "Model", "Prompt"]
num_cols = ["Error_Density", "Lexical_Sophistication"]

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ("num", "passthrough", num_cols),
    ]
)

model = XGBRegressor(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42,
    objective="reg:squarederror"
)

pipe = Pipeline(steps=[("prep", preprocess), ("model", model)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipe.fit(X_train, y_train)

pred = pipe.predict(X_test)
rmse = mean_squared_error(y_test, pred, squared=False)
r2 = r2_score(y_test, pred)

print(f"RMSE: {rmse:.4f}")
print(f"R2: {r2:.4f}")

# SHAP on transformed matrix
X_test_trans = pipe.named_steps["prep"].transform(X_test)
feature_names = pipe.named_steps["prep"].get_feature_names_out()
explainer = shap.TreeExplainer(pipe.named_steps["model"])
shap_values = explainer.shap_values(X_test_trans)

summary = pd.DataFrame({
    "feature": feature_names,
    "mean_abs_shap": np.abs(shap_values).mean(axis=0)
}).sort_values("mean_abs_shap", ascending=False)
summary.to_csv("/mnt/data/SM_S7_SHAP_Summary.csv", index=False)
print(summary.head(20))
