import sqlite3
import os
# sqlite3 permite criar um banco de dados local
# já vem disponível nas bibliotecas python

# a linguagem SQL é a resp por escrever o código de manipulação dos bancos de dados 
# criando funções para facilitar a manipulação do banco de dados

# crie um banco de dados e conecte, se já existir, apenas conecte 

def conectar():
    conn = sqlite3.connect('score.db')
    return conn

def desconectar(conn):
    conn.close()
    
# para acontecer alguma manipulação no sqlite, é necessário criar um cursor e o conectá-lo
# consulta sql para criar uma tabela:
 
def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS score_jogo (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor_score INTEGER NOT NULL
    )    
    """)    
    conn.commit()

# commit, neste caso, permite que a consulta sql seja efetivada


def inserir_dado(nome, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO score_jogo (nome, valor_score)
        VALUES (?, ?)
    """, (nome, valor))  
    conn.commit()
    desconectar(conn)
    
def listar_dados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM score_jogo
        ORDER BY valor_score DESC
    """)  
    dados = cursor.fetchall()
    conn.commit()
    desconectar(conn)
    return dados

# fetchall pega todos os dados e joga numa lista
