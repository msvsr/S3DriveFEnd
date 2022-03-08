import requests


def to_s3(data):
    file = data.get('filetoupload')
    key = file._get_name()

    url = f'https://wzi3q87r97.execute-api.us-east-1.amazonaws.com/v1/getpresignedurl/{key}'
    pre_signed_url_data = requests.get(url).json().get('URL and Fields', '')

    if pre_signed_url_data:
        files = {'file': (key, file.open())}
        requests.post(pre_signed_url_data['url'], data=pre_signed_url_data['fields'], files=files)



