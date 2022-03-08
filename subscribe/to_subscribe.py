import requests


def subscribe(data):
    email = data.get('subscriber')
    url = f'https://wzi3q87r97.execute-api.us-east-1.amazonaws.com/v1/subscribe/{email}'
    response = requests.post(url).json()
    return response.get('Message', '')

