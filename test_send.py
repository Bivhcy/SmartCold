import requests

url = "http://127.0.0.1:5000/sensor-data"

data = {
    "storage_id": 1,
    "device_id": 1,
    "temperature": 5.2,
    "humidity": 88,
    "gas": 170,
    "ethylene": 40,
    "smoke": 0,
    "door": False,
    "time": "2026-06-30 22:30:00"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())