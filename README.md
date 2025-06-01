📊 Pals Analysis

Pals Analysis est un projet d'analyse de données centré sur les créatures du jeu Palworld (ou Eidolon Parlu), combinant modélisation de base de données, exploration statistique, visualisation interactive et développement web. Ce projet vise à tirer des enseignements stratégiques à partir des attributs comportementaux et statistiques des "Pals".
🎓 Objectifs pédagogiques

Ce projet est réalisé dans un cadre de formation en Data & IA, avec les objectifs suivants :

    Concevoir un schéma relationnel normalisé avec MariaDB.

    Réaliser une exploration de données (EDA) avec Jupyter Notebook.

    Créer une interface interactive avec Streamlit.

    Pratiquer la gestion de version Git/GitHub et la documentation technique.

🧠 Workflow du projet
1. 🔍 Exploration du dataset

    Analyse de la structure des données sur les "Pals".

    Identification des types de variables (catégorielles, numériques).

    Détection de valeurs manquantes, outliers et distributions.

2. 🧱 Modélisation de base de données (MariaDB)

Création d'une base de données palworld_database avec 6 tables :

    combat_attribute

    job_skill

    hidden_attribute

    refresh_area

    ordinary_boss_attribute

    tower_boss_attribute

Objectifs : normalisation des données, structuration relationnelle claire, et optimisation des requêtes SQL.
3. 🧼 Nettoyage & Préparation

    Suppression des doublons et anomalies.

    Traitement des valeurs nulles.

    Intégration dans la base via des scripts SQL (à venir dans database/).

4. 📈 Analyse exploratoire (Jupyter Notebooks)

    Étude des corrélations entre attributs de combat et rôles de travail.

    Visualisation de la répartition des capacités.

    Représentations graphiques pour guider les choix de jeu.

5. 🌐 Application interactive (Streamlit)

    Développement dans app/app.py.

    Interface utilisateur pour requêtes dynamiques et graphiques en temps réel.

    Permet aux joueurs et analystes d’explorer visuellement les données sans coder.

🗂️ Structure du projet

pals-analysis/
├── app/                  # Application Streamlit (app.py)
├── data/                 # Données brutes / nettoyées (.csv, .json, etc.)
├── database/             # Scripts SQL pour la BDD MariaDB
├── notebooks/            # EDA en Jupyter Notebooks
├── src/                  # Code source modulaire (utils, requêtes SQL, etc.)
├── requirements.txt      # Dépendances Python
├── .gitignore            # Fichiers ignorés par Git
└── README.md             # Ce fichier

💻 Technologies utilisées
Outil	Rôle
Python	Traitement, scripting, visualisation
Jupyter	Analyse exploratoire
MariaDB	Base relationnelle & requêtes SQL
Streamlit	Application web interactive
Git / GitHub	Versioning, collaboration
🚀 Mise en place

    Cloner le dépôt

git clone https://github.com/Paul-Emmanuel-Buffe/pals-analysis.git
cd pals-analysis

Créer l'environnement virtuel

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Installer les dépendances

pip install -r requirements.txt

Configurer la base de données

    Installer MariaDB.

    Exécuter les scripts dans database/ (à venir).

    Se connecter à la base palworld_database.

Lancer l'application Streamlit

    streamlit run app/app.py

📦 Livrables attendus

    📘 Jupyter Notebook avec l'analyse complète et justifications

    🌐 Application web fonctionnelle (Streamlit)

    📁 Dépôt GitHub structuré et documenté

    🎞️ Diaporama de présentation du projet et des résultats
