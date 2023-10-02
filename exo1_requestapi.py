import requests

url="https://icanhazdadjoke.com"
response=requests.get(url)
try:
    response = requests.get(url, headers={"Accept": "application/json"})

    
    if response.status_code == 200:
        data = response.json()
        joke = data["joke"]
        print("Dad Joke:")
        print(joke)
    else:
        print(f"API request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")

except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")

except requests.exceptions.Timeout as e:
    print(f"Request timed out: {e}")


except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")







