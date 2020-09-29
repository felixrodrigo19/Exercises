#Faça um programa que contenha um menu para as 4 operações básicas
# (Soma, subtração, Produto e Divisão) mais a opção Sair.
# O programa deve simular uma calculadora e resolver a operação entre os 2 operandos.
sair = False
while (sair != True):
    menu = str(input("Opções:\n '+'\n '-'\n'*'\n'/'\n'q' para sair: "))
    if (menu == "q"):
        sair = True
        break
    #se não foss com menu dava pra fazer a pessoa só digitar a operação com espaços e então pegar a posição 1 do vetor pra
    # definir o if e já teria os dois valores para a operação tudo em uma linha.

    numero_1 = float(input("Digite o primeiro valor: "))
    numero_2 = float(input("Digite o segundo valor: "))


    if (menu == "+"):
        result = numero_1 + numero_2
        print(f"Resultado: {result}")
        continue


    elif (menu == "-"):
        result = numero_1 - numero_2
        print(f"Resultado : {result}")
        continue

    elif (menu == "*"):
        result = numero_1 * numero_2
        print(f"Resultado : {result}")
        continue

    elif (menu =="/"):
        result=format(numero_1 / numero_2, '.2f')
        print(f"Resultado: {result}")
        continue

    else:
        print("Comando inválido")
        continue
