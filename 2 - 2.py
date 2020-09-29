def triangles(A,B,C):
    if (A <= (B + C)) and (B <= (A + C)) and (C <= (A + B)):
        print("Forma um triangulo")
    else:
        print("Não forma um triangulo")

lado1 = float(input("Medida do lado A"))
lado2 = float(input("Medida do lado B"))
lado3 = float(input("Medida do lado C"))
triangles(lado1, lado2, lado3)
