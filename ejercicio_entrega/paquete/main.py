from geometria import area_circulo, area_cuadrado, area_triangulo
from perimetros import perimetro_circulo, perimetro_cuadrado, perimetro_triangulo

def main():
    # Calcular áreas
    radio = 5
    lado_cuadrado = 4
    base_triangulo = 6
    altura_triangulo = 7

    area_c = area_circulo(radio)
    area_sq = area_cuadrado(lado_cuadrado)
    area_t = area_triangulo(base_triangulo, altura_triangulo)

    print(f"Área del círculo con radio {radio}: {area_c}")
    print(f"Área del cuadrado con lado {lado_cuadrado}: {area_sq}")
    print(f"Área del triángulo con base {base_triangulo} y altura {altura_triangulo}: {area_t}")

    # Calcular perímetros
    perimetro_c = perimetro_circulo(radio)
    perimetro_sq = perimetro_cuadrado(lado_cuadrado)
    lado1 = 3
    lado2 = 4
    lado3 = 5
    perimetro_t = perimetro_triangulo(lado1, lado2, lado3)

    print(f"Perímetro del círculo con radio {radio}: {perimetro_c}")
    print(f"Perímetro del cuadrado con lado {lado_cuadrado}: {perimetro_sq}")
    print(f"Perímetro del triángulo con lados {lado1}, {lado2}, y {lado3}: {perimetro_t}")

