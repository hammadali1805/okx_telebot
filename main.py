import requests
import hashlib
import hmac
import base64
from datetime import datetime, timezone
import urllib.parse
import json

# Define your variables
apiKey = '827b45e0-699b-4d63-928e-49f239c3908c'
secretKey = 'E01A9D94802F38389287E2B9E663C71F'
passphrase = 'Okxbrc20!'
timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat() + 'Z' # Construct the timestamp in UTC timezone
# Define your method and params
method = 'GET'  # or 'POST'
endpoint = 'api/v5/mktplace/nft/ordinals/listings'
params = {}  

query_string = ''

if method == 'GET' and params:
    query_string = '?' + urllib.parse.urlencode(params)
elif method == 'POST' and params:
    query_string = json.dumps(params)

# Construct the message to be hashed
message = timestamp + method + endpoint + query_string

# Hash the message using HMAC SHA256
hashed_message = hmac.new(secretKey.encode(), message.encode(), hashlib.sha256)

# Encode the hashed message to base64
signature = base64.b64encode(hashed_message.digest()).decode()

# Construct headers
headers = {
    'Content-Type': 'application/json',
    'OK-ACCESS-KEY': apiKey,
    'OK-ACCESS-SIGN': signature,
    'OK-ACCESS-TIMESTAMP': timestamp,
    'OK-ACCESS-PASSPHRASE': passphrase
}

# Make your HTTP request using the requests library
url = f'https://www.okx.com/{endpoint}'
response = requests.post(url, headers=headers)

# Handle the response as needed
print(response.json)
