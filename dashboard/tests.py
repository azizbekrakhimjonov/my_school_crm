from django.test import TestCase

import requests

api_url = 'http://127.0.0.1:8000/api/subjects/'
response = requests.get(api_url)
print(response.status_code)
print(response.json())
