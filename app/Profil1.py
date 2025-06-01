import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine, text
import pandas as pd

# Configuration base de données
engine = create_engine("mysql+pymysql://root:cN06+#P34@localhost:3307/palworld_database")

# Titre principal
st.title("🌿 Pals en Grassland")

# Requête pour compter les Pals en Grassland
@st.cache_data
def count_grassland_pals():
    query = """
    SELECT prl.refresh_area, COUNT(*) AS total
    FROM palu_refresh_level prl
    JOIN palu_combat_attribute pca ON prl.name = pca.chinese_name
    WHERE prl.refresh_area = 'grassland' 
    AND prl.minimum_level BETWEEN 1 AND 4
    GROUP BY prl.refresh_area
    """
    with engine.connect() as conn:
        result = conn.execute(text(query)).fetchone()
        return result[1] if result else 0

# Affichage du résultat
total = count_grassland_pals()
st.subheader(f"Nombre de Pals en grassland (niveau 1-4) : {total}")

# Détails des Pals en Grassland avec rareté
@st.cache_data
def get_grassland_pals_with_rarity():
    query = """
    SELECT 
        prl.refresh_area, 
        pca.name AS pal_display_name, 
        pca.rarity,
        prl.minimum_level,
        prl.maximum_level
    FROM 
        palu_refresh_level prl
    JOIN 
        palu_combat_attribute pca 
        ON prl.name = pca.chinese_name
    WHERE 
        prl.refresh_area = 'grassland' 
        AND prl.minimum_level BETWEEN 1 AND 4
    ORDER BY 
        pca.rarity ASC, prl.minimum_level ASC
    """
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# Affichage des données
if total > 0:
    df = get_grassland_pals_with_rarity()

    # Nettoyage des lignes vides
    df.dropna(how='all', inplace=True)
    df.dropna(subset=['pal_display_name'], inplace=True)
    
    # Tableau simple des Pals
    st.subheader("Liste des Pals présents en grassland (niveau 1-4)")
    
    # Ajout de métriques (avec vérification des colonnes)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Niveau min moyen", f"{df['minimum_level'].mean():.1f}")
    with col2:
        st.metric("Niveau max moyen", f"{df['maximum_level'].mean():.1f}")
    
    if 'rarity' in df.columns:
        col3 = st.columns(1)[0]
        with col3:
            st.metric("Rareté moyenne", f"{df['rarity'].mean():.1f}")
    
    st.dataframe(
        df,
        height=500,
        use_container_width=True
    )

    
    
    
else:
    st.warning("Aucun Pal trouvé en grassland avec niveau minimum entre 1 et 4")
