import re
from collections import Counter


#01) Faça um programa que retorne a quantidade de vogais de uma frase.
def conta_vogais(texto):
  return Counter(re.sub('[^aeiouAEIOU]', '', texto))


# 02) Faça um programa que leia uma frase e retorne a frase sem as vogais.
def remove_vogais(texto):
  return texto.translate(texto.maketrans("", "", "aeiouAEIOU"))


# 03) Faça um programa que retorne uma frase sem os espaços em branco.
def remove_espacos(texto):
  return texto.replace(" ", "")


texto = input("Insira o texto: ")
print(f"Contador de vogais: {conta_vogais(texto)}")
print(f"Frase sem vogais: {remove_vogais(texto)}")
print(f"Frase sem espaços: {remove_espacos(texto)}")
