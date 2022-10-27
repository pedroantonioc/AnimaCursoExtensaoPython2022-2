# 1 - comando input(): quero permitir que o usuário digite algo...
nome = input("digite seu nome: ")

#comando de saída... exibe na tela
print(f"Boa noite, seu nome é {nome}")

#exiba "Sua idade é..."
#necessário declarar o tipo de variável pois estava armazenando direto como string
idade = int(input("digite sua idade:"))
print(f"Sua idade é {idade} anos")

#exiba com format
dobro = idade * 2
print("o dobro da sua idade é {}".format(dobro)) 

# 2 - estrutura condicional - o famoso "SE" (if)
# se a pessoa for maior de idade, mostre " você é maior de idade, já pode beber ou dirigir"
#condição if precisa de ":" para indicar qual linha será condicionada
# para amarrar á função if as linhas de codigo precisam ter o recuo, caso contrário não serão dependentes da condição e serão rodadas normalmente.
if (idade >= 18):
  print("você é maior de idade, ótimo! Já pode beber ou dirigir!")
#senão é o contrário da condição que estabeleceu no if(também precisa dos ":")
else:
  print("você é menor de idade, que pena! Não pode dirigir nem beber!")



# e se eu quisesse perguntar o gênero (m = masculino e f = Feminino), mostre (e você também precisa prestar o serviço obrigatório militar)

genero = input("informe o gênero (M = Masculino, F=Feminino, O = Outros)\n")

if (idade >= 18) and (genero == "M"):
  print("você precisa prestar o serviço obrigatório militar")
else:
  print("você não precisa prestar o serviço obrigatório militar")