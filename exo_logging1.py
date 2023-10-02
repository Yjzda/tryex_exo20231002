import requests
import logging


log_filename = "api_request.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the API URL
api_url = "https://icanhazdadjoke.com"

try:
    # Log that we are about to make the API request
    logging.info("Making API request to %s", api_url)

    # Send the API request
    response = requests.get(api_url)

    # Check if the API call was successful (status code 200)
    if response.status_code == 200:
        # Log that the API call was successful
        logging.info("API call succeeded")
        
        # Process the API response here if needed
        # Example: data = response.json()

    else:
        # Log an error message if the API call failed
        logging.error("API call failed with status code %d", response.status_code)

except requests.exceptions.RequestException as e:
    # Log an error if there was a request exception
    logging.error("API request error: %s", e)

except Exception as e:
    # Log any other unexpected exceptions
    logging.error("An unexpected error occurred: %s", e)

else:
    # This block will execute if no exceptions were raised
    logging.info("API request completed successfully")

# Close the log file
logging.shutdown()
