import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine, text

# === Titre et description ===
st.title("Profil #5 – Builder de Base (Niv. 10–12)")
st.markdown("""
### Objectif :
Optimiser la **construction** et **l’automatisation** de la base en early/mid game.  
Les Pals doivent être efficaces en **minage**, **artisanat**, **abattage**, **électricité** et **transport**.
""")

# === Connexion base de données ===
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 3307,
    'database': 'palworld_database'
}

@st.cache_resource
def get_engine():
    return create_engine(
        f"mysql+pymysql://{config['user']}:{config['password']}@"
        f"{config['host']}:{config['port']}/{config['database']}"
    )

engine = get_engine()

# === Requête SQL avec filtrage sur "Grassland" ===
query = """
SELECT 
    pca.name AS Nom,
    m.craftspeed AS Artisanat,
    m.Mining AS Minage,
    m.logging AS Abattage,
    m.generate_electricity AS Electricite,
    m.carry AS Transport,
    m.rarity AS Rareté,
    prl.refresh_area AS Zone,
    prl.minimum_level AS NiveauMin
FROM palu_combat_attribute pca
JOIN monsters m ON pca.id = m.id
JOIN palu_refresh_level prl ON pca.id = prl.id
WHERE prl.minimum_level BETWEEN 10 AND 12
  AND prl.refresh_area = 'Grassland'
  AND (m.craftspeed > 0 OR m.Mining > 0 OR m.logging > 0 OR m.generate_electricity > 0 OR m.carry > 0)
ORDER BY (m.craftspeed + m.Mining + m.logging + m.generate_electricity + m.carry) DESC
LIMIT 10;
"""

with engine.connect() as conn:
    df = pd.read_sql(text(query), conn)

st.subheader("Top 10 Pals pour le développement de base en Grassland")
st.dataframe(df, use_container_width=True)

# === Graphe visuel des compétences combinées ===
if not df.empty:
    df_viz = df.melt(
        id_vars=["Nom"],
        value_vars=["Artisanat", "Minage", "Abattage", "Electricite", "Transport"],
        var_name="Compétence",
        value_name="Niveau"
    )

    fig = px.bar(
        df_viz,
        x="Nom",
        y="Niveau",
        color="Compétence",
        barmode="stack",
        title="Polyvalence des Pals pour le Build",
        labels={"Nom": "Pal", "Niveau": "Niveau Compétence"}
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# === Recommandation stratégique ===
st.markdown("""
### Recommandations :
- **Favoriser la polyvalence** : Un Pal capable de faire plusieurs tâches rend votre base plus productive.
- **Utiliser Grassland intelligemment** : C’est une zone stable et riche, idéale pour établir une base.
- **Mixer spécialisation & multi-tâches** : Avoir un bon artisan + un bon transporteur = synergie gagnante.
""")
# --- Conclusion : Pal recommandé ---
st.markdown("---")
if not df.empty:
    meilleur_pal = df.iloc[0]
    st.success(f"**Pal Recommandé : {meilleur_pal['Nom']}**")
    st.markdown(f"""
    Ce Pal est le **plus polyvalent** parmi ceux disponibles dans **Grassland** pour la construction de base.
    
    **Résumé des compétences :**
    - Artisanat : `{meilleur_pal['Artisanat']}`
    - Minage : `{meilleur_pal['Minage']}`
    - Abattage : `{meilleur_pal['Abattage']}`
    - Électricité : `{meilleur_pal['Electricite']}`
    - Transport : `{meilleur_pal['Transport']}`
    
    Il combine **efficacité** et **accessibilité** dès le niveau `{meilleur_pal['NiveauMin']}`. Un **allié incontournable** pour bâtir une base solide dès le début du jeu !
    """)