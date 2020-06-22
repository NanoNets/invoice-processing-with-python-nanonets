import requests, os
import json

api_key = os.environ.get('NANONETS_API_KEY')
invoice_model_id = "cc3330a2-acf6-4199-ba46-43a70a9ca337"
url = "https://app.nanonets.com/api/v2/miscroutes/lightclonemodel"

payload = json.dumps({"email": "sarthak@nanonets.com","model_id": invoice_model_id})
headers = {
  'Content-Type': 'application/json'  
}

response = requests.request("POST", url, headers=headers, data = payload, auth=(api_key, ''))

model_id = json.loads(response.text)["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/prediction.py ./images/1.png")