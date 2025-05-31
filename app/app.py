import streamlit as st

# Barre latérale de navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choisis une page :", [
    "Accueil",
    "Stratégie",
    "Profil 1",
    "Profil 2",
    "Profil 3",
    "Profil 4",
    "Profil 5"
])

# Affichage du contenu selon la page
if page == "Accueil":
    st.title("Optimisation d'Équipe Palworld")
    st.subheader("Analyse Data-Driven pour la Formation d'Équipes Équilibrées")
    
    st.markdown("""
    ## Problématique
    
    Définir une équipe idéale et équilibrée de 5 Pals basée sur l'analyse des données fournies 
    pour une évolution optimale dans le jeu. Nous avons choisi de nous placer dans une situation 
    arbitraire : **la Phase 1 du jeu**.
    
    ## Contexte Stratégique
    
    Le but n'est pas seulement de former une équipe idéale de 5 Pals, mais s'inscrit dans une 
    **réelle stratégie qui permet de débuter de manière optimale** dans ce jeu. Cette approche 
    Phase 1 vise à établir les fondations d'une progression durable et efficace.
    
    ## Méthodologie
    
    **Définition des KPI** : Métriques de combat, production et synergie d'équipe
    
    **Exploration des données** : Analyse des 6 datasets, preprocessing et identification des patterns
    
    **Analyse métier** : Segmentation des profils, modélisation des besoins et optimisation multi-critères
    
    ## Objectif
    
    Proposer une solution d'optimisation basée sur l'analyse quantitative des attributs et synergies 
    identifiés dans le dataset pour maximiser l'efficacité stratégique en début de partie.
    
    ---
    *Explorez nos recommandations via le menu de navigation.*
    """)

elif page == "Stratégie":
    st.title("Stratégie d'Optimisation – Grassland Phase 1")
    st.write("Contenu à venir...")

elif page == "Profil 1":
    st.title("Profil 1 – Garde-Combat Efficace (Niveau 2-3)")
    st.write("Contenu à venir...")

elif page == "Profil 2":
    st.title("Profil 2 – Collecteur Polyvalent (Niveau 3-4)")
    st.write("Contenu à venir...")

elif page == "Profil 3":
    st.title("Profil 3 – Capture XP Multi-Cibles (Niveau 4-6)")
    st.write("Contenu à venir...")

elif page == "Profil 4":
    st.title("Profil 4 – Monture Précoce (Niveau 7-10)")
    st.write("Contenu à venir...")

elif page == "Profil 5":
    st.title("Profil 5 – Builder de Base (Niveau 10-12)")
    st.write("Contenu à venir...")