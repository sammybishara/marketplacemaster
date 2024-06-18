from website import Website
import requests
import json


class Mercari(Website):
    def __init__(self):
        super().__init__()

    def get_search_results(self, query):
        # Mercari api endpoint
        api_url = "https://www.mercari.com/v1/api"
        
        # Mercari endpoint for authentication token
        initalize_url = "https://www.mercari.com/v1/initialize"
        
        # headers to mimic browser request
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mercari/6.102.0 (com.mercariapp.mercari; build:102; iOS 14.4.2) Alamofire/4.9.1", 
        }
        
        # Get request for access token 
        response = requests.get(initalize_url, headers=headers)
        token = response.json()["accessToken"]
        
        # Add token to header
        headers["Authorization"] = f"Bearer {token}"
        
        # Define the payload (already URL-encoded)
        payload = {
            "operationName": "searchFacetQuery",
            "variables": {
                "criteria": {
                    "offset": 0,
                    "soldItemsOffset": 0,
                    "promotedItemsOffset": 0,
                    "sortBy": 0,
                    "length": 100,
                    "query": query,
                    "itemConditions": [],
                    "shippingPayerIds": [],
                    "sizeGroupIds": [],
                    "sizeIds": [],
                    "itemStatuses": [],
                    "customFacets": [],
                    "facets": [1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 16, 19],
                    "authenticities": [],
                    "deliveryType": "all",
                    "state": None,
                    "locale": None,
                    "shopPageUri": None,
                    "withCouponOnly": None,
                    "countrySources": [],
                    "showDescription": False,
                },
                "categoryId": 0,
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "2fd981e6c4573c3b9a63aedfc106c09f27f6800fa7117920f1f04a42c1f2a7f9",
                }
            },
        }

        # Make the POST request
        response = requests.post(api_url, json=payload, headers=headers)
        
        with open("mercari.json", "w") as f:
            json.dump(
                response.json(), f, indent=4
            )  # Indent parameter formats the JSON with 4 spaces


if __name__ == "__main__":
    m = Mercari()
    m.get_search_results("dead space steelbook")
