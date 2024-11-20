import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    key = 'API_KEY'
    query = request.args.get('query', 'awordforshownoresultsinthepage')
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        books = [
            {
                'title': book['volumeInfo'].get('title', 'Título não disponível'),
                'authors': book['volumeInfo'].get('authors', ['Autor não disponível']),
                'description': book['volumeInfo'].get('description', 'Descrição não disponível'),
            }
            for book in data.get('items', [])
        ]
    else:
        books = []

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)