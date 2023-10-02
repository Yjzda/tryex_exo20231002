import psycopg2
import logging

# Configure logging for database module
db_logger = logging.getLogger('database')
db_logger.setLevel(logging.ERROR)  # Set the log level to ERROR for this module

class DatabaseError(Exception):
    pass

def query_customer_age(customer_name):
    try:
        # Database connection parameters
        db_params = {
            "host": "localhost",
            "database": "postgres",
            "port": 5432,         
            "database": "postgres",
            "user": "postgres",
            "password": "mdp",
        }

        # Create a connection to the PostgreSQL database
        conn = psycopg2.connect(**db_params)

        # Create a cursor object
        cursor = conn.cursor()

        # Query the database to get the age of the customer
        cursor.execute("SELECT age FROM customer WHERE firstname = %s", (customer_name,))

        # Fetch the result
        age = cursor.fetchone()

        if age is not None:
            return age[0]  # Return the age as an integer

        # Raise a custom exception if the customer was not found
        raise DatabaseError(f"Customer '{customer_name}' not found in the database")

    except psycopg2.OperationalError as e:
        # Log the error and raise a custom exception for database connection issues
        db_logger.error("Database connection error: %s", e)
        raise DatabaseError("Database is not reachable. Please contact the team in charge of the API.")

    except psycopg2.Error as e:
        # Log the error and re-raise it for unknown database errors
        db_logger.error("Database error: %s", e)
        raise

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
