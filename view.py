import sqlite3 as lite

# Criando conexão com o banco
con = lite.connect('dados.db')
cur = con.cursor()

item_categoria = "SELECT id FROM Categoria WHERE nome = ?"
item_subCategoria = "SELECT id FROM SubCategoria WHERE nome = ?"
item_banco = "SELECT id FROM Banco WHERE nome = ?"
item_lancamento = "SELECT id FROM Lancamento WHERE descricao = ?"

# Inserção de dados------------------------------------

# Categorias
def inserir_categoria(nome):
    with con:
        cur.execute(item_categoria, (nome,)) # Parâmetro passado em forma de tuplas
        result = cur.fetchall()
        # Verifica se a categoria existe
        if len(result)!=0:
            print("Categoria já existe.")
        else:
            #Insere a categoria
            query = "INSERT INTO Categoria (nome) VALUES (?)"
            cur.execute(query, (nome,))
            print("Cadastro da Categoria feita!")

#inserir_categoria("Investimento")
            
# Sub-categorias
def inserir_subCategoria(categoria,
                         novaSubCategoria):
    with con:
        cur.execute(item_subCategoria, (novaSubCategoria,))
        result_sub = cur.fetchall()
        cur.execute(item_categoria, (categoria,))
        result_cat = cur.fetchone()

        if len(result_cat) is not None:
            if len(result_sub) != 0:
                print("Sub-Categoria já existe.")
            else:
                #Insere a sub-categoria
                query = "INSERT INTO SubCategoria (categoria_id, nome) VALUES (?, ?)"
                cur.execute(query, (result_cat[0], novaSubCategoria))
                print("Cadastro da Sub-Categoria feita!")
        else:
            print("Categoria não existe.")

#inserir_subCategoria("Moradia", "Água")

# Bancos
def inserir_banco(nome):
    with con:
        cur.execute(item_banco, (nome,))
        result = cur.fetchall()

        if len(result)!=0:
            print("Categoria já existe.")
        else:
            #Insere o banco
            query = "INSERT INTO Banco (nome, saldoinicial) VALUES (?, 0.00)"
            cur.execute(query, (nome,))
            print("Cadastro do Banco feito!")

#inserir_banco("Bradesco")

# Lançamentos
def inserir_lancamento(data,
                       descricao,
                       valor,
                       tipo,
                       categoria,
                       subcategoria,
                       banco):
    with con:
        cur.execute(item_categoria, (categoria,))
        result_cat = cur.fetchone()
        cur.execute(item_subCategoria, (subcategoria,))
        result_sub = cur.fetchone()
        cur.execute(item_banco, (banco,))
        result_banco = cur.fetchone()

        if len(result_cat) and len(result_sub) and len(result_banco) is not None:
            #Insere o lançamento
            query = "INSERT INTO Lancamento (data, descricao, valor, tipo, categoria_id, subCategoria_id, banco_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cur.execute(query, (data, descricao, valor, tipo, result_cat[0], result_sub[0], result_banco[0]))
            print("Cadastro de Lançamentos feitos!")
        else:
            print("Valores invalidos.")

#inserir_lancamento("2024-01-16", "Saaetri", -24.63, "Despesa", "Moradia", "Luz", "Itaú")

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
        
# Alterar dados------------------------------------

# Alterar dados da categoria
def alterar_categoria(i, j):
    with con:
        cur = con.cursor()
        query = "SELECT nome FROM Categoria WHERE nome = ?"
        cur.execute(query, (j,))
        result = cur.fetchall()
        if len(result) != 0:
            cur.execute(query, (i,))
            result1 = cur.fetchall()
            if len(result1) == 0:
                query = "UPDATE Categoria SET nome = ? WHERE nome = ?"
                cur.execute(query, (i, j))
                print("Categoria alterada.")
            else:
                print("Categoria já existe")
        else:
            print("Categoria não existe")

#alterar_categoria("Pessoal", "Tecnologia")
            
# Alterar dados da sub-categoria
def alterar_subCategoria(i, j):
    with con:
        cur = con.cursor()
        query = "SELECT nome FROM SubCategoria WHERE nome = ?"
        cur.execute(query, (j,))
        result = cur.fetchall()
        if len(result) != 0:
            cur.execute(query, (i,))
            result1 = cur.fetchall()
            if len(result1) == 0:
                query = "UPDATE SubCategoria SET nome = ? WHERE nome = ?"
                cur.execute(query, (i, j))
                print("Sub-Categoria alterada.")
            else:
                print("Sub-Categoria já existe", result)
        else:
            print("Sub-Categoria não existe", result)

#alterar_subCategoria("Internet", "Presente")
            
# Alterar dados do banco
def alterar_banco(nome_novo, valor_novo, nome):
    with con:
        cur = con.cursor()
        """ query_nome = "SELECT nome FROM Banco WHERE nome = ?" """
        """ query_valor = "SELECT saldoinicial FROM Banco WHERE nome = ?" """
        """ cur.execute(query_nome, (nome,)) """
        """ result_nome = cur.fetchall() """
        """ cur.execute(query_valor, (nome,))
        result_valor = cur.fetchall() """
        """ if result_nome != 0: """
        query_novoNome = "UPDATE Banco SET nome = ? WHERE nome = ?"
        query_novoValor = "UPDATE Banco SET saldoinicial = ? WHERE nome = ?"
        cur.execute(query_novoValor, (valor_novo, nome))
        cur.execute(query_novoNome, (nome_novo, nome))
        print("Banco alterado.")
        """ else: """
        #print("Dados incorretos. Não existe no Banco.")

#alterar_banco("Itaú", 500.00, "Itaú")
            
# Alterar dados do lançamento
def alterar_lancamento(novo_categoria,
                       nova_subCategoria,
                       novo_banco,
                       nova_data, 
                       nova_descricao,
                       novo_valor,
                       novo_tipo,
                       descricao):
    with con:
        cur = con.cursor()


# Ver Dados----------------------------------------

# Ver Categoria
def ver_dadosCategoria():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

# Ver Sub-Categoria
def ver_dadosSubCategoria():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM SubCategoria")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

# Ver Bancos
def ver_dadosBanco():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Banco")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

# Ver Lançamentos
def ver_dadosLancamento():
    lista = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Lancamento")
        linha = cur.fetchall()
        for l in linha:
            lista.append(l)

    return lista

print(ver_dadosLancamento())