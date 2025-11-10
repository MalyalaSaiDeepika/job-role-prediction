import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
import datetime

# ------------------------------
# Paths
# ------------------------------
MODEL_PATH = "models/job_role_model.pkl"
USER_DATA_PATH = "user_data.csv"
FLAGGED_PATH = "flagged_predictions.csv"

# ------------------------------
# Load Model
# ------------------------------
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    else:
        return None

model = load_model()
if model is None:
    st.error("❌ Model not found! Place 'job_role_model.pkl' in 'models/' folder.")
    st.stop()

# ------------------------------
# Admin Login
# ------------------------------
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

def login(username, password):
    if username == "admin" and password == "admin123":
        st.session_state.admin_logged_in = True
        st.session_state.username = username
    else:
        st.error("Invalid username or password")

if not st.session_state.admin_logged_in:
    st.title("🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)
    st.stop()

# ------------------------------
# Dashboard Title
# ------------------------------
st.title("🛠 Admin Dashboard & Model Management")
st.write(f"Logged in as: {st.session_state.username}")

# ------------------------------
# 1. Upload New Training Data & Retrain Model
# ------------------------------
st.subheader("📥 Upload New Training Data")
uploaded_file = st.file_uploader("Choose CSV file", type="csv")
if uploaded_file:
    df_new = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(df_new.head())

    if st.button("🔄 Retrain Model with Uploaded Data"):
        try:
            # Use 'target' column if exists; else create dummy
            X_new = df_new.drop(columns=["target"], errors='ignore').values
            y_new = df_new["target"].values if "target" in df_new.columns else np.random.choice(
                ["Software Developer","Data Scientist","AI Engineer"], len(df_new)
            )

            new_model = RandomForestClassifier(n_estimators=100, random_state=42)
            new_model.fit(X_new, y_new)

            with open(MODEL_PATH, "wb") as f:
                pickle.dump(new_model, f)
            st.success("✅ Model retrained and saved successfully!")
        except Exception as e:
            st.error(f"Retraining failed: {e}")

# ------------------------------
# 2. View User Predictions Log
# ------------------------------
st.subheader("📊 User Predictions Log")
if os.path.exists(USER_DATA_PATH):
    df_users = pd.read_csv(USER_DATA_PATH)
    st.dataframe(df_users)
else:
    st.info("No user submissions yet.")

# ------------------------------
# 3. Flag Incorrect Predictions
# ------------------------------
st.subheader("🚩 Flag Incorrect Predictions")
if os.path.exists(USER_DATA_PATH):
    df_users = pd.read_csv(USER_DATA_PATH)
    user_ids = df_users.index.tolist()
    user_to_flag = st.selectbox("Select user row to flag", user_ids)
    if st.button("⚠ Flag this prediction"):
        flagged_entry = df_users.loc[[user_to_flag]]
        if os.path.exists(FLAGGED_PATH):
            df_flagged = pd.read_csv(FLAGGED_PATH)
            df_flagged = pd.concat([df_flagged, flagged_entry], ignore_index=True)
        else:
            df_flagged = flagged_entry
        df_flagged.to_csv(FLAGGED_PATH, index=False)
        st.success(f"User row {user_to_flag} flagged successfully!")
elif not os.path.exists(USER_DATA_PATH):
    st.info("No user submissions yet to flag.")

# ------------------------------
# 4. Visualizations / Metrics
# ------------------------------
st.subheader("📈 Prediction Visualizations")
if os.path.exists(USER_DATA_PATH):
    df_users = pd.read_csv(USER_DATA_PATH)
    if not df_users.empty and "prediction" in df_users.columns and "confidence" in df_users.columns:
        # Average confidence per role
        top_roles = df_users.groupby("prediction")["confidence"].mean().sort_values(ascending=False).reset_index()
        fig_bar = px.bar(top_roles, x="prediction", y="confidence", color="prediction", text="confidence",
                         title="Average Confidence per Role")
        st.plotly_chart(fig_bar, use_container_width=True)

        # Pie chart
        fig_pie = px.pie(top_roles, names="prediction", values="confidence", title="Confidence Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("User data does not contain 'prediction' and 'confidence' columns.")