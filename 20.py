#01) Faça um programa que leia várias notas de vários alunos e armazene em umdicionário
# (o nome é a chave e as notas os valores).Faça um programa que mostre o nome do aluno e a média do aluno.



import statistics


boletim = {}
res = []


def media(dic_notas):
  print(dic_notas)
  for x in dic_notas:
      medianota = statistics.mean(dic_notas[x])
      print(x ,round(medianota, 2))


nome = str(input("Insira o nome: ")).lower()

for x in range(2):
  nota = format(float(input(f"Insira a nota do {nome} p{x}: ")), '.2f')

  if float(nota) <= 0:
      nota = 0

  elif float(nota) >= 10:
      nota = 10
  
  res.append(float(nota))
  

boletim[nome] = res


media(boletim)
