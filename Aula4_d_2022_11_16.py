import Aula4_c_2022_11_16 as bd

con, cur = bd.conectar()

#conectamos acima com a função q criamos na aula 4c
nome = input("digite o nome do herói/vilão")
nome_civil = input("informe o nome civil do herói/vilão")
tipo_numerico = input("tecle 1 para Herói(na) ou 2 para Vilã(o)")

#consulta para o valor maximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico =="1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()

