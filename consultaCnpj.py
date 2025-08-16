import requests
from pprint import pprint

#dados
cnpj = int(input("Insira o cnpj: "))
url = f'https://publica.cnpj.ws/cnpj/{cnpj}'

#requisição
response = requests.get(url)

#validação da url

if response.status_code==200:
    data = response.json()
    pprint(data)
else:
    print(f'Erro: {response.status_code}')
