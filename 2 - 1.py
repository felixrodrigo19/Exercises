
def imc_calculator(weight, height):
    imc = weight/(height*2)

    if imc < 18.5:
        print("Abaixo do peso.")

    elif imc > 18.5 and imc < 25:
        print("Peso Normal.")

    elif imc > 25  and imc < 30:
        print("Acima do Peso.")

    else:
        print("Obeso.")

weight = float(input("Peso:"))
height = float(input("Altura"))
imc_calculator(weight, height)
