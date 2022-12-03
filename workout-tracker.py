import requests
from datetime import datetime

nutrionix_API ="1b27e70bd82991518b16b6803f41ac79"
nutrionix_APPID ="41f58f64"
GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = "178"
AGE ="20"
exercise_endpoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
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

retrive_endpoints = "https://api.sheety.co/8c9a975e418b512cfe36c6ea240d2192/workoutTracker/workouts"
add_endpoints = "https://api.sheety.co/8c9a975e418b512cfe36c6ea240d2192/workoutTracker/workouts"
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