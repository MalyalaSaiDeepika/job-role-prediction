# Job Role Prediction Project

## Project Overview
This project aims to predict suitable job roles for candidates based on their resumes using machine learning. The project is structured into multiple milestones to ensure systematic progress.

---

## Milestone 1 – Data Cleaning & Exploratory Data Analysis
**Notebook:** `Milestone1/Infosys(M-1).ipynb`  

**Objectives:**
- Collect and integrate datasets (Education, Certifications, Skills, Job Roles)
- Handle missing values and normalize text fields
- Perform Exploratory Data Analysis (EDA)
- Produce clean dataset ready for feature engineering

**Output:**  
- Cleaned dataset  
- EDA insights notebook  

---

## Milestone 2 – Feature Engineering & Preprocessing Pipeline
**Notebook:** `Milestone2/Infosys(M-2).ipynb`  
**Pipeline File:** `Milestone2/milestone2_pipeline.pkl`  

**Objectives:**
- Encode categorical variables (Education, Certifications)  
- Apply TF-IDF on `Skills` column  
- Handle class imbalance using SMOTE  
- Reduce dimensionality and prepare dataset for modeling  
- Save preprocessing pipeline for future model training  

**Output:**  
- Feature-engineered dataset  
- Preprocessing pipeline (`.pkl`) ready for Milestone 3  

---

## Folder Structure
job-role-prediction/
│── LICENSE
│── README.md
│── Infosys(M-1).ipynb
│── Infosys(M-2).ipynb
│── archive (1).zip
│── milestone2_pipeline.pkl

