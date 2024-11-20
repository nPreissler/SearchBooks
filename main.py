import requests


search = input('Search for a book: ')

api_key = 'API_KEY'
query = search
url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Erro: {response.status_code}')

