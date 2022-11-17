#criação de funções

preco = 1999.90

#calcular 5% de imposto, guardar na variável imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar função calcular_imposto() que calcula imposto de 5% e retorna a quem pediu
#isto é a declaração da função (como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#aqui é o uso... imposto à calcular...
preco = 299
imposto = calcular_imposto(preco)
precofinal = preco + imposto
print(imposto)
print(precofinal)

#explicação de variável local x gobal
#variáveis criadas dentro de funções só existem lá, nesse exemplo foi criada uma fora somente para conseuguir imprimir a variável
print(preco) #???
preco_produto = 100
print(preco_produto) #???

#agora calcular imposto a alíquota é 7%
#mudar somente no método

valores = [1.99, 24.50, 78.27, 1515.5]
#se eu quiser calcular o imposto destes quatro valores e exibir na tela assim: " o imposto de ... é ..."
