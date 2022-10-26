#comando input(): quero permitir que o usuário digite algo...
nome = input("digite seu nome: ")

#comando de saída... exibe na tela
print(f"Boa noite, seu nome é {nome}")

#exiba "Sua idade é..."
#necessário declarar o tipo de variável pois estava armazenando direto como string
idade = int(input("digite sua idade:"))
print(f"Sua idade é {idade} anos")

#exiba com format
print("Sua idade é {}".format(idade))

dobro = idade * 2
print("o dobro da sua idade é {}".format(dobro)) 
