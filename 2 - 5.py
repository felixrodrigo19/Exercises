def payment(salary, sales_amount):
    if sales_amount < 1000:
        print(f"Salário: {salary}")

    elif sales_amount >= 1000 and sales_amount <= 5000:
        print(f"Salário: {salary + 500}")

    elif sales_amount > 5000 and sales_amount <= 7500:
        print(f"Salário: {salary + 750}")

    else:
        print(f"Salário: {salary + 1000}")


salario = float(input("Salário do vendedor: "))
vendas = float(input("Valor vendas: "))
payment(salario, vendas)
