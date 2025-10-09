🚀 Job Role Prediction Project

This repository contains the Job Role Prediction project using Machine Learning, completed as part of the Infosys Internship. The project predicts suitable job roles from resumes based on skills, experience, education, certifications, and other features.

📑 Table of Contents

Repository Structure

Milestone 1 – Data Exploration & Initial Setup

Milestone 2 – Data Preprocessing & Visualization

Visualizations

Dataset

How to Use

License

Acknowledgements

📂 Repository Structure
Infosys(M-1).ipynb       → Milestone 1 notebook
Infosys(M-2).ipynb       → Milestone 2 notebook (Data Preprocessing & Visualization)
archive (1).zip          → Original dataset
screenshots/             → Folder containing visualization images
LICENSE                  → License file
README.md                → Project documentation

📝 Milestone 1 – Data Exploration & Initial Setup

🔍 Loaded and explored the dataset.

🗂 Checked dataset shape, data types, and missing values.

📊 Conducted basic analysis to identify features and target.

✏️ Documented observations and initial insights.

🧹 Milestone 2 – Data Preprocessing & Visualization

🧼 Data Cleaning: Removed duplicates, filled missing values in Certifications.

🔄 Data Transformation: Encoded categorical features (Skills, Education, Certifications, Recruiter Decision) and target (Job Role) using LabelEncoder.

📏 Feature Scaling: Scaled numerical features (Experience, Salary Expectation, Projects Count, AI Score) using StandardScaler.

📊 Data Structuring: Split dataset into features (X) and target (y) for machine learning.

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

Clone the repository:

git clone https://github.com/YourUsername/JobRolePrediction.git


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
