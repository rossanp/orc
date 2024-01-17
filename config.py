import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')

#Criando as tabelas
# Tabela Categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Tabela Sub_Categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE SubCategoria(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, categoria_id INTEGER, nome TEXT, FOREIGN KEY(categoria_id) REFERENCES Categoria(id))")
    
# Tabela Banco
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Banco(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT, saldoinicial Numeric(10,2))")
    
# Tabela Lançamento
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Lancamento(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, categoria_id INTEGER, subcategoria_id INTEGER, banco_id INTEGER, data DATE, descricao TEXT, valor DECIMAL, tipo TEXT, FOREIGN KEY(categoria_id) REFERENCES Categoria(id), FOREIGN KEY(subcategoria_id) REFERENCES SubCategoria(id), FOREIGN KEY(banco_id) REFERENCES Banco(id))")