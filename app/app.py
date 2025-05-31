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
    st.title("Optimisation Grassland - Phase 1")
    st.write("""
    Bienvenue ! Cette application vous guide dans l’optimisation de votre équipe en zone Grassland pour une progression rapide et sûre.

    Explore les stratégies et les profils recommandés via le menu de gauche.
    """)

elif page == "Stratégie":
    st.title("Stratégie d’Optimisation – Grassland Phase 1")
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
