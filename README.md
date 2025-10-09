🚀 Job Role Prediction Project

This repository contains the Job Role Prediction project using Machine Learning, completed as part of the Infosys Internship. The project predicts suitable job roles from resumes based on skills, experience, education, certifications, and other features.

📂 Repository Structure
Infosys(M-1).ipynb       → Milestone 1 notebook
Infosys(M-2).ipynb       → Milestone 2 notebook (Data Preprocessing & Visualization)
archive (1).zip          → Original dataset
screenshots/             → Folder containing visualization images
LICENSE                  → License file
README.md                → Project documentation

📝 Milestone 1 – Data Exploration & Initial Setup

🔍 Dataset Exploration: Loaded the dataset, checked shape, data types, and missing values.

🗂 Feature Analysis: Identified important features and target variable (Job Role).

✏️ Observations: Documented initial insights for better understanding of dataset.

🧹 Milestone 2 – Data Preprocessing & Visualization

🧼 Data Cleaning: Removed duplicates, filled missing values in Certifications.

🔄 Data Transformation: Encoded categorical features (Skills, Education, Certifications, Recruiter Decision) and target (Job Role) using LabelEncoder.

📏 Feature Scaling: Standardized numerical features (Experience, Salary Expectation, Projects Count, AI Score) using StandardScaler.

📊 Data Structuring: Prepared dataset for machine learning by splitting into features (X) and target (y).

📈 Visualizations

🎯 Distribution of Job Roles:
Shows the number of resumes per Job Role.
<img src="screenshots/job_role_distribution.png" width="800"/>

🌡️ Correlation Heatmap:
Highlights relationships between numerical features.
<img src="screenshots/correlation_heatmap.png" width="800"/>

📊 Histograms of Numerical Features:
Shows distribution and spread of numerical features.
<img src="screenshots/numerical_histograms.png" width="800"/>

🗃️ Dataset

Dataset is provided in archive (1).zip.

Columns include:

Resume_ID

Name

Skills

Experience (Years)

Education

Certifications

Job Role

Recruiter Decision

Salary Expectation ($)

Projects Count

AI Score (0-100)

⚡ How to Use

Open notebooks in Jupyter Notebook.

Run cells sequentially:

Infosys(M-1).ipynb → Milestone 1

Infosys(M-2).ipynb → Milestone 2

Use the preprocessed data from Milestone 2 for training ML models in later milestones.

🛡️ License

This project is licensed under the MIT License – see LICENSE file for details.

🙏 Acknowledgements

Infosys Internship program for providing project guidelines.

Kaggle dataset contributors.

Libraries used: pandas, numpy, scikit-learn, matplotlib, seaborn.
