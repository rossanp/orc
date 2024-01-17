import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')

# Inserção de dados------------------------------------

# Categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        item = "SELECT nome FROM Categoria WHERE nome = ?"
        cur.execute(item, (i,)) # Parâmetro passado em forma de tuplas
        result = cur.fetchall()
        if len(result)!=0:
            print("Categoria já existe.")
        else:
            #Insere a categoria
            query = "INSERT INTO Categoria (nome) VALUES (?)"
            cur.execute(query, (i,))
            print("Cadastro da Categoria feita!")

# inserir_categoria("Alimentação")
            
# Sub-categorias
def inserir_subCategoria(i, j):
    with con:
        cur = con.cursor()

        # Verifica se a categoria existe
        item = "SELECT id FROM subCategoria WHERE nome = ?"
        cur.execute(item, (j,))
        result = cur.fetchall()

        if len(result) != 0:
            print("Sub-Categoria já existe.")
        else:
            #Insere a sub-categoria
            query = "INSERT INTO SubCategoria (categoria_id, nome) VALUES (?, ?)"
            cur.execute(query, (i, j))
            print("Cadastro da Sub-Categoria feita!")

# inserir_subCategoria("Moradia", "Luz")

# Bancos
def inserir_banco(i):
    with con:
        cur = con.cursor()
        # Verifica se a categoria existe
        item = "SELECT nome FROM Banco WHERE nome = ?"
        cur.execute(item, (i,))
        result = cur.fetchall()

        if len(result)!=0:
            print("Categoria já existe.")
        else:
            #Insere o banco
            query = "INSERT INTO Banco (nome, saldoinicial) VALUES (?, 0.00)"
            cur.execute(query, (i,))
            print("Cadastro do Banco feito!")

# inserir_banco("Itaú")

# Lançamentos
def inserir_lancamento(i, j, k, l, m, n, o):
    with con:
        cur = con.cursor()
        
        #Insere o lançamento
        query = "INSERT INTO Lancamento (data, descricao, valor, tipo, categoria_id, subCategoria_id, banco_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (i, j, k, l, m, n, o))
        print("Cadastro de Lançamentos feitos!")


#inserir_lancamento("16/01/2024", "Saaetri", -24.63, "Despesa", "Moradia", "Luz", "Itaú")

# Deletar dados------------------------------------

# Deletar Categoria
def deletar_categoria(i):
    with con:
        cur = con.cursor()

        query = "DELETE FROM Categoria WHERE id = ?"
        cur.execute(query, (i,))
        print("Categoria deletada.")
        
# Deletar Sub-Categoria
def deletar_subCategoria(i):
    with con:
        cur = con.cursor()

        query = "DELETE FROM SubCategoria WHERE id = ?"
        cur.execute(query, (i,))
        print("Sub-Categoria deletada.")
        
# Deletar Banco
def deletar_banco(i):
    with con:
        cur = con.cursor()

        query = "DELETE FROM Banco WHERE id = ?"
        cur.execute(query, (i,))
        print("Banco deletado.")
        
# Deletar Lançamento
def deletar_lancamento(i):
    with con:
        cur = con.cursor()

        query = "DELETE FROM Lançamento WHERE id = ?"
        cur.execute(query, (i,))
        print("Lançamento deletado.")

#deletar_subCategoria(5)

# Ver Dados----------------------------------------

def ver_dados():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM SubCategoria")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

#print(ver_dados())