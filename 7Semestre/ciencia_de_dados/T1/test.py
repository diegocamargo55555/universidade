import json

import serpapi

client = serpapi.Client(api_key="3ea5d182282942a7355b9d38a88bf0dccb2ffd7b7211e104027260dba406c51f")
results = client.search({
  "engine": "google_finance",
  "q": "GOOGL:NASDAQ"
})