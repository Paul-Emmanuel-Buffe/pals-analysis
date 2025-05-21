# Pals Analysis Project

# Pals Analysis Project

## 📌 Overview

**Pals Analysis** is a data-driven exploration of creatures ("Pals") from the game Palworld, released in January 2024. This project combines database management, statistical analysis, and interactive visualization to extract strategic insights for gameplay optimization.

## 🎮 About Palworld

Palworld is an open-world survival crafting game developed by Pocket Pair where players capture and collect creatures called "Pals". These creatures can be used for:
- Combat against other Pals and bosses
- Building and managing bases/camps
- Resource gathering and production
- Farming and crafting

## 🧩 Dataset Structure

Our analysis utilizes six interconnected datasets:

1. **Combat Attributes**: Battle statistics, elemental affinities, and combat capabilities
2. **Job Skills**: Work efficiencies and specialized abilities for base development
3. **Hidden Attributes**: Special characteristics not immediately visible in-game
4. **Refresh Areas**: Spawn locations and level distribution information
5. **Ordinary Boss Attributes**: Statistics for standard bosses encountered in the world
6. **Tower Boss Attributes**: Data on endgame tower bosses and their capabilities

## 🎯 Project Objectives

This analysis aims to answer key gameplay questions including:
- Identifying the most powerful Pals for combat
- Finding optimal work crews for base development
- Understanding correlations between Pal attributes
- Developing efficient capture strategies
- Creating balanced team compositions

## 🛠️ Technical Implementation

### Database Design
- MariaDB implementation with normalized tables
- SQL queries via Python connectors

### Analysis Pipeline
- Jupyter notebook documenting the full exploratory data analysis
- Statistical methods for distribution analysis and correlation identification
- Data visualization using matplotlib, seaborn, and plotly

### Interactive Dashboard
- Streamlit application providing real-time filtering and visualization
- Combat strategy optimization tools
- Workforce management insights

## 📊 Key Findings

*To be completed following analysis*

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- MariaDB/MySQL
- Required Python packages (see requirements.txt)

### Installation
```bash
# Clone this repository
git clone https://github.com/[username]/pals-analysis.git

# Install required packages
pip install -r requirements.txt

# Run the Streamlit app
cd app
streamlit run app.py
```

## 📁 Project Structure

```
pals-analysis/
│
├── app/                  # Streamlit web application
│   └── app.py            # Main application file
│
├── data/                 # Data files
│   ├── raw/              # Original dataset files
│   └── processed/        # Cleaned and transformed data
│
├── database/             # Database scripts and schema
│   ├── schema.sql        # Database structure
│   └── queries/          # SQL query files
│
├── notebooks/            # Jupyter analysis notebooks
│   └── pals_analysis.ipynb  # Main analysis document
│
├── src/                  # Helper scripts and utilities
│   └── data_utils.py     # Data processing functions
│
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── presentation.pdf      # Project presentation slides
```

## 🔍 Analysis Methods

Our approach includes:
- Distribution analysis of Pal attributes
- Correlation studies between combat statistics
- Clustering of Pals by capability and function
- Optimization algorithms for team composition

## 📚 Resources

- [Palworld Wiki](https://palworld.fandom.com/wiki/Palworld_Wiki)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Data Visualization Best Practices](https://www.tableau.com/learn/articles/data-visualization-tips)

## 👥 Contributors

*To be added*

## 📄 License

This project is shared for educational purposes only. All game data is property of Pocket Pair, Inc.



