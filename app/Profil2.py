import streamlit as st
import streamlit as st
import pandas as pd
import mariadb as mb

def get_connection():
    try:
        conn = mb.connect(
            user='root',
            password='cN06+#P34',
            host='localhost',
            port=3307,
            database='palworld_database'
        )
        return conn
    except mb.Error as e:
        print(f"Erreur de connexion : {e}")
        return None

def fetch_data1(conn):
    query = """
    select chinese_name, (make_a_fire+watering+planting+generate_electricity+manual+collection+ logging+ mining+pharmaceutical+pasture+carry) as total_skills, make_a_fire, watering, planting, generate_electricity, manual, collection, logging, mining, pharmaceutical, pasture, carry 
    from job_skills 
    inner join palu_refresh_level as prl  
    on chinese_name= prl.name 
    where refresh_area = "grassland" 
    order by total_skills desc limit 7;
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    return df

def fetch_data2(conn):
    query = """select chinese_name, (make_a_fire+watering+planting+generate_electricity+manual+collection+ logging+ mining+pharmaceutical+pasture+carry) as total_skills, make_a_fire, watering, planting, generate_electricity, manual, collection, logging, mining, pharmaceutical, pasture, carry 
    from job_skills 
    inner join palu_refresh_level as prl  
    on chinese_name= prl.name 
    where refresh_area = "grassland" 
    order by total_skills desc limit 1;
            """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    return df


st.title(" Profil #2  Collecteur Polyvalent (Niv. 3-4)")


conn = get_connection()
if conn:
    df = fetch_data1(conn)
    dp = fetch_data2(conn)
    st.write("Données des meilleurs collecteur polyvalent dans la zone des grassland:")
    data = df['chinese_name'], df['total_skills']
    dg = df[['chinese_name', 'total_skills']].set_index('chinese_name')
    st.bar_chart(dg['total_skills'])
    st.title("Meilleur collecteur avec les differentes collecte qu'il peu faire")
    st.dataframe(dp)
    st.title("Analyse du meilleur cas de collecteur")
    st.markdown("""
                ### Feather Archer : le Pal collecteur le plus polyvalent en début de partie

**Feather Archer** est sans doute l’un des meilleurs choix de **Pal collecteur** pour bien démarrer votre aventure. Grâce à sa grande polyvalence, il peut remplir plusieurs rôles essentiels dès les premières heures de jeu :

- 🌲 Collecter du bois  
- 🔥 Allumer un feu de camp  
- 🪓 Couper du bois  
- 🧺 Transporter plusieurs objets d’un même élément  
- ❤️ Soigner les autres Pals  
- 🌱 Pratiquer l’agriculture  

---

Ces nombreuses capacités font de **Feather Archer** un excellent allié pour le début de partie.  
Cependant, à mesure que l’aventure progresse, il devient nécessaire de diversifier les Pals collecteurs. Notamment, dans les secteurs comme **l’exploitation minière**, d’autres Pals spécialisés seront indispensables pour augmenter l’efficacité de la collecte.

                """)
    conn.close()
else:
    st.error("Impossible de se connecter à la base.")