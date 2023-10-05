from flask import Flask, jsonify
import psycopg2  
app = Flask(__name__)

def create_table_if_not_exists():
    db_params = {
        "host": "localhost",  
        "port": 5433,         
        "database": "postgres",
        "user": "postgres",
        "password": "mdp",
    }
    conn = psycopg2.connect(**db_params)
    print(conn)

    # Create a cursor object
    cursor = conn.cursor()
    print(cursor)

    
    
    table_name = 'rfjeudi_datadb'
    
    # Créez un curseur pour exécuter une requête SQL
    cur = conn.cursor()

    # Check if the table exists, if not, create it
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            name TEXT,
            age INT,
            email TEXT
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()



def insert_sample_data():
    db_params = {
        "host": "localhost",  
        "port": 5433,         
        "database": "postgres",
        "user": "postgres",
        "password": "mdp",
    }
    conn = psycopg2.connect(**db_params)
    print(conn)

    # Create a cursor object
    cursor = conn.cursor()
    print(cursor)

    
    
    table_name = 'rfjeudi_datadb'
    
  
    cur = conn.cursor()
    
   
    data = [
        ('John', 30, 'john@example.com'),
        ('Alice', 25, 'alice@example.com'),
        ('Bob', 35, 'bob@example.com')
    ]
    
    cur.executemany(f'INSERT INTO {table_name} (name, age, email) VALUES (%s, %s, %s)', data)
    
    conn.commit()
    cur.close()
    conn.close()


def get_db_data():
    db_params = {
    "host": "localhost",  
    "port": 5433,         
    "database": "postgres",
    "user": "postgres",
    "password": "mdp",
    }
    conn = psycopg2.connect(**db_params)
    print(conn)

    # Create a cursor object
    cursor = conn.cursor()
    table_name = 'rfjeudi_datadb'
     
    # Exécutez une requête SQL pour récupérer les données de la table
    cursor.execute(f'SELECT * FROM {table_name}')
    
    # Récupérez toutes les lignes de résultat
    rows = cursor.fetchall()
    
    # Fermez le curseur et la connexion à la base de données
    cursor.close()
    conn.close()
    
    # Convertissez les données en une liste de dictionnaires
    data = []
    for row in rows:
        data.append({
            'colonne1': row[0],
            'colonne2': row[1],
            
        })
    
    return data

@app.route('/get_data', methods=['GET'])
def get_data_endpoint():
    create_table_if_not_exists() 
    insert_sample_data()
    data = get_db_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
