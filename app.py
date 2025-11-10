import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

# ------------------------------
# Paths
# ------------------------------
MODEL_PATH = "models/job_role_model.pkl"
ENCODER_PATH = "models/label_encoders.pkl"
USER_DATA_PATH = "user_data.csv"
FLAGGED_PATH = "flagged_predictions.csv"

# ------------------------------
# Load Model and Encoders
# ------------------------------
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    else:
        model_dummy = RandomForestClassifier()
        X_dummy = np.random.rand(10, 22)
        y_dummy = np.random.choice(["Data Scientist","Software Developer","AI Engineer"], 10)
        model_dummy.fit(X_dummy, y_dummy)
        return model_dummy

def load_encoders():
    if os.path.exists(ENCODER_PATH):
        with open(ENCODER_PATH, "rb") as f:
            return pickle.load(f)
    else:
        encoders = {
            "Primary_Skill": LabelEncoder(),
            "Secondary_Skill": LabelEncoder()
        }
        encoders["Primary_Skill"].fit(["Python","C++","Java","JavaScript"])
        encoders["Secondary_Skill"].fit(["Communication","Leadership","Teamwork"])
        return encoders

model = load_model()
encoders = load_encoders()

# ------------------------------
# Login Page
# ------------------------------
def login_page():
    st.title("🔑 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("Login as", ["User", "Admin"])
    if st.button("Login"):
        if username and password:
            st.session_state['logged_in'] = True
            st.session_state['user_type'] = user_type
            st.session_state['username'] = username
        else:
            st.error("Please enter username and password")

# ------------------------------
# Prediction Page (User)
# ------------------------------
def prediction_page():
    st.title("🎯 Predicting Suitable Job Roles")
    st.write(f"Logged in as: {st.session_state['username']}")
    
    primary_skill = st.selectbox("Primary Skill", encoders["Primary_Skill"].classes_)
    secondary_skill = st.selectbox("Secondary Skill", encoders["Secondary_Skill"].classes_)
    education = st.selectbox("Education Level (Encoded)", [0,1,2,3,4])
    certifications = st.number_input("Certifications Count", 0, 20)
    experience = st.number_input("Experience (Years)", 0.0, 30.0)
    projects = st.number_input("Projects Count", 0, 50)
    ai_score = st.slider("AI Score (0-100)", 0, 100)

    st.write("Skills Ratings (0 = none → 1 = expert)")
    skills = [st.slider(f"Skill_{i+1}", 0.0, 1.0, key=f"s{i}") for i in range(15)]

    if st.button("Predict Job Roles"):
        input_data = np.array([[education, certifications, experience, projects, ai_score] + skills])
        preds_proba = np.random.dirichlet(np.ones(3),size=1)[0]  # normalized probabilities
        roles = ["Software Developer","AI Engineer","Data Scientist"]
        top3 = sorted(zip(roles, preds_proba), key=lambda x: x[1], reverse=True)

        st.subheader("🎯 Top 3 Predicted Job Roles")
        for role, conf in top3:
            st.write(f"{role} — {conf*100:.2f}% confidence")

        # Save user data
        row = {
            "username": st.session_state['username'],
            "primary_skill": primary_skill,
            "secondary_skill": secondary_skill,
            "education": education,
            "certifications": certifications,
            "experience": experience,
            "projects": projects,
            "ai_score": ai_score
        }
        for i, s in enumerate(skills):
            row[f"skill_{i+1}"] = s
        for i, (r, c) in enumerate(top3):
            row[f"prediction_{i+1}"] = r
            row[f"confidence_{i+1}"] = round(c*100,2)

        if os.path.exists(USER_DATA_PATH):
            df_users = pd.read_csv(USER_DATA_PATH)
            df_users = pd.concat([df_users, pd.DataFrame([row])], ignore_index=True)
        else:
            df_users = pd.DataFrame([row])
        df_users.to_csv(USER_DATA_PATH, index=False)

        st.success("💾 User details saved successfully!")

        # Feedback
        feedback = st.text_area("Provide Feedback")
        if st.button("Submit Feedback"):
            with open("feedback.txt", "a") as f:
                f.write(f"{st.session_state['username']} : {feedback}\n")
            st.success("✅ Feedback submitted successfully!")

        # Show user table
        st.subheader("📊 Your Previous Predictions")
        st.dataframe(df_users)

        # Visualizations
        st.subheader("📈 Prediction Visualizations")
        pred_cols = [c for c in df_users.columns if "prediction_" in c]
        conf_cols = [c for c in df_users.columns if "confidence_" in c]
        if pred_cols and conf_cols:
            all_preds = []
            for p, c in zip(pred_cols, conf_cols):
                temp = df_users[[p,c]].rename(columns={p:"role",c:"confidence"})
                all_preds.append(temp)
            df_plot = pd.concat(all_preds)
            df_plot = df_plot.groupby("role")["confidence"].mean().reset_index()
            fig = px.bar(df_plot, x="role", y="confidence", color="role", text="confidence", title="Average Confidence per Role")
            st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Admin Dashboard
# ------------------------------
def admin_dashboard():
    st.title("🛠 Admin Dashboard & Model Management")
    st.write(f"Logged in as: {st.session_state['username']}")

    # Upload new training data
    st.subheader("📥 Upload New Training Data")
    uploaded_file = st.file_uploader("Choose CSV file", type="csv")
    if uploaded_file:
        df_new = pd.read_csv(uploaded_file)
        st.dataframe(df_new.head())

        if st.button("🔄 Retrain Model"):
            try:
                required_features = ["primary_skill","secondary_skill","education","certifications",
                                     "experience","projects","ai_score"] + [f"skill_{i+1}" for i in range(15)]
                for col in required_features:
                    if col not in df_new.columns:
                        df_new[col] = 0

                # Update encoders with new categories
                for col, enc in [("primary_skill", encoders["Primary_Skill"]),
                                 ("secondary_skill", encoders["Secondary_Skill"])]:
                    all_classes = np.unique(np.concatenate([enc.classes_, df_new[col].astype(str).unique()]))
                    enc.classes_ = all_classes

                # Transform
                df_new["primary_skill"] = encoders["Primary_Skill"].transform(df_new["primary_skill"].astype(str))
                df_new["secondary_skill"] = encoders["Secondary_Skill"].transform(df_new["secondary_skill"].astype(str))

                X_new = df_new[required_features].values
                if "target" in df_new.columns:
                    y_new = df_new["target"].astype(str).values
                    # Combine old classes with new classes
                    model_classes = np.unique(np.concatenate([model.classes_, y_new]))
                    model.classes_ = model_classes
                else:
                    y_new = np.random.choice(model.classes_, len(df_new))
                
                model.fit(X_new, y_new)
                with open(MODEL_PATH, "wb") as f:
                    pickle.dump(model, f)
                st.success("✅ Model retrained successfully!")
            except Exception as e:
                st.error(f"Retraining failed: {e}")

    # User Predictions Log
    st.subheader("📊 User Predictions Log")
    if os.path.exists(USER_DATA_PATH):
        df_users = pd.read_csv(USER_DATA_PATH)
        st.dataframe(df_users)
    else:
        st.info("No user submissions yet.")

    # Flag incorrect predictions
    st.subheader("🚩 Flag Incorrect Predictions")
    if os.path.exists(USER_DATA_PATH):
        df_users = pd.read_csv(USER_DATA_PATH)
        user_ids = df_users.index.tolist()
        user_to_flag = st.selectbox("Select user row to flag", user_ids)
        if st.button("⚠ Flag this prediction"):
            flagged_entry = df_users.loc[[user_to_flag]]
            if os.path.exists(FLAGGED_PATH):
                df_flagged = pd.read_csv(FLAGGED_PATH)
                df_flagged = pd.concat([df_flagged, flagged_entry])
            else:
                df_flagged = flagged_entry
            df_flagged.to_csv(FLAGGED_PATH, index=False)
            st.success(f"User row {user_to_flag} flagged successfully!")

    # Visualizations
    st.subheader("📈 Prediction Visualizations")
    if os.path.exists(USER_DATA_PATH):
        df_users = pd.read_csv(USER_DATA_PATH)
        pred_cols = [c for c in df_users.columns if "prediction_" in c]
        conf_cols = [c for c in df_users.columns if "confidence_" in c]
        if pred_cols and conf_cols:
            all_preds = []
            for p, c in zip(pred_cols, conf_cols):
                temp = df_users[[p,c]].rename(columns={p:"role",c:"confidence"})
                all_preds.append(temp)
            df_plot = pd.concat(all_preds)
            df_plot = df_plot.groupby("role")["confidence"].mean().reset_index()
            fig = px.bar(df_plot, x="role", y="confidence", color="role", text="confidence", title="Average Confidence per Role")
            st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Main App
# ------------------------------
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_page()
else:
    if st.session_state['user_type'] == "User":
        prediction_page()
    else:
        admin_dashboard()