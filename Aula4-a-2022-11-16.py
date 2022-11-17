#python acessando banco de dados, usando documentação ofcial da biblioteca da Mysql "sqlite3"
#1o passo: importar a biblioteca sqlite3
import sqlite3

#2o passo: vamos estabelecer uma conexão com o banco de dados (guardada em uma variável chamada conexao)
conexao = sqlite3.connect("dc_universe.db")

#3o passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4o passo: comndo sql do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5o passo: executar o comando SQL no SQLlight(no cursor)
cursor.execute(sql)

#6 passo: exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[2]})")

