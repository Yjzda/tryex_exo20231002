import psycopg2
import logging
# Connection parameters
db_params = {
    "host": "localhost",     
    "port": 5432,         
    "database": "postgres",
    "user": "postgres",
    "password": "mdp",
}

try:
    # Create a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    cursor = conn.cursor()

    # Create the "customer" table
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS customer (
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            age INT
        )
    """
    cursor.execute(create_table_sql)

    # Insert a customer record
    insert_customer_sql = """
        INSERT INTO customer (firstname, lastname, age)
        VALUES ('Pedro', 'Salsa', 24)
    """
    cursor.execute(insert_customer_sql)

    # Commit the changes to the database
    conn.commit()

    # Log a success message
    logging.info("Database setup completed successfully")

except psycopg2.OperationalError as e:
    # Log an error message if there was a database connection issue
    logging.error("Error connecting to the database: %s", e)

except psycopg2.Error as e:
    # Log an error message for any other database-related errors
    logging.error("Database error: %s", e)

finally:
    # Close the cursor and connection in the 'finally' block to ensure they are always closed
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
