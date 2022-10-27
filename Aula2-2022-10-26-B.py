#Pede o nome do aluno e sua nota de 0 a 10. Se ele tirou nota 10, mostra "{nome} você é o bichão memo..."

nome = input("digite seu nome: ")
nota = float(input("digite sua nota: "))

if (nota == 10):
  print("{}você é o bichão memo... Nota A".format(nome))
elif ( nota >= 7 ) and (nota < 10):
  print("{} você tirou a nota B".format(nome))
elif ( nota >= 5 ) and (nota < 7):
  print("{} você tirou a nota C".format(nome))
elif ( nota >= 3 ) and (nota < 5):
  print("{} você tirou a nota D".format(nome))
else:
  print("{} você tirou a nota F".format(nome))

