# Pals Analysis Project

## 📌 Overview

**Pals Analysis** is a data-driven project focused on studying the attributes and behaviors of "Pals" from the open-world multiplayer survival game **Palworld** (also known as Eidolon Parlu). The goal is to uncover strategic insights through structured data exploration and interactive visualization.

---

## 🎯 Educational Objectives

This project is part of a data and AI training program, aiming to develop the following skills:

- SQL database modeling and data normalization with **MariaDB**  
- Exploratory Data Analysis (EDA) using **Jupyter Notebook**  
- Interactive web app development with **Streamlit**  
- Technical documentation and version control with **Git/GitHub**  

---

## 🧩 Project Workflow

1. **Dataset Acquisition & Exploration**  
   - Analyze and understand the structure of the dataset related to Pals  
   - Identify categorical and numerical attributes, correlations, and outliers  

2. **Database Design with MariaDB**  
   - Create a database `palworld_database` including six main tables:  
     - `combat_attribute`  
     - `job_skill`  
     - `hidden_attribute`  
     - `refresh_area`  
     - `ordinary_boss_attribute`  
     - `tower_boss_attribute`  

3. **Data Cleaning & Normalization**  
   - Remove inconsistencies, handle missing values, and prepare for querying  

4. **Exploratory Analysis in Notebooks**  
   - Investigate trends, distributions, and relations across attributes  

5. **Streamlit App Development**  
   - Build an interactive interface (`app/app.py`) for real-time visualization and user interaction  

---

## 📁 Project Structure

```plaintext
pals-analysis/
│
├── app/                  # Streamlit web app
│   └── app.py
│
├── data/                 # Raw and cleaned data files
│   └── .keep
│
├── database/             # SQL scripts or DB dumps
│   └── .keep
│
├── notebooks/            # Jupyter notebooks for EDA
│   └── .keep
│
├── src/                  # Additional source code or utilities
│   └── __init__.py
│
├── README.md             # Project overview (this file)
├── .gitignore            # Files and folders to ignore in Git
├── requirements.txt      # Python dependencies

🚀 Deliverables
📊 Jupyter Notebook documenting the full analysis and reasoning

🌐 Streamlit app for interactive visualization

📂 Public GitHub repository with clear structure and documentation

🎞️ Presentation slide deck summarizing findings and methods

🛠️ Technologies Used
Python (for scripting and visualization)

Jupyter Notebook (for analysis documentation)

SQL with MariaDB (for structured data storage and queries)

Streamlit (for building the interactive app)

Git & GitHub (for version control and collaboration)

📌 Status
Project initialized — structure ready for dataset ingestion and database setup.



