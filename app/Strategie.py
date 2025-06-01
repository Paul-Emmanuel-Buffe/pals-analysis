import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine, text
import pandas as pd

# Configuration de la base de données
config = {
    'user': 'root',
    'password': 'cN06+#P34',
    'host': 'localhost',
    'port': 3307,
    'database': 'palworld_database'
}

# Connexion à la base (cache la ressource pour éviter reconnections inutiles)
@st.cache_resource
def get_engine():
    return create_engine(
        f"mysql+pymysql://{config['user']}:{config['password']}@"
        f"{config['host']}:{config['port']}/{config['database']}"
    )

engine = get_engine()

@st.cache_data(ttl=3600)  # cache 1h
def load_data():
    query = """
    SELECT 
        refresh_area AS Zone,
        COUNT(*) AS `Nombre de Pals`,
        ROUND(COUNT(*)/(SELECT COUNT(*) FROM palu_refresh_level)*100, 1) AS `Part (%)`
    FROM palu_refresh_level
    GROUP BY refresh_area
    ORDER BY COUNT(*) DESC;
    """
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

df = load_data()

st.title("📊 Stratégie : Grass Land")
st.markdown("**Distribution des Pals par zone de réapparition**")

# Palette adaptée au nombre de barres
colors = px.colors.sequential.Viridis[:len(df)]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Zone'],
    y=df['Nombre de Pals'],
    marker=dict(
        color=colors,
        line=dict(color='#1a1a1a', width=1)
    ),
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Quantité: %{y}<br>"
        "Part: %{customdata[0]}%"
        "<extra></extra>"
    ),
    customdata=df[['Part (%)']],
    name=''
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title=None,
        tickfont=dict(size=12),
        gridcolor='lightgray'
    ),
    yaxis=dict(
        title=dict(
            text="Nombre de Pals",
            font=dict(size=14)
        ),
        gridcolor='lightgray'
    ),
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ),
    margin=dict(l=20, r=20, t=60, b=20),
    height=400
)

fig.add_annotation(
    text=f"Total Pals : {df['Nombre de Pals'].sum()}",
    xref="paper", yref="paper",
    x=0.9, y=1.1,
    showarrow=False,
    font=dict(size=12)
)

col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Zones uniques", len(df))
    st.metric("Pals total", df['Nombre de Pals'].sum())

with st.expander("🔍 Voir les données détaillées"):
    st.dataframe(
        df.sort_values("Nombre de Pals", ascending=False),
        column_config={
            "Part (%)": st.column_config.ProgressColumn(
                format="%.1f%%",
                min_value=0,
                max_value=100
            )
        },
        hide_index=True,
        use_container_width=True
    )



# --- AJOUT : Calcul et affichage de la rareté moyenne par zone ---

@st.cache_data(ttl=3600)
def load_rarity_by_zone():
    query = """
    SELECT 
        prl.refresh_area AS Zone,
        ROUND(AVG(pca.rarity), 2) AS rarete_moyenne
    FROM palu_refresh_level prl
    JOIN palu_combat_attribute pca ON prl.id = pca.id
    WHERE prl.min_level BETWEEN 1 AND 12
    GROUP BY prl.refresh_area
    ORDER BY rarete_moyenne DESC;
    """
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)


df_rarity = load_rarity_by_zone()

st.markdown("---")
st.markdown("**Rareté moyenne des Pals ayant un niveau min entre 1-12 par zone géographique**")

fig2 = px.bar(
    df_rarity,
    x='Zone',
    y='rarete_moyenne',
    color='rarete_moyenne',
    color_continuous_scale='Viridis',
    labels={'rarete_moyenne': 'Rareté Moyenne', 'Zone': 'Zone'},
    title="Rareté moyenne par zone"
)
fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=40, b=20),
    height=400
)

st.plotly_chart(fig2, use_container_width=True)

with st.expander("🔍 Détails de la rareté moyenne par zone"):
    st.dataframe(df_rarity, use_container_width=True)

st.markdown("### Ce que l'analyse métier nous a révélé :")
st.markdown("""
- Paysages dégagés, sans massifs montagneux, donc avec une bonne visibilité et accessibilité. Ce qui facilite la capture.
- Zones géographiques riches en ressources clés (bois, pierre, nourriture)  
- Faible dangerosité en early game, permettant une progression sécurisée
""")

