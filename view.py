import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')

# Inserção de dados

#Categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES(?)"
        cur.execute(query, i)

inserir_categoria(["Alimentação"])