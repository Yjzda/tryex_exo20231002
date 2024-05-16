import psycopg2
import random


db_params = {
    "host": "localhost",  # The Docker host name
    "port": 5432,         # The port mapped to the PostgreSQL container in the Docker Compose file
    "database": "postgres",
    "user": "postgres",
    "password": "mdp",
}



try:
  
    conn = psycopg2.connect(**db_params)
    print(conn)

    cursor = conn.cursor()
    print(cursor)

    cursor.execute("SELECT * FROM table_exo2_postgre_docker")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except psycopg2.OperationalError as e:
    print(f"Error connecting to the database: {e}")

except psycopg2.Error as e:
    print(f"Database error: {e}")

finally:
   
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()






