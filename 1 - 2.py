def sum_reverses(value1, value2, value3):
    X = int(str(value1)[::-1])
    Y = int(str(value2)[::-1])
    Z = int(str(value3)[::-1])

    result = X + Y + Z
    print(f"A soma dos reversos é: {result}")


numero1 = int(input("Valor 1: "))
numero2 = int(input("Valor 2: "))
numero3 = int(input("Valor 3: "))
reverses = sum_reverses(numero1, numero2, numero3)
