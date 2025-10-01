#ler 3 medidas de um triangulo verificar se realmente essas medidas formam
#um triangulo e se formarem dizer qual triangulo foi formado

a = float(input("insira o lado A:"))
b = float(input("insira o lado B:"))
c = float(input("insira o lado C:"))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and b == c:
        print("O Triangulo é valido e é Equilatero")
    elif a == b or b == c or a == c:
        print("Triangulo Isoceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Valores nao formam um triangulo")
    
