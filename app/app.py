import streamlit as st

# Configuration de la page (doit être le premier appel Streamlit)
st.set_page_config(page_title="Optimisation Palworld", page_icon="🐉")

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
    st.title("🐉 Optimisation d'Équipe Palworld")
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

    À ce stade du jeu, les besoins sont multiples : disposer de Pals utiles à la **récolte rapide de ressources**, capables de **soutenir la production** sur la base (minage, agriculture, énergie), tout en assurant une **présence offensive** efficace pour les premiers combats. Il est également important d’avoir une **certaine robustesse défensive** pour protéger la base et sécuriser les premières zones d’exploration. L’équilibre entre ces rôles conditionne une montée en puissance fluide et stratégique.

    ## Méthodologie

    **Définition des KPI** : Métriques de combat, production et synergie d'équipe

    **Exploration approfondie des données** : Analyse des 6 datasets, preprocessing et identification des patterns

    **Analyse métier approfondie** : Compréhension des mécaniques de jeu, identification des besoins stratégiques 
    en Phase 1 et modélisation des synergies optimales

    ## Objectif

    Proposer une solution d'optimisation basée sur l'analyse quantitative des attributs et l'analyse métier 
    des synergies identifiées dans le dataset pour maximiser l'efficacité stratégique en début de partie.

    ---

    *Explorez nos recommandations via le menu de navigation.*
    """)

elif page == "Stratégie":
    exec(open('Strategie.py', encoding='utf-8').read())

elif page == "Profil 1":
    exec(open('Profil1.py', encoding='utf-8').read())

elif page == "Profil 2":
    exec(open('Profil2.py', encoding='utf-8').read())

elif page == "Profil 3":
    exec(open('Profil3.py', encoding='utf-8').read())

elif page == "Profil 4":
    exec(open('Profil4.py', encoding='utf-8').read())

elif page == "Profil 5":
    exec(open('Profil5.py', encoding='utf-8').read())
