import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

# ✅ Get absolute path to your current project folder (Final submission)
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, "models")

# ✅ Create the folder if missing
os.makedirs(models_dir, exist_ok=True)

# ✅ Create dummy encoders
encoders = {
    "Primary_Skill": LabelEncoder(),
    "Secondary_Skill": LabelEncoder()
}

encoders["Primary_Skill"].fit(["Python", "Java", "C++", "SQL", "R"])
encoders["Secondary_Skill"].fit(["Communication", "Leadership", "Problem Solving", "Teamwork"])

# ✅ Dummy model with 22 input features
model = RandomForestClassifier(random_state=42)
X_dummy = np.random.rand(20, 22)
y_dummy = np.random.choice(["Data Scientist", "Software Developer", "AI Engineer"], size=20)
model.fit(X_dummy, y_dummy)

# ✅ Save model and encoders using absolute paths
model_path = os.path.join(models_dir, "job_role_model.pkl")
encoders_path = os.path.join(models_dir, "label_encoders.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(encoders_path, "wb") as f:
    pickle.dump(encoders, f)

print(f"✅ Model saved to: {model_path}")
print(f"✅ Encoders saved to: {encoders_path}")