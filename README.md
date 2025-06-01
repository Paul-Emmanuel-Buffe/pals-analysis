# 📊 Pals Analysis

**Pals Analysis** est un projet d'analyse de données portant sur les créatures du jeu *Palworld*. Il combine modélisation relationnelle, exploration statistique et visualisation interactive dans le but d’identifier des patterns utiles à la stratégie de jeu.

---

## 🎓 Objectifs pédagogiques

Projet développé dans un cadre de formation en Data & IA, permettant de travailler :

- 📁 Modélisation et normalisation de base de données (MariaDB)
- 📊 Analyse exploratoire (EDA) avec Jupyter
- 🌐 Développement d'applications interactives avec Streamlit
- 🗂️ Documentation technique et versionnage avec Git/GitHub

---

## 🧠 Workflow du projet

### 1. Acquisition & exploration de données

- Étude des attributs catégoriels et numériques des Pals
- Identification des corrélations et valeurs aberrantes

### 2. Création de la base de données

Définition d'un schéma relationnel dans `palworld_database` incluant 6 tables :

- `combat_attribute`
- `job_skill`
- `hidden_attribute`
- `refresh_area`
- `ordinary_boss_attribute`
- `tower_boss_attribute`

### 3. Nettoyage & normalisation

- Gestion des valeurs manquantes
- Nettoyage de doublons
- Préparation pour l’import SQL

### 4. Analyse exploratoire

- Visualisation de distributions et de tendances
- Étude croisée des attributs de combat et de travail
- Résumés graphiques des capacités dominantes

### 5. Développement de l'application Streamlit

- Interface interactive (`app/app.py`)
- Graphiques et filtres en temps réel
- Accessible à tout utilisateur sans compétence technique

---

## 📁 Structure du projet

pals-analysis/
├── app/ # Interface utilisateur (Streamlit)
│ └── app.py
├── data/ # Données brutes et nettoyées
│ └── .keep
├── database/ # Scripts SQL pour la base MariaDB
│ └── .keep
├── notebooks/ # Analyses exploratoires (Jupyter)
│ └── .keep
├── src/ # Code Python (fonctions, utilitaires)
│ └── init.py
├── requirements.txt # Dépendances Python
├── .gitignore # Fichiers à ignorer
└── README.md # Présentation du projet


---

## 🛠️ Technologies utilisées

| Technologie    | Rôle                                   |
|----------------|----------------------------------------|
| Python         | Analyse de données & scripting         |
| Jupyter        | Exploration et documentation           |
| SQL (MariaDB)  | Stockage structuré et interrogation     |
| Streamlit      | Interface web interactive               |
| Git/GitHub     | Suivi de version et collaboration       |

---

## 🚀 Installation

```bash
# Cloner le projet
git clone https://github.com/Paul-Emmanuel-Buffe/pals-analysis.git
cd pals-analysis

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # (ou venv\Scripts\activate sous Windows)

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'app Streamlit
streamlit run app/app.py

📦 Livrables attendus

    📘 Jupyter Notebook complet retraçant l’analyse

    🌐 Application Streamlit interactive

    🧾 Scripts SQL pour générer et alimenter la base

    🎞️ Présentation finale du projet
