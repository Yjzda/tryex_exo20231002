import psycopg2
import logging

logging.basicConfig(filename='postgre_setup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "mdp",
}

try:
    conn = psycopg2.connect(**db_params)

    cursor = conn.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'customer')")
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        create_table_sql = """
            CREATE TABLE customer (
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                age INT
            )
        """
        cursor.execute(create_table_sql)
        logging.info("Created the 'customer' table")


    insert_customer_sql = """
        INSERT INTO customer (firstname, lastname, age)
        VALUES ('Pedro', 'Salsa', 24)
    """
    cursor.execute(insert_customer_sql)
    logging.info("Inserted a customer record")

    # Commit the changes to the database
    conn.commit()

    # Log a success message
    logging.info("Database setup completed successfully")

except psycopg2.OperationalError as e:
  
    logging.error("Error connecting to the database: %s", e)

except psycopg2.Error as e:

    logging.error("Database error: %s", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
