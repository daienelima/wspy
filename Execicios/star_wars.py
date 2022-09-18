import requests

url = 'https://swapi.dev/api/people/4/'
req = requests.get(url)

print(req.status_code)

dados = req.json()
print(dados['name'])
print(dados['height'])
print(dados['mass'])
print(dados['birth_year'])
