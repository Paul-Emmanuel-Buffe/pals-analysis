import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Configuration
st.title(" Profil #4 – Monture Précoce (Niv. 7-10)")
st.markdown("""
### Objectif :
Optimiser la **mobilité** du joueur dès le niveau 7.  
Ce profil est essentiel pour **explorer rapidement la carte**, fuir le danger ou atteindre des ressources plus éloignées.
""")

# Connexion BDD
config = {
    'user': 'root',
    'password': 'cN06+#P34',
    'host': 'localhost',
    'port': 3307,
    'database': 'palworld_database'
}
engine = create_engine(f"mariadb+mariadbconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}")

# Récupération des Pals éligibles (niveau min 1-12, zone Grassland, vitesse dispo)
query = """
SELECT 
    pca.name, 
    pca.running_speed, 
    pca.riding_sprint_speed, 
    pca.endurance, 
    pca.rarity,
    prl.refresh_area,
    prl.minimum_level
FROM palu_combat_attribute pca
JOIN palu_refresh_level prl ON pca.id = prl.id
WHERE prl.minimum_level BETWEEN 1 AND 12
AND prl.refresh_area LIKE '%Grassland%'
AND pca.riding_sprint_speed IS NOT NULL
ORDER BY pca.riding_sprint_speed DESC
LIMIT 10;
"""
df = pd.read_sql(query, engine)

# Affichage principal
st.subheader("Top 10 des meilleures montures précoces (zone Grassland, Niv. 1-12)")
st.dataframe(df)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="name", y="riding_sprint_speed", ax=ax)
plt.xticks(rotation=45)
plt.title("Vitesse de sprint des meilleures montures précoces")
st.pyplot(fig)

# Recommandation stratégique
st.markdown("""
###  Recommandation stratégique (niveau 1-10)
Ces Pals sont fortement recommandés pour maximiser la mobilité dès les premiers niveaux.
""")
reco_df = df[df['minimum_level'] <= 10].head(2)
st.table(reco_df[['name', 'riding_sprint_speed', 'endurance', 'rarity']])

engine.dispose()
