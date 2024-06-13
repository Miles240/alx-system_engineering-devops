import requests
import json

client_id = "E64cxcVmr8xoobi530hKug"
secret_key = "w_PgzYD3Bxst4NlZlC3TfTBL8ubfDA"
auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
data = {"grant_type": "password", "username": "bg_miles", "password": "scombone240"}
headers = {"User-Agent": "Custom"}

res = requests.post(
    "https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers
)
TOKEN = res.json()["access_token"]

if TOKEN:
    # Add the access token to the headers
    headers["Authorization"] = f"bearer {TOKEN}"

    # Make a request to the Reddit API using the access token
    respond = requests.get(
        "https://oauth.reddit.com/r/webdev/comments/1ddbewt/even_apple_makes_mistakes",
        headers=headers,
    )

    # Print the response JSON for debugging
    with open("file.json", "w", encoding="utf-8") as file:
        json.dump(respond.json(), file)
    # print(len(respond.json()))
else:
    print("Failed to obtain access token")
