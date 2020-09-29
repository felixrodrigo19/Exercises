def coordinate(X, Y):
    if X >=  0 and Y >= 0:
        print("Primeiro quadrante.")

    elif X < 0 and Y >= 0:
         print("Segundo quadrante.")

    elif X < 0 and Y < 0:
         print("Terceira quadrante.")

    else:
         print("Quarto quadrante.")

x = float(input("Ponto X: "))
y = float(input("Ponto Y: "))
coordinate(x, y)
