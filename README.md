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




🤖 Job Role Prediction Project – Milestone 3
🎯 Objective

Apply multiple machine learning models to predict Job Roles based on candidate profiles and compare their performance to select the best model.

⚙️ Models Applied & Parameters
Model	Main Parameters	Accuracy (%)	Key Point
KNN	n_neighbors = 5	93.00	Simple, effective distance-based model
Gradient Boosting	n_estimators = 100, criterion = 'friedman_mse'	90.00	Excellent performance, stable and generalizable
Decision Tree	criterion = 'gini'	85.43	Easy to interpret, risk of overfitting
Random Forest	n_estimators = 100, criterion = 'gini'	61.81	Moderate performance, depends on tuning
SVM	kernel = 'rbf', max_iter = -1	47.24	Non-linear, sensitive to scaling
AdaBoost	n_estimators = 50	43.22	Weak learner combination
Logistic Regression	max_iter = 1000	39.20	Linear baseline model
📋 Cross-Validation

Used 5-Fold Cross Validation for stable and unbiased accuracy measurement.

KNN and Gradient Boosting showed consistent and reliable performance across folds.

Models like Decision Tree and Random Forest varied slightly due to data complexity.

📊 Visualizations
1️⃣ Bar Chart – Model vs Accuracy

Displays performance comparison of all models.

2️⃣ Pie Chart – Accuracy Proportion

Represents how much each model contributes to total performance.

3️⃣ Confusion Matrix

Visualizes prediction accuracy of the top model (KNN / Gradient Boosting).

4️⃣ Accuracy Trend (Optional)

Shows accuracy progression as parameters were tuned.

📸 Screenshots of accuracies:

<img width="1104" height="653" alt="Screenshot 2025-10-30 000109" src="https://github.com/user-attachments/assets/84772ff8-d4b4-448c-9c7f-04a96acae8ac" />
<img width="1121" height="613" alt="Screenshot 2025-10-30 000124" src="https://github.com/user-attachments/assets/ac1a6298-1863-46e3-b0fc-dc8a71e23f9f" />
<img width="788" height="618" alt="Screenshot 2025-10-30 000117" src="https://github.com/user-attachments/assets/ef5d7e63-a20b-4766-90a0-a4ca08928916" />


✅ Summary

Applied and compared 7 machine learning models.

KNN (93%) and Gradient Boosting (91%) achieved top results.

Accuracy improved after fine-tuning and proper preprocessing.

Gradient Boosting shows stable generalization; KNN offers simpler, strong performance.

Dataset thoroughly preprocessed and scaled from Milestone 2.


💻 Tech Stack

Python 🐍

Pandas, NumPy — Data Handling

Matplotlib, Seaborn — Data Visualization

Scikit-learn — ML Algorithms & Evaluation

🚀 Outcome

Models trained, evaluated, and compared systematically.

KNN achieved the best overall performance (93%) for this dataset.

Project ready for Milestone 4 – Deployment or Optimization.
