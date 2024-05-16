from flask import Flask, request, jsonify
import logging
from database import query_customer_age, DatabaseError


controller_logger = logging.getLogger('controller')
controller_logger.setLevel(logging.INFO)  # Set the log level to INFO for this module

app = Flask(__name__)

@app.route('/get_customer_age', methods=['GET'])
def get_customer_age():
    try:
        customer_name = request.args.get('name')
        age = query_customer_age(customer_name)
        controller_logger.info(f"Retrieved age for customer '{customer_name}'")
        return jsonify({'age': age})

    except DatabaseError as e:
        controller_logger.error("Database error: %s", e)
        return jsonify({'error': 'An internal issue occurred. Please contact the team in charge of the API.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
