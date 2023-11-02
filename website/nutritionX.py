import requests
import json


def find_nutrition(food_name):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

    headers = {
        'x-app-id' : 'd5bd0711',
        'x-app-key' : 'c8b6f411efafe4b2e15825983bb2352b'
    }
    
    parameters = {
        'query' : food_name
    }
    
    response = requests.post(url, headers=headers, json=parameters)
    return response.json()