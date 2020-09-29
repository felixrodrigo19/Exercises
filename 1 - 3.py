nome_produto = input("Nome do produto: ")
quantidade_comprada = int(input("Quantidade comprada: "))
valor_unitario = float(input("Valor da unidade: "))
desconto = float(input("Valor do desconto: "))
porcentagem = 1-(desconto / 100)
total = format((valor_unitario * quantidade_comprada) * porcentagem, '.2f')

print(f"Produto: {nome_produto} \nTotal: {total}")
