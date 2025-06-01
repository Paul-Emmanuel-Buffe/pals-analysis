import streamlit as st
import pandas as pd
import mariadb as mb

import mysql.connector as mb  # Assure-toi d’avoir cet import

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
    select chinese_name, damage_multiplier, remote_attack, HP, defense, catch_rate 
    from palu_combat_attribute 
    inner join palu_refresh_level as prl 
    on chinese_name= prl.name where refresh_area = "grassland" and catch_rate >=1 and remote_attack >= 110 and catch_rate >=0.5 
    order by remote_attack desc limit 5;
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    return df


st.title("🎯 Profil #3 – Capture XP Multi-Cibles (Niv. 4-6)")


conn = get_connection()
if conn:
    df = fetch_data1(conn)
    st.write("Données des meilleurs capture xp Multi-cibles dans la zone des grassland:")
    st.dataframe(df)

st.markdown("""
# 🤔 Choix du Pal optimal

D'après les données filtrées, **Anubis** semble être le Pal idéal pour ce rôle.

---

## 🧠 Analyse stratégique : Quel est réellement le meilleur choix ?

En réalité, **Knight of Light** pourrait s’avérer être un choix plus optimal, et ce, malgré une attaque plus faible qu’Anubis.

### Pourquoi privilégier Knight of Light ?

Il se distingue par une meilleure polyvalence grâce à :

- Une **défense** plus élevée
- Un **HP** supérieur

### 🎯 Conclusion

Grâce à sa robustesse (défense + HP), **Knight of Light** pourra rester actif plus longtemps en combat. Cela permet une **durée de capture prolongée**, ce qui en fait un excellent choix pour la stratégie de capture XP multi-cibles.
""")