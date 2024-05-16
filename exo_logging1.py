import requests
import logging


log_filename = "api_request.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_url = "https://icanhazdadjoke.com"

try:

    logging.info("Making API request to %s", api_url)


    response = requests.get(api_url)
    if response.status_code == 200:
    
        logging.info("API call succeeded")
        # Example: data = response.json()

    else:
        logging.error("API call failed with status code %d", response.status_code)

except requests.exceptions.RequestException as e:

    logging.error("API request error: %s", e)

except Exception as e:
  
    logging.error("An unexpected error occurred: %s", e)

else:

    logging.info("API request completed successfully")


logging.shutdown()
