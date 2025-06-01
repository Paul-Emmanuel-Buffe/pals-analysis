import streamlit as st
import pandas as pd
import mariadb as mb


def get_connection():
    try:
        conn = mb.connect(
            user="root",
            password="root",
            host="localhost",
            port=3307,
            database="palworld_database"
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
# 🎯 Stratégie de Capture Optimale : Quel Pal choisir ?

D’après les données analysées, **Anubis** semble initialement être un bon choix pour ce rôle. Cependant, une évaluation plus stratégique révèle un candidat encore plus adapté…

---

## 🧠 Le meilleur Pal pour la **capture prolongée**

Malgré une attaque plus faible, **Knight of Light** se révèle être **le choix optimal** pour maximiser les sessions de capture.

### ⚖️ Pourquoi privilégier Knight of Light pour la capture ?

Sa robustesse en fait un atout majeur :

- Une **défense** nettement supérieure
- Un **HP élevé**, garantissant une **longévité en combat**

Ces qualités assurent une **présence prolongée sur le terrain**, idéale pour :

- Enchaîner les combats sans interruption
- **Capturer plusieurs Pals d'affilée** sans risquer l'épuisement
- Optimiser l’**XP par session de capture**

---

## 🏆 Conclusion : Le champion de la capture

Avec sa **résistance accrue**, **Knight of Light** s’impose comme le **Pal parfait** pour une **stratégie de capture intensive**. Il est donc **le meilleur allié** pour les chasseurs de Pals en quête d'efficacité maximale !
""")
