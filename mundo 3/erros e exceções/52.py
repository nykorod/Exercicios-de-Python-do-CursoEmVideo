import requests

def siteon(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code < 400
    except requests.exceptions.RequestException:
        return False

url = 'https://www.pudim.com.br'
if siteon(url):
    print('site acessivel')
else:
    print('site inacessivel')

