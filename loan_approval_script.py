import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("loan_data.csv")

X_train, X_test, y_train, y_test = train_test_split(df.drop("loan_status", axis=1), df['loan_status'], test_size = 0.25, random_state=42)

X_train.reset_index(drop=True, inplace=True)
X_test.reset_index(drop=True, inplace=True)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

# numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop="first")
# categorical_transformer = OrdinalEncoder()

# numerical_columns = list(df.select_dtypes(["int", "float", "object", "bool"]).drop(["loan_status"], axis=1).columns)
categorical_columns = list(df.select_dtypes(["object", "bool"]).columns)

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_transformer, categorical_columns),
        # ("num", numeric_transformer, numerical_columns),
    ], remainder='passthrough'
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(C=0.046415888336127774, l1_ratio=0.0, max_iter=500,penalty='l1', random_state=42, solver='saga'))
])

pipeline.fit(X_train, y_train)

import joblib

joblib.dump(pipeline, "model.pkl")