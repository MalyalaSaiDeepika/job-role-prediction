📊 Job Role Prediction Project
Milestone 1 – Dataset Exploration & Basic Analysis

Objective: Understand the dataset, perform initial cleaning, and basic exploratory data analysis (EDA).

Steps Completed:

Loaded dataset and inspected columns, types, and missing values.

Handled missing values.

Performed basic summary statistics.

Visualizations included:

Count plots for categorical columns

Histograms for numeric columns

Correlation heatmaps

<img width="1065" height="634" alt="Screenshot 2025-10-08 203336" src="https://github.com/user-attachments/assets/a4e30060-d772-4cb9-876d-1fbbe63eb389" />
<img width="1085" height="716" alt="Screenshot 2025-10-08 203413" src="https://github.com/user-attachments/assets/33ae71c8-1407-482f-98dd-a9d37b41f06b" />

💼 Job Role Prediction Project – Milestone 2

✨ Project Overview

This project predicts Job Roles based on candidate Education, Skills, Experience, Certifications, and other features.
Milestone 2 focuses on data preprocessing, outlier handling, encoding, scaling, and visualizations to prepare the dataset for ML models.

📊 Dataset Information
Feature	Type	Missing Values	Notes
Resume_ID	Numeric	0	Unique ID
Name	Categorical	0	Candidate Name
Skills	Categorical	0	Candidate Skills
Experience (Years)	Numeric	0	Years of Experience
Education	Categorical	0	Degree Type
Certifications	Categorical	274	Missing handled
Job Role	Categorical	0	Target Variable
Recruiter Decision	Categorical	188	Missing handled
Salary Expectation ($)	Numeric	0	
Projects Count	Numeric	0	
AI Score (0-100)	Numeric	6	Outliers handled
🛠 Milestone 2 Workflow

1️⃣ Load & Inspect Data

Loaded dataset into a DataFrame

Checked shape, data types, missing values, duplicates

2️⃣ Handle Missing Values

Filled categorical columns with mode

Filled numeric columns with mean

3️⃣ Handle Outliers

Capped extreme values using IQR method

Checked numeric features for unusual values

4️⃣ Encode Categorical Variables

Converted categorical data into numeric form using Label Encoding

5️⃣ Feature Scaling

Standardized numeric features with Z-score scaling

6️⃣ Feature Selection & Train-Test Split

Split data into features (X) and target (y)

Train-Test split: 80% train, 20% test

📈 Visualizations

Distribution of Job Roles

<img width="1364" height="679" alt="Screenshot 2025-10-10 225220" src="https://github.com/user-attachments/assets/04ede74c-2c59-486f-b60b-571ccdc3b96d" />


Boxplots: Features vs Job Role
<img width="1437" height="825" alt="Screenshot 2025-10-10 225247" src="https://github.com/user-attachments/assets/f22ed63b-ba75-4876-a459-f2c18393e565" />



Scatter Plot: Certifications vs Job Role
<img width="1496" height="910" alt="Screenshot 2025-10-10 225319" src="https://github.com/user-attachments/assets/7a385344-11cd-4f8a-8fd7-c31d8701e569" />
<img width="1493" height="921" alt="Screenshot 2025-10-10 225346" src="https://github.com/user-attachments/assets/0ad10760-f203-40a8-b5e7-588efdc18393" />
<img width="1493" height="480" alt="Screenshot 2025-10-10 225411" src="https://github.com/user-attachments/assets/e663778f-3da3-47a0-963d-8a1c004e115b" />





Correlation Heatmap of Numeric Features
<img width="1350" height="824" alt="Screenshot 2025-10-10 225425" src="https://github.com/user-attachments/assets/77f9cd29-e9c3-4712-bb84-4af5839af01a" />



Histograms of Numeric Features
<img width="1494" height="914" alt="Screenshot 2025-10-10 225444" src="https://github.com/user-attachments/assets/0ee4928c-6743-43d8-a0d1-6861d80b1523" />
<img width="1494" height="917" alt="Screenshot 2025-10-10 225502" src="https://github.com/user-attachments/assets/e75eb7fe-2356-4121-937a-b3af734626fc" />
<img width="1481" height="458" alt="Screenshot 2025-10-10 225529" src="https://github.com/user-attachments/assets/ec18c914-516b-4eb0-8fb7-5ff67eb874d5" />





✅ Summary

Data Preprocessing Complete: Missing values handled, categorical features encoded

Outliers Managed: Capped extreme values in numeric features

Feature Scaling Applied: Standardization done

Dataset Ready for ML Models: Train-test split completed

Visual Insights Generated: Distribution, correlation, scatter, and boxplots

💻 Tech Stack

Python 🐍

Pandas 📊

NumPy 🔢

Matplotlib & Seaborn 📉

Scikit-learn 🤖

Outcome:
Dataset is now clean, scaled, and ready for machine learning models. Advanced visualizations give clear insights into data distribution, relationships, and outliers.
