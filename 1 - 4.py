def currency_converter(cotacao, real):
    valor = format((real / cotacao), '.2f')
    print(f"R${real} é igual a ${valor}")


valor_cotacao = float(input("Valor da cotação: "))
valor_real = float(input("Valor em reais: "))
currency_converter(valor_cotacao, valor_real)
