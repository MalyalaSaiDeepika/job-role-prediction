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

🎯 Distribution of Job Roles – Shows the number of resumes per Job Role.
<img width="1003" height="611" alt="Screenshot 2025-10-09 220117" src="https://github.com/user-attachments/assets/c4c3be07-2c84-4b88-bc9d-74bea0c66ea3" />


🌡️ Correlation Heatmap – Highlights relationships between numerical features.
<img width="1134" height="845" alt="Screenshot 2025-10-09 220615" src="https://github.com/user-attachments/assets/6c4e91d6-cff4-414d-bdbc-1f8020338503" />


📊 Histograms of Numerical Features – Shows distribution and spread of numerical features.
<img width="1501" height="918" alt="Screenshot 2025-10-09 222159" src="https://github.com/user-attachments/assets/bbc99e46-6da9-4337-b1af-49d91d151563" />
<img width="1493" height="907" alt="Screenshot 2025-10-09 222220" src="https://github.com/user-attachments/assets/17caf880-fb3e-40ca-9596-63cb3d215a7c" />
<img width="781" height="478" alt="Screenshot 2025-10-09 222232" src="https://github.com/user-attachments/assets/e9fe2f30-3ff7-48d5-abca-ff67848b5f68" />





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
