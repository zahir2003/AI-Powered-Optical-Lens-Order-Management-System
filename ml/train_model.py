import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.metrics import classification_report

df = pd.read_csv("historical_orders.csv")

le_lens = LabelEncoder()
le_stage = LabelEncoder()
le_store = LabelEncoder()

df["lens_type"] = le_lens.fit_transform(df["lens_type"])

df["stage"] = le_stage.fit_transform(df["stage"])
df["store_location"] = le_store.fit_transform(df["store_location"])

X = df[
    [
        "lens_type",
        "stage",
        "store_location",
        "inventory_available",
        "elapsed_hours",
        "sla_hours",
        "days_in_current_stage",
    ]
]

y = df["breached"]

print(df["breached"].value_counts(normalize=True))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=300, max_depth=10, min_samples_split=5, random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

print(classification_report(y_test, preds))

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "model.pkl")

joblib.dump(le_lens, "lens_encoder.pkl")

joblib.dump(le_stage, "stage_encoder.pkl")
joblib.dump(le_store, "store_encoder.pkl")
