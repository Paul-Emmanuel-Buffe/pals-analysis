import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine, text
import pandas as pd

# Configuration de la base de données
engine = create_engine("mysql+pymysql://root:cN06+#P34@localhost:3307/palworld_database")

# Titre de l'application
st.title("🌿 Pals en Grassland")

# Requête pour compter les Pals en grassland entre niveau 1 et 4
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

# Affichage du total
total = count_grassland_pals()
st.subheader(f"Nombre de Pals en grassland (niveau 1-4) : {total}")

# Requête détaillée des Pals en grassland
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

if total > 0:
    df = get_grassland_pals_with_rarity()

    # Nettoyage
    df.dropna(how='all', inplace=True)
    df.dropna(subset=['pal_display_name'], inplace=True)

    # Affichage des données
    st.subheader("Liste des Pals présents en grassland (niveau 1-4)")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Niveau min moyen", f"{df['minimum_level'].mean():.1f}")
    with col2:
        st.metric("Niveau max moyen", f"{df['maximum_level'].mean():.1f}")
    
    if 'rarity' in df.columns:
        st.metric("Rareté moyenne", f"{df['rarity'].mean():.1f}")

    st.dataframe(df, height=500, use_container_width=True)

noms_cibles = [
    "Lamball",
    "Chikipi",
    "Cattiva",
    "Pengullet",
    "Cremis",
    "Rushoar",
    "Sparkit",
    "Hoocrates",
    "Depresso",
    "Vixy"
]

@st.cache_data
def get_combat_stats(noms):
    placeholder = ",".join([f"'{nom}'" for nom in noms])
    query = f"""
    SELECT name, melee_attack, defense, HP, remote_attack
    FROM palu_combat_attribute
    WHERE name IN ({placeholder})
    """
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        return df

df_stats = get_combat_stats(noms_cibles)

if not df_stats.empty:
    try:
        df_stats['combat_score'] = df_stats[['melee_attack', 'defense', 'HP', 'remote_attack']].mean(axis=1)
    except KeyError as e:
        st.error(f"Colonne(s) manquante(s) : {e}")
        st.write("Colonnes disponibles :", df_stats.columns.tolist())
    else:
        df_stats.sort_values('combat_score', ascending=False, inplace=True)

        # Graphique score moyen
        fig = px.bar(
            df_stats,
            x='name',
            y='combat_score',
            labels={'name': 'Nom du Pal', 'combat_score': 'Score moyen'},
            title="📊 Score moyen de melee_attack, defense, HP et remote_attack",
            color='combat_score',
            color_continuous_scale='Plasma'
        )
        st.plotly_chart(fig, use_container_width=True)

        # -------------------------------
        # Affichage tableau stats détaillées pour 4 pals
        pals_selected = ["pengullet", "hoocrates", "cremis", "rushoar"]
        df_selected = df_stats[df_stats['name'].isin(pals_selected)][
            ['name', 'melee_attack', 'defense', 'HP', 'remote_attack']
        ].set_index('name')

        st.write("### 📋 Stats détaillées des Pals sélectionnés")
        st.dataframe(df_selected.style.format("{:.1f}"))

else:
    st.warning("Aucun Pal trouvé avec les noms spécifiés.")

st.markdown("## Nos recommandations")

st.markdown("""
Après analyse des statistiques de combat, nous recommandons **Pengullet**.  
Bien que Pengullet puisse sembler moins puissant que Rushoar, Cremis ou Hoocrates, sa capacité à atteindre le niveau 45 lui confère un avantage important sur le long terme.  
Cet avantage compense une légère perte initiale en combat par rapport aux autres pals, car l'investissement du joueur dans Pengullet est moins susceptible d'être rapidement perdu.  
De plus, Pengullet possède une valeur de **remote_attack** supérieure à celle de ses concurrents, renforçant son utilité stratégique à distance.  
Ainsi, Pengullet offre un bon équilibre entre progression et performance, ce qui en fait un choix pertinent pour les joueurs engagés.
""")
