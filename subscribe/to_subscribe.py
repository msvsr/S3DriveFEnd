import requests


def subscribe(data):
    email = data.get('subscriber')
    url = f'https://gqj6fzcffi.execute-api.us-east-1.amazonaws.com/v1/subscribe/{email}'
    response = requests.post(url).json()
    return response.get('Message', '')

