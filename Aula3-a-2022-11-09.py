print("início da aula 3(09/11/22)")

contador = 1

#exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador + 1 #contador += 1
# para rodar comandos como while é preciso colocar os ":", sem necessidade de incluir "{}"
#site para exemplos de laço: https://www.w3schools.com/python/python_while_loops.asp

#Laço for(python for = foe each)
fruta = "morango"

print(fruta)

#Lista
frutas = ["morango", "laranja", "pêra"]

#quero exibir apenas a terceira fruta (Pêra)
print(frutas) #aqui mostra todas
#colocar o índice da posição do item que quer mostrar da lista contando do 0 (para a maioria das linguagens é assim
print(frutas[2])
print(frutas[1])

#quantas frutas tem na minha lista? 
print(len(frutas)) #length = tamanho
#quero incluir uma fruta nova
frutas.append("manga")
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("")
print("Exemplo das frutas com o while\n")

i=0 #variável para contar
while(i<len(frutas)):
  print(frutas[i])
  i = i+1


print("")
print("Exemplo das frutas com o for\n")
# para for não pode usar parênteses.
# ele carrega a variável fruta com o primeiro item da lista(nesse caso o morango) e no próximo loop ele irá colocar a segunda fruta, etc. (processo chamado de next)
for fruta in frutas:
  print(fruta)