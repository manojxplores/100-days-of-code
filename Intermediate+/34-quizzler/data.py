import requests

params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}

res = requests.get("https://opentdb.com/api.php", params=params)
res.raise_for_status()
data = res.json()["results"]

question_data = data
