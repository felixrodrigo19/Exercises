import random
from statistics import mean

a = []
smaller_accountant = 0
count = 0
for x in range(10):
    a.append(random.randrange(0,10))


mean_number = mean(a)


for y in a:
    if y > mean_number:
        count += 1
    else:
        smaller_accountant += 1


print(f"Média: {mean_number} \nMaiores: {count} \nMenores: {smaller_accountant}")
