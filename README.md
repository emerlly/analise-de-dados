# 📚 Tabela de Livros e Autores (JSON → CSV)  

Este projeto converte um arquivo **JSON** contendo informações sobre livros e seus autores em um arquivo **CSV** estruturado. Ele evita duplicação de autores e cria um identificador único para cada um, facilitando o armazenamento e análise dos dados.  

---

## 🚀 **Como funciona?**  
1. **Lê o arquivo `dados.JSON`** contendo informações sobre livros e autores.  
2. **Gera uma lista de autores únicos**, atribuindo um **ID** para cada um.  
3. **Cria uma tabela de livros** com os dados formatados e associando os autores corretos.  
4. **Exporta os dados para um arquivo `authors_and_books.csv`**.  

---


## 🛠 **Requisitos**  

Certifique-se de ter **Python 3.x** instalado.  

### 📌 Instalação das dependências  
```bash
pip install -r requirements.txt
```
*(O projeto usa apenas bibliotecas padrão do Python, então esse passo pode ser opcional.)*  

---

## ▶ **Como Executar?**  
Basta rodar o script Python:  
```bash
python script.py
```

---

## 📥 **Exemplo de Entrada (`dados.JSON`)**  
```json
{
    "Livros": [
        {
            "ISBN": "12345",
            "Título": "Aprendendo Python",
            "Preço": 50.0,
            "Autores": [
                {"Nome": "João", "Sobrenome": "Silva"},
                {"Nome": "Maria", "Sobrenome": "Souza"}
            ]
        }
    ]
}
```

---

## 📤 **Exemplo de Saída (`authors_and_books.csv`)**  

| ISBN  | Price | Title              | AuthorID | Name  | Surname  |
|-------|-------|---------------------|----------|--------|----------|
| 12345 | 50.0  | Aprendendo Python   | 1        | João   | Silva    |
| 12345 | 50.0  | Aprendendo Python   | 2        | Maria  | Souza    |

---

## 🎯 **Objetivo do Projeto**  
✅ Converter **JSON → CSV**  
✅ Criar uma estrutura organizada para **livros e autores**  
✅ Facilitar a exportação dos dados para **planilhas ou bancos de dados**  

---

## 📜 **Licença**  
Este projeto está licenciado sob a **MIT License**.  

📌 **Sinta-se à vontade para contribuir!** 🚀
