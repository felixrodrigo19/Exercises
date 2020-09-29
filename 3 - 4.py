from datetime import datetime

data_inicio = input("Informe a data de inicio:  ")
data_termino = input("Informe a data de termino:  ")

data_inicio_convert = datetime.strptime(data_inicio, "%d/%m/%Y")
data_termino_convert = datetime.strptime(data_termino, "%d/%m/%Y")

dias = abs((data_termino_convert - data_inicio_convert).days)
print(dias)
