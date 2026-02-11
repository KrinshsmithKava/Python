import requests

url = "https://api.yelp.com/v3/businesses/seaarch"
api_key = "TvEQDsOs9Gm"
headers = {
    "Authorization": "Bearer " + api_key
}
response = requests.get(url, headers=headers)
print(response.text)
