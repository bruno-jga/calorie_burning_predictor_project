import requests

url = 'http://localhost:9696/predict'

physical_activity = {
    "avg_bpm":140,
    "resting_bpm": 45,
    "session_duration_(hours)": 1,
    "fat_percentage":10,
    "water_intake_(liters)":1,
    "workout_frequency_(days/week)":5,
    "experience_level":3,
    "bmi":25,
    "gender":"male"
}

print(requests.post(url, json=physical_activity).json())