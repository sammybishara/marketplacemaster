from website import Website
import requests
import json
import os
from dotenv import load_dotenv
import base64

class Ebay(Website):
    def __init__(self) -> None:
        super().__init__()
        
        
    def get_search_results(self, query):
        # Api endpoint for authentication token
        auth_url = "https://api.ebay.com/identity/v1/oauth2/token"
      
        # Api endpoint for searches
        search_url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit=200"
        
        # load client id and client secret from .env
        load_dotenv()
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv("CLIENT_SECRET")
        
        # format credentials and convert to bytes
        auth_str = f"{client_id}:{client_secret}"
        auth_bytes = auth_str.encode("utf-8")
        base64_str = base64.b64encode(auth_bytes).decode("utf-8")
        
        auth_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {base64_str}"
        }
        
         # Set up the body of the request
        data = {
            'grant_type': 'client_credentials',
            'scope': 'https://api.ebay.com/oauth/api_scope'
        }
        
        response = requests.post(auth_url, headers=auth_headers, data=data)
        oauth_token = response.json()["access_token"]
        
        search_headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        
        response = requests.get(search_url, headers=search_headers)

        with open("ebay.json", "w") as f:
            json.dump(
                response.json(), f, indent=4
            )  # Indent parameter formats the JSON with 4 spaces

        
if __name__ == "__main__":
    e = Ebay()
    e.get_search_results("dead space steelbook")
        

