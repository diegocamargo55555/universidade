import requests
import json

# 1. Send the GET request
response = requests.get('https://substack.com/@daseintropical')

print(response.status_code)
# 2. Check if the request was successful
if response.status_code == 200:
    # 3. Parse the response as JSON
    data = response.json()
    
    # 4. Save to a file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
else:
    print("error ")
