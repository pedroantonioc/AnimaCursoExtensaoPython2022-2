# Meu primeiro projeto Python!!!

# print() = comando de saída
print("Hello world!")

#quando quiser fazer comentários usar # ou '''  ''' para comentários em bloco 
'''
comentário em bloco
'''

# quando quiser guardar uma String! (frase) 
nome = "Pedro Carvalho"

# quando quiser guardar um número inteiro
idade = 22

#exibir o meu nome (que está dentro da variável nome)
print(nome)

#exibir minha idade (que está na variável idade)
print(idade)


#exibir a frase "minha idade é" completando com o conteúdo da variável idade.
print("minha idade é: "+str(idade))
print(f"minha idade é: {idade}\n")
print("minha idade é {}".format(idade))

'''anotações
(o str é um comando de conversão para concatenar tipos diferentes de variáveis)
(o f e {} são comandos para concatenar)
(\n é para pular linha)
(.format é outra forma de escrever o comando)
'''
#quando quiser exibir "meu nome é... e tenho... anos" trocando pelas variáveis nome e idade
print("meu nome é {} e tenho {} anos".format(nome, idade))

''' anotações
(quando quiser imprimir várias variáveis com o format, abrir chaves e depois colocar as variáveis no comando .format na ordem que quero exibilas)
'''