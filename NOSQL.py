
import json
import csv

with open ( 'dados.JSON', 'r', encoding='utf-8') as file:
    data = json.load(file)

authors = []
author_id = 1
for books in data['Livros']:
    for author in books['Autores']:
        name = author['Nome']
        surname = author['Sobrenome']
        # Verifica se o autor já existe na lista de autores
        autor_existente = next((
            a for a in authors 
            if a['Name'] == name 
            and a['Surname'] == surname), None)
        
        if not autor_existente:
            authors.append({
                'AuthorID': author_id, 
                'Name': name, 
                'Surname': surname})
            author_id += 1

# Cria tabela 
books = []
for book in data['Livros']:
    isbn = book['ISBN']
    preco = book.get('Preço', 0)  # define como 0 Se a chave 'Preço' não estiver presentr
    titulo = book['Título']
    authors_book = book['Autores']
    for autor in authors_book:
        author_id = next(
            a['AuthorID'] 
            for a in authors 
            if a['Name'] == author['Nome'] 
            and a['Surname'] == author['Sobrenome'])
        
        books.append({
            'ISBN': isbn, 
            'Price': preco, 
            'Title': titulo, 
            'AuthorID': author_id, 
            'Name': author['Nome'], 
            'Surname': autor['Sobrenome']})

# Salva dados das tabelas em um arquivo .csv
def write_csv(data, name_arquive):
    with open(name_arquive, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

write_csv(books, 'authors_and_books.csv')

print("Arquivo .csv foi criado com sucesso.")
