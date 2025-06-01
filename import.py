import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='cN06+#P34',  # Remplacez par votre mot de passe réel
            host='localhost',
            port=3307,
            database='palworld_database'  # Vérifiez que cette base existe
        )
        
        if conn.is_connected():
            print("✅ Connexion réussie à MariaDB !")
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"Version de MariaDB : {version[0]}")
            
    except Error as e:
        print(f"❌ Erreur de connexion : {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connexion fermée.")

test_connection()