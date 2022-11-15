import sqlite3
import random

Conexao = sqlite3.connect('Banco_Dados')
Cursor = Conexao.cursor()

Cursor.execute(
    'CREATE TABLE if not exists Minha_tabela1 (Data text, Nome text, Idade real)'
)

Conexao.commit()

# Inserindo valores
Cursor.execute('INSERT INTO Minha_tabela1 VALUES ("09/02/1999", "Victor", "23")')
Cursor.execute('INSERT INTO Minha_tabela1 VALUES ("17/06/1999", "Renan", "23")')
Cursor.execute('INSERT INTO Minha_tabela1 VALUES ("16/11/1998", "Biel","24")')

numero = random.randint(30, 51)

# Inserir informação na minha tabela
Cursor.execute(f'INSERT INTO Minha_tabela1 VALUES ("??/??/????", "Mister M", {numero})')

# * retorna todas as colunas
Consultor = Cursor.execute('SELECT * FROM Minha_tabela1').fetchall()
print(Consultor)

# Query de consulta - Colunas Específicas
Consultor = Cursor.execute('SELECT Nome, Idade FROM Minha_tabela1').fetchall()
for linha in Consultor:
    print(linha)

# Query usando o Igual "="
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome = 'Biel'
    '''
).fetchall()

print(Consulta)

# Query usando o Maior ">"
ConIdadeMaior = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade > 25
    '''
).fetchall()

print(ConIdadeMaior)

# Query usando o Menor "<"
ConIdadeMenor = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade < 25
    '''
).fetchall()

print(ConIdadeMenor)

# Query usando o Diferente "<>"
ConNomeDif = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome <> 'Mister M'
    '''
).fetchall()

print(ConNomeDif)

# combinacao AND NOT
ConIdVar = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade BETWEEN 20 AND 58
    '''
).fetchall()

print(ConIdVar)

# query LIKE com inicial do nome
ConINome = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome LIKE 'R%'
    '''
).fetchall()

print(ConINome)

# query LIKE com final do nome
ConFNome = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome LIKE '%r'
    '''
).fetchall()

print(ConFNome)

# query LIKE com parte do nome
ConPrtNome = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome LIKE '%el%'
    '''
).fetchall()

print(ConPrtNome)

# query IN
ConEmId = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade IN (23, 24, 50)
    '''
).fetchall()

print(ConEmId)

# query AND
ConIdENon = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade = 23 and Nome = 'Victor'
    '''
).fetchall()

print(ConIdENon)

# query OR
ConIdOUNon = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Idade = 23 OR Nome = 'Victor'
    '''
).fetchall()

print(ConIdOUNon)

# combinacao AND NOT
ConNoNon = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE NOT Nome = 'Victor' AND NOT Nome = 'Renan' AND NOT Nome = 'Mister M'
    '''
).fetchall()

print(ConNoNon)

# ORDER BY EM ORDEM CRESCENTE
ConODBY = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    ORDER BY Nome
    '''
).fetchall()

print(ConODBY)

# ORDER BY EM ORDEM DECRESCENTE (caso querer adicionar algo alem do nome usar a virgula)
ConODBYDE = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    ORDER BY Nome DESC
    '''
).fetchall()

print(ConODBYDE)

# Preenchendo valores nulos
Cursor.execute('INSERT INTO Minha_Tabela1 VALUES ("01/01/0000", null, 30 ) ')
Cursor.execute('INSERT INTO Minha_Tabela1 VALUES ("01/01/9999", null, null ) ')

# verificando valores nulos
ConNull = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome IS NULL
    '''
).fetchall()

print(ConNull)

# verificando valores nao nulos
ConNull = Cursor.execute(
    '''
    SELECT * FROM Minha_tabela1 
    WHERE Nome IS NOT NULL
    '''
).fetchall()

print(ConNull)

# atualizando a tabela
ATT = Cursor.execute(
    ''' 
    UPDATE Minha_Tabela1
    SET Nome = 'Alterado'
    WHERE Nome IS NULL
    '''
).fetchall()

# Verificando
ConATT = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela1
    '''
).fetchall()

print(ConATT)

# atualizando a tabela
ATTid = Cursor.execute(
    ''' 
    UPDATE Minha_Tabela1
    SET Idade = '50'
    WHERE Idade IS NULL
    '''
).fetchall()

# Verificando
ConATTid = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela1
    '''
).fetchall()

print(ConATTid)
