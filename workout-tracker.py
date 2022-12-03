import requests
from datetime import datetime
#ADD YOUR API KEYS AND AUTH TOKENS
nutrionix_API =""
nutrionix_APPID =""
GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = "178"
AGE ="20"
exercise_endpoint =""
add_endpoints = ""
exercise_text = input("Tell me what exercise did you do :")
exercise_params ={
    "query":"exercise_text",
    "gender": "male"
}

exercise_headers = {
    "x-app-id" : nutrionix_APPID,
    "x-app-key": nutrionix_API,

}

response = requests.post(url=exercise_endpoint,json=exercise_params, headers=exercise_headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d%m%Y")
time_now = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs ={
        "workout":{
            "date":today_date,
            "time":time_now,
            "exercise":exercise['name'].title(),
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories'],
        }
    }

sheet_response = requests.post(url=add_endpoints, json = sheet_inputs)
print(sheet_response.text)
