import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("Dataset After Milestone 3.csv")

# Create encoders
edu_enc = LabelEncoder()
role_enc = LabelEncoder()

# Encode columns
df["Education"] = edu_enc.fit_transform(df["Education"])
df["Job Role"] = role_enc.fit_transform(df["Job Role"])

# Features list (20 skill columns + education + experience + cert + projects + AI score)
feature_cols = [
    "Education", "Experience (Years)", "Certifications",
    "Projects Count", "AI Score (0-100)"
] + [f"Skill_Feature_{i}" for i in range(15)]

X = df[feature_cols]
y = df["Job Role"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model & encoder
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump({"edu": edu_enc, "role": role_enc}, open("encoders.pkl", "wb"))

print("✅ Training Completed Successfully!")
print(f"✅ Features Used: {len(feature_cols)}")
