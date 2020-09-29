lista = []

for posicao in range(20):
    lista.append(int(input("Digite um número: ")))


lista_direita = list(lista[::-1])
lista_esquerda = list(lista[::1])


print(f"Lista rotacionada para direita: {lista_direita} \nLista rotacionada para esquerda: {lista_esquerda}")
