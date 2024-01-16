import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')

# Inserção de dados

# Categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        item = "SELECT nome FROM Categoria WHERE nome = ?"
        cur.execute(item, (i,))
        result = cur.fetchall()
        if len(result)!=0:
            print("Categoria já existe.")
        else:
            query = "INSERT INTO Categoria (nome) VALUES (?)"
            cur.execute(query, (i,))
            print("Cadastro da Categoria feita!")

# inserir_categoria("Alimentação")
            
# Sub-categorias
def inserir_subCategoria(i, j):
    with con:
        cur = con.cursor()

        # Verifica se a categoria existe
        item = "SELECT id FROM Categoria WHERE nome = ?"
        cur.execute(item, (i,))
        result = cur.fetchone()

        if len(result) is None:
            print("Categoria já existe.")
        else:
            #Insere a sub-categoria
            query = "INSERT INTO SubCategoria (categoria_id, nome) VALUES (?, ?)"
            cur.execute(query, (i, j))
            print("Cadastro da Sub-Categoria feita!")

#inserir_subCategoria("Moradia", "Luz")

""" Ver Dados
def ver_dados():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM SubCategoria")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

print(ver_dados()) """