#01)Faça uma rotina para calcular asraízesde uma equação do 2ºgrau.
#A rotina receberá os valores de a, b e c. E deverá retornar o tipo
#das raízese os valores das raízes.


import math


def equacao_quadratica(a, b, c):
  if a == 0:
    return print("a não deve ser zero")


  var = (b**2 - 4*a*c)
  delta = math.sqrt(var)


  if var < 0:
    return print("\nNenhuma raiz real\n x: {var}")


  else:
    x1 = ((-B + delta) / (2 * A))
    x2 = ((-B - delta) / (2 * A))

    if delta == 0:
      return print ("\nRaíz única\nX1: {x1}\nX2: {x2} ")

    else:
      return print(f"Duas raízes reais\nX1: {x1}\nX2: {x2} ")


A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))


equacao_quadratica(A, B, C)
