import requests

FLASK_URL = 'http://127.0.0.1:5000' 

def get_pdf_location(employee_name):
    response = requests.get(f'{FLASK_URL}/employee/{employee_name}')
    if response.status_code == 200:
        return response.json().get('pdf_location') 
    else:
        return None